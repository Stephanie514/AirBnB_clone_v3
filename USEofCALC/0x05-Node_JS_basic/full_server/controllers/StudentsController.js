import readDatabase from '../utils';

class StudentsController {
  static async getAllStudents(req, res) {
    try {
      const students = await readDatabase(req.dbFilePath);
      let response = 'This is the list of our students\n';

      Object.entries(students).forEach(([field, names]) => {
        response += `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}\n`;
      });

      res.status(200).send(response);
    } catch (error) {
      res.status(500).send(error.message);
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      return res.status(500).send('Major parameter must be CS or SWE');
    }

    try {
      const students = await readDatabase(req.dbFilePath);
      const names = students[major] || [];

      res.status(200).send(`List: ${names.join(', ')}`);
    } catch (error) {
      res.status(500).send(error.message);
    }
  }
}

export default StudentsController;
