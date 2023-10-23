// Chamar a biblioteca do express para criação de rotas
const express = require('express');

// Você da um "apelido" para a biblioteca
const app = express();

// Chamando a abertura do meu serviço
// Criação do servidor express
app.listen(8080);
// da um 'node index.js' para iniciar o servidor, e 'ctrl + c' para parar o servidor

// Criação da rota
app.get('/', () => {
  console.log('Hello World!!')
});