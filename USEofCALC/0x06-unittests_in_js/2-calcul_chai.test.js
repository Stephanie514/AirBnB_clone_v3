// 2-calcul_chai.test.js
const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', () => {
  describe('SUM', () => {
    it('should return 6 when type is SUM, a is 1.4, and b is 4.5', () => {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });

    it('should return 4 when type is SUM, a is 2.0, and b is 2.0', () => {
      expect(calculateNumber('SUM', 2.0, 2.0)).to.equal(4);
    });

    it('should return 4 when type is SUM, a is 2.3, and b is 1.8', () => {
      expect(calculateNumber('SUM', 2.3, 1.8)).to.equal(4);
    });

    it('should return -4 when type is SUM, a is -2.0, and b is -2.0', () => {
      expect(calculateNumber('SUM', -2.0, -2.0)).to.equal(-4);
    });

    it('should return -4 when type is SUM, a is -2.3, and b is -1.8', () => {
      expect(calculateNumber('SUM', -2.3, -1.8)).to.equal(-4);
    });

    it('should return 0 when type is SUM, a is -2.0, and b is 2.0', () => {
      expect(calculateNumber('SUM', -2.0, 2.0)).to.equal(0);
    });

    it('should return 0 when type is SUM, a is 2.0, and b is -2.0', () => {
      expect(calculateNumber('SUM', 2.0, -2.0)).to.equal(0);
    });

    it('should return 0 when type is SUM, a is 0.0, and b is 0.0', () => {
      expect(calculateNumber('SUM', 0.0, 0.0)).to.equal(0);
    });
  });

  describe('SUBTRACT', () => {
    it('should return 0 when type is SUBTRACT, a is 2.0, and b is 2.0', () => {
      expect(calculateNumber('SUBTRACT', 2.0, 2.0)).to.equal(0);
    });

    it('should return 0 when type is SUBTRACT, a is 2.3, and b is 1.8', () => {
      expect(calculateNumber('SUBTRACT', 2.3, 1.8)).to.equal(0);
    });

    it('should return 0 when type is SUBTRACT, a is -2.0, and b is -2.0', () => {
      expect(calculateNumber('SUBTRACT', -2.0, -2.0)).to.equal(0);
    });

    it('should return 0 when type is SUBTRACT, a is -2.3, and b is -1.8', () => {
      expect(calculateNumber('SUBTRACT', -2.3, -1.8)).to.equal(0);
    });

    it('should return -4 when type is SUBTRACT, a is -2.0, and b is 2.0', () => {
      expect(calculateNumber('SUBTRACT', -2.0, 2.0)).to.equal(-4);
    });

    it('should return 4 when type is SUBTRACT, a is 2.0, and b is -2.0', () => {
      expect(calculateNumber('SUBTRACT', 2.0, -2.0)).to.equal(4);
    });

    it('should return 0 when type is SUBTRACT, a is 0.0, and b is 0.0', () => {
      expect(calculateNumber('SUBTRACT', 0.0, 0.0)).to.equal(0);
    });
  });

  describe('DIVIDE', () => {
    it('should return 4 when type is DIVIDE, a is 8.0, and b is 2.0', () => {
      expect(calculateNumber('DIVIDE', 8.0, 2.0)).to.equal(4);
    });

    it('should return -3.5 when type is DIVIDE, a is -7.0, and b is 2.0', () => {
      expect(calculateNumber('DIVIDE', -7.0, 2.0)).to.equal(-3.5);
    });

    it('should return -3.5 when type is DIVIDE, a is 7.0, and b is -2.0', () => {
      expect(calculateNumber('DIVIDE', 7.0, -2.0)).to.equal(-3.5);
    });

    it('should return 3.5 when type is DIVIDE, a is -7.0, and b is -2.0', () => {
      expect(calculateNumber('DIVIDE', -7.0, -2.0)).to.equal(3.5);
    });

    it('should return 1 when type is DIVIDE, a is 2.0, and b is 2.0', () => {
      expect(calculateNumber('DIVIDE', 2.0, 2.0)).to.equal(1);
    });

    it('should return 1 when type is DIVIDE, a is -2.0, and b is -2.0', () => {
      expect(calculateNumber('DIVIDE', -2.0, -2.0)).to.equal(1);
    });

    it('should return 1 when type is DIVIDE, a is 2.6, and b is 3.0', () => {
      expect(calculateNumber('DIVIDE', 2.6, 3.0)).to.equal(1);
    });

    it('should return 1 when type is DIVIDE, a is 2.4, and b is 2.0', () => {
      expect(calculateNumber('DIVIDE', 2.4, 2.0)).to.equal(1);
    });

    it('should return 0 when type is DIVIDE, a is 0.0, and b is 5.0', () => {
      expect(calculateNumber('DIVIDE', 0.0, 5.0)).to.equal(0);
    });

    it('should return -0 when type is DIVIDE, a is 0.0, and b is -5.0', () => {
      expect(calculateNumber('DIVIDE', 0.0, -5.0)).to.equal(-0);
    });

    it('should return "Error" when type is DIVIDE, a is 5.0, and b is 0', () => {
      expect(calculateNumber('DIVIDE', 5.0, 0)).to.equal('Error');
    });

    it('should return "Error" when type is DIVIDE, a is 5.0, and b is 0.2', () => {
      expect(calculateNumber('DIVIDE', 5.0, 0.2)).to.equal('Error');
    });

    it('should return "Error" when type is DIVIDE, a is 5.0, and b is -0.2', () => {
      expect(calculateNumber('DIVIDE', 5.0, -0.2)).to.equal('Error');
    });

    it('should return "Error" when type is DIVIDE, a is -5.0, and b is 0', () => {
      expect(calculateNumber('DIVIDE', -5.0, 0)).to.equal('Error');
    });

    it('should return "Error" when type is DIVIDE, a is -5.0, and b is 0.2', () => {
      expect(calculateNumber('DIVIDE', -5.0, 0.2)).to.equal('Error');
    });

    it('should return "Error" when type is DIVIDE, a is -5.0, and b is -0.2', () => {
      expect(calculateNumber('DIVIDE', -5.0, -0.2)).to.equal('Error');
    });

    it('should return "Error" when type is DIVIDE, a is 0.0, and b is 0.0', () => {
      expect(calculateNumber('DIVIDE', 0.0, 0.0)).to.equal('Error');
    });
  });
});
