const express = require('express');
const iconv = require('iconv-lite');
const { PythonShell } = require('python-shell');
const translatorFile = process.env.translatorFile || 'translator.py';
const translatorWriteFile = process.env.translatorWriteFile || 'write-file.py';

const router = express.Router();

let options = {
  mode: 'text',
  scriptPath: '',
  encoding: 'binary'
};

/* GET home page. */
router.get('/', (req, res, next) => res.render('index.html'));

router.post('/translator', (req, res, next) => {
  const { text } = req.body;
  
  if (!text) {
    next();
  }

  options.args = [text];

  const test = new PythonShell(`./${translatorFile}`, options);

  test.on('message', msg => {
    const buff = new Buffer.from(msg, 'binary');
    const result = iconv.decode(buff, 'EUC-KR');
    res.status(200).json({ text: result })
  });
});

router.post('/translator/add', (req, res, next) => {
  const { english, korean } = req.body;

  if (!english || !korean) {
    next();
  }

  options.args = [english, korean];

  const test = new PythonShell(`./${translatorWriteFile}`, options);

  test.on('message', msg => res.status(200).json({ text: msg }))
})

module.exports = router;