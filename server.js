const express = require('express');
const path = require('path');
const app = express();
const PORT = 5051;

// Servir archivos estáticos
app.use(express.static(path.join(__dirname)));

// Ruta por defecto
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'index.html'));
});

// Iniciar servidor
app.listen(PORT, () => {
  console.log(`🚀 Servidor ejecutándose en http://localhost:${PORT}`);
});
