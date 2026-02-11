#!/usr/bin/env node
const Replicate = require('replicate');
const fs = require('fs');
const path = require('path');
const https = require('https');

// Leer API key del archivo
const apiKeyFile = path.join(__dirname, '.replicate-api-key');
const apiToken = fs.readFileSync(apiKeyFile, 'utf8').trim();

const replicate = new Replicate({
  auth: apiToken,
});

// Helper para descargar imagen
async function downloadImage(url, filename) {
  return new Promise((resolve, reject) => {
    const file = fs.createWriteStream(filename);
    https.get(url, (response) => {
      response.pipe(file);
      file.on('finish', () => {
        file.close();
        resolve(filename);
      });
    }).on('error', reject);
  });
}

async function generateImage(prompt) {
  try {
    console.log(`🎨 Generando imagen con google/imagen-4`);
    console.log(`📝 Prompt: "${prompt}"\n`);
    console.log('⏳ Procesando (esto puede tardar ~30-60 segundos)...\n');

    const prediction = await replicate.run(
      "google/imagen-4",
      {
        input: {
          prompt: prompt,
          aspect_ratio: "1:1",
          negative_prompt: "",
          quality: "standard",
          safety_filter_level: "block_only_high"
        }
      }
    );

    // google/imagen-4 retorna array de URLs o string URL
    let imageUrl = null;
    
    if (Array.isArray(prediction) && prediction.length > 0) {
      imageUrl = prediction[0];
    } else if (typeof prediction === 'string') {
      imageUrl = prediction;
    }

    if (imageUrl) {
      console.log('✅ Imagen generada exitosamente!');
      console.log(`\n📸 URL: ${imageUrl}`);
      
      // Descargar la imagen
      const filename = `/tmp/generated-image-${Date.now()}.jpg`;
      console.log(`\n⬇️  Descargando...`);
      await downloadImage(imageUrl, filename);
      console.log(`✓ Guardada en: ${filename}`);
      
      return {
        url: imageUrl,
        filename: filename
      };
    } else {
      console.log('⚠️ Respuesta inesperada:');
      console.log(JSON.stringify(prediction, null, 2));
      return null;
    }
  } catch (error) {
    console.error('❌ Error generando imagen:');
    console.error(error.message);
    process.exit(1);
  }
}

// Usar prompt del argumento o default
const prompt = process.argv[2] || "un gato naranja jugando con un ovillo de lana en una habitación acogedora";
generateImage(prompt);
