// npm i nodemon express

const express = require("express");

const app = express();

app.use(express.json());

app.listen(8080, () => {
  console.log("O servidor está ativo na porta 8080");
})

// CRUD - CREATE, READ, UPDATE, DELETE
// POST, GET, PUT, DELETE
app.get('/', () => {
  console.log('DEU CERTO!!!')
});

// SELECT * FROM Alunos WHERE id = 123
app.get('/getAluno', (req, res) => {
  const {id} = req.body;
  console.log(`O aluno de id: ${id} foi encontrado!`) // fica visível no terminal
  res.send(`O aluno de id: ${id} foi encontrado!`) // fica visível no front
})