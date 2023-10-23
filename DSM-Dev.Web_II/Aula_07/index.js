const express = require("express");

const app = express();

app.use(express.json());

app.listen(8080, () => {
  console.log("O servidor está ativo na porta 8080");
})

let Alunos = ['Maria', 'João', 'Lucas', 'Marcio', 'Victor'];

// CRUD - CREATE, READ, UPDATE, DELETE
// POST, GET, PUT, DELETE

// CREATE
app.post('/includeAluno', (req, res) => {
  const { nome } = req.body;
  Alunos.push(nome);
  res.send(`<h1>Olá ${nome}, tudo bem?</h1>`);
  console.log(Alunos);
})


// READ
app.get('/getAluno', (req, res) => {
  const { index } = req.body;

  // CONNECT SQL
  // SELECT * FROM Alunos WHERE id = index
  res.send(`<h1>O aluno ${Alunos[index]} foi encontrado!</h1>`);
});

app.get('/getAlunos', (req, res) => {
  // SELECT * FROM Alunos
  console.log(Alunos);
  res.send(`Esses são todos os alunos cadastrados: ${Alunos}`);
});

// UPDATE
// app.post
app.put('/updateAluno', (req, res) => {
  const {index, nome} = req.body;

  // UPDATE nome FROM Alunos WHERE id = index
  Alunos[index] = nome;
  res.send('<h1>O nome foi atualizado com sucesso!</h1>');
  console.log(Alunos);
});

//DELETE
app.delete('/deleteAluno', (req, res) => {
  const { index } = req.body;

  // DELETE FROM Alunos WHERE id = index
  const deleted = Alunos.splice(index, 1);
  res.send(`<h1>O aluno ${deleted} foi deletado e sobraram: ${Alunos}`);
});