const express = require('express');
const bodyParser = require('body-parser');
const tasks = require('./tasks');

const app = express();

app.use(express.json());
app.use(bodyParser.json());

app.listen(8080, () => {
  console.log("O servidor esta ativo!!")
});

let createId = () => {
  let id;
  do {
    id = '';
    for(let i = 0; i < 3; i++) {
      id += Math.floor(Math.random() * 9);
    }
  }
  while (id === '000' || tasks.find((e) => e.id === parseInt(id)));
  return id;
};

app.get('/tasks', (req, res) => {
  res.send(tasks);
});

app.get('/tasks/:id', (req, res) => {
  const id = String(req.params.id);
  const task = tasks.find(task => task.id === id);

  if (!task) {
    res.status(404).send(`Tarefa com ID ${id} não existe!!!`);
  }
  else {
    res.send(task);
  }
});

app.post('/tasks', (req, res) => {
  const {title, description} = req.body;

  if(!title) {
    res.status(400).send('O campo "title" é obrigatório!');
  }
  else {
    const newTask = {
      id: createId(),
      title,
      description,
      completed: req.body.completed || false
    };
    tasks.push(newTask);
    res.send(newTask);
  }
});

app.put('/tasks/:id', (req, res) => {
  const id = String(req.params.id);
  const taskIndex = tasks.findIndex(task => task.id === id);

  if (taskIndex < 0) {
    res.status(404).send(`Tarefa com ID ${id} não existe!!!`);
  }
  else {
    const {title, description, completed} = req.body;

    tasks[taskIndex] = {
      ...tasks[taskIndex],
      title: title || tasks[taskIndex].title,
      description: description || tasks[taskIndex].description,
      completed: completed === undefined ? tasks[taskIndex].completed : completed
    };

    res.send(tasks[taskIndex]);
  }
});

app.delete('/tasks/:id', (req, res) => {
  const taskId = String(req.params.id);
  const taskIndex = tasks.findIndex(task => task.id === taskId);

  if (taskIndex === -1) {
    res.status(404).send(`Tarefa não existe!!!`);
  }
  else {
    tasks.splice(taskIndex, 1);
    res.send('Tarefa removida com sucesso!');
  }
});