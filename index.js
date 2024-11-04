const express = require('express');
const addon = require('stremio-addon-sdk');

const manifest = {
  "id": "community.glorioso.addon",
  "version": "1.0.0",
  "name": "GloriosoTV Addon",
  "description": "Addon para acessar a lista GloriosoTV.",
  "types": ["tv"],
  "resources": ["stream"],
  "idPrefixes": ["gloriosotv"],
  "catalogs": []
};

const builder = new addon(manifest);

// Exemplo de URL da lista
const IPTV_URL = "https://raw.githubusercontent.com/gloriosotv/Server/refs/heads/main/Lista-GloriosoTv";

builder.defineStreamHandler(async (args) => {
  // Aqui você deve adicionar a lógica para buscar a URL específica de acordo com o `args`
  return {
    streams: [{
      title: "GloriosoTV",
      url: IPTV_URL
    }]
  };
});

const app = express();
app.use('/', addon.middleware(builder));
app.listen(7000, () => {
  console.log('Addon funcionando na porta 7000');
});
