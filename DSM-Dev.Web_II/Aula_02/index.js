const express = require("express");

const app = express()

// app.get("/",()=>{
//   console.log("Hello world");
// })

app.listen(8080,()=>console.log("O server está ativo na porta 8080"));

let nome = "Leonardo";
let cor = "green";

app.get("/",(req, res)=>{
  res.send(`<h1 style="color: ${cor}">Olá ${nome}!</h1>`);
});

app.post("/getHTML",(req, res)=>{
  const { nome } = req.body;
  console.log(`Olá ${nome}`);
})
