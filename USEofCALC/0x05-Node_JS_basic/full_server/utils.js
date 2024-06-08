import fs from 'fs';

const readDatabase = (filePath) => new Promise((resolve, reject) => {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
    } else {
      const lines = data.trim().split('\n');
      const students = {};

      lines.forEach((line) => {
        const [name, , , field] = line.split(',');
        if (!students[field]) students[field] = [];
        students[field].push(name);
      });

      resolve(students);
    }
  });
});

export default readDatabase;
