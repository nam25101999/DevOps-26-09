const express = require('express');
const path = require('path');
const fs = require('fs');
const pool = require('./db');

const app = express();
const PORT = process.env.PORT || 3000;

// Cấu hình CORS để cho phép gọi API trực tiếp
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*');
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
  next();
});

// API: kiểm tra kết nối database (dùng cho badge trạng thái trên web)
app.get('/api/health', async (req, res) => {
  try {
    const result = await pool.query('SELECT COUNT(*) FROM words');
    res.json({ db: 'connected', words: Number(result.rows[0].count) });
  } catch (err) {
    res.status(503).json({ db: 'disconnected', error: err.message });
  }
});

// API: lấy danh sách từ (để đổ vào listbox)
app.get('/api/words', async (req, res) => {
  try {
    const result = await pool.query('SELECT word FROM words ORDER BY word');
    res.json(result.rows.map((row) => row.word));
  } catch (err) {
    res.status(503).json({ error: 'Không truy vấn được database' });
  }
});

// API: tra nghĩa 1 từ cụ thể
app.get('/api/define/:word', async (req, res) => {
  const word = req.params.word.toLowerCase();
  try {
    const result = await pool.query(
      'SELECT word, definition FROM words WHERE word = $1',
      [word]
    );
    if (result.rows.length === 0) {
      return res.status(404).json({ error: 'Không tìm thấy từ này' });
    }
    res.json(result.rows[0]);
  } catch (err) {
    res.status(503).json({ error: 'Không truy vấn được database' });
  }
});

// API: đọc và trả về nội dung file MSSV
app.get('/api/mssv', (req, res) => {
  const possiblePaths = [
    path.join(__dirname, 'mssv', 'mssv.txt'),
    path.join(__dirname, 'mssv.txt'),
  ];
  for (const p of possiblePaths) {
    if (fs.existsSync(p)) {
      return res.type('text/plain').send(fs.readFileSync(p, 'utf8'));
    }
  }
  res.status(404).json({ error: 'Không tìm thấy file mssv.txt' });
});

// Phục vụ file tĩnh nếu có thư mục public (tương thích backward)
const publicPath = path.join(__dirname, 'public');
if (fs.existsSync(publicPath)) {
  app.use(express.static(publicPath));
  app.get('*', (req, res) => {
    res.sendFile(path.join(publicPath, 'index.html'));
  });
} else {
  app.get('/', (req, res) => {
    res.send('Backend Dictionary API is running');
  });
}

app.listen(PORT, () => {
  console.log(`Server đang chạy tại http://localhost:${PORT}`);
});
