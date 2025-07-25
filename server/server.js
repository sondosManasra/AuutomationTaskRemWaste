const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
app.use(cors());
app.use(bodyParser.json());

// --- In-Memory Data ---
const users = [{ username: 'admin', password: '1234' }];
let todos = [
    { id: 1, title: 'First Todo', user: 'admin' }
];

// --- Auth Route ---
app.post('/api/login', (req, res) => {
    const { username, password } = req.body;
    const user = users.find(u => u.username === username && u.password === password);
    if (user) {
        res.json({ success: true, username });
    } else {
        res.status(401).json({ success: false, message: 'Invalid credentials' });
    }
});

// --- CRUD Routes ---
app.get('/api/todos', (req, res) => {
    res.json(todos);
});

app.post('/api/todos', (req, res) => {
    const { title, user } = req.body;
    const newTodo = { id: Date.now(), title, user };
    todos.push(newTodo);
    res.json(newTodo);
});

app.put('/api/todos/:id', (req, res) => {
    const { id } = req.params;
    const { title } = req.body;
    const todo = todos.find(t => t.id == id);
    if (todo) {
        todo.title = title;
        res.json(todo);
    } else {
        res.status(404).json({ message: 'Todo not found' });
    }
});

app.delete('/api/todos/:id', (req, res) => {
    const { id } = req.params;
    todos = todos.filter(t => t.id != id);
    res.json({ success: true });
});

const PORT = 5000;
app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
