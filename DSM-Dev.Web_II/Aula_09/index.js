const express = require("express");
const jwt = require("jsonwebtoken");

const app = express();

app.listen(8080, () => {
  console.log('O servidor está ativo!');
})

const segredo = "minhaSenha";

function verifyToken(req, res, next) {
  // essa const pega esse token do cabeçalho
  const token = req.headers.authorization;

  // faz a verificação se o token foi encontrado ou não
  if (!token) {
    res.status(401).json({ message: 'Token não fornecido!' });
    return
  }

  try {
    const decodificado = jwt.verify(token, segredo);
    req.user = decodificado;
    next()
  } catch (err) {
    res.status(403).json({ message: 'Token inválido!' })
  }
}

app.post("/login", (req, res) => {
  const user = {
    id: 123,
    name: 'Victor',
    password: '123victor'
  }

  const token = jwt.sign(user, segredo);
  res.status(200).json({ token });
})

app.get("/userProt", verifyToken, (req, res) => {
  const { id, name, password } = req.user;

  res.status(200).json({ id, name, password });
})