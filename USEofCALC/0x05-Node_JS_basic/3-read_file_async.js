//  function named countStudents-accepts  path in argument (same as in 2-read_file.js
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
      } else {
        const lines = data.split('\n').filter((line) => line.trim() !== '');

        if (lines.length === 0) {
          reject(new Error('Cannot load the database'));
          return;
        }

        const students = lines.slice(1).map((line) => line.split(',')).filter((student) => student.length === 4);
        const numberOfStudents = students.length;
        console.log(`Number of students: ${numberOfStudents}`);

        const fields = {};

        students.forEach(([firstname, , , field]) => {
          if (!fields[field]) {
            fields[field] = [];
          }
          fields[field].push(firstname);
        });

        for (const [field, names] of Object.entries(fields)) {
          console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
        }

        resolve();
      }
    });
  });
}

module.exports = countStudents;
