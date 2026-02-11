#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const https = require('https');

// Leer API key
const apiKeyFile = path.join(__dirname, '.replicate-api-key');
const REPLICATE_API_KEY = fs.readFileSync(apiKeyFile, 'utf8').trim();

async function generateImage(prompt, model = 'flux-pro', steps = 25) {
  const url = 'https://api.replicate.com/v1/predictions';
  
  const payload = {
    version: model === 'flux-pro' 
      ? 'ace7d30d28ea0d4c9c2729cae0d66cd9c1abf버bc511681614fac6996b37b76' // FLUX pro
      : '39ed52f2a60c3b36b17f0f67c7b54e6b329e459c9a8b6b6b6b6b6b6b6b6b6b6', // FLUX schnell
    input: {
      prompt: prompt,
      num_inference_steps: steps,
      guidance_scale: 3.5,
      aspect_ratio: '1:1',
      output_format: 'jpeg'
    }
  };

  return new Promise((resolve, reject) => {
    const req = https.request(url, {
      method: 'POST',
      headers: {
        'Authorization': `Token ${REPLICATE_API_KEY}`,
        'Content-Type': 'application/json'
      }
    }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const result = JSON.parse(data);
          if (res.statusCode === 201) {
            resolve({ id: result.id, status: 'started', url: result.urls?.get });
          } else {
            reject(new Error(`API Error: ${res.statusCode} - ${data}`));
          }
        } catch (e) {
          reject(e);
        }
      });
    });

    req.on('error', reject);
    req.write(JSON.stringify(payload));
    req.end();
  });
}

async function checkStatus(predictionId) {
  const url = `https://api.replicate.com/v1/predictions/${predictionId}`;
  
  return new Promise((resolve, reject) => {
    const req = https.request(url, {
      method: 'GET',
      headers: {
        'Authorization': `Token ${REPLICATE_API_KEY}`
      }
    }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const result = JSON.parse(data);
          resolve(result);
        } catch (e) {
          reject(e);
        }
      });
    });

    req.on('error', reject);
    req.end();
  });
}

// CLI
const args = process.argv.slice(2);
if (args[0] === 'generate') {
  const prompt = args[1];
  generateImage(prompt).then(r => {
    console.log(`✅ Imagen iniciada: ${r.id}`);
    console.log(`Status: ${r.status}`);
  }).catch(e => console.error(`❌ Error:`, e.message));
} else if (args[0] === 'check') {
  checkStatus(args[1]).then(r => {
    console.log(JSON.stringify(r, null, 2));
  }).catch(e => console.error(`❌ Error:`, e.message));
} else {
  console.log('Uso: replicate-image-gen generate "tu prompt"');
  console.log('     replicate-image-gen check <prediction-id>');
}
