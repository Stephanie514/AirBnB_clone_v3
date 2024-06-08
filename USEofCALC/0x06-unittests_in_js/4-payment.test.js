// 4-payment.test.js file

const sinon = require('sinon');
const chai = require('chai');
const { expect } = chai;

const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', () => {
  let stub;

  beforeEach(() => {
    stub = sinon.stub(Utils, 'calculateNumber').returns(10);
  });

  afterEach(() => {
    stub.restore();
  });

  it('stub calculates sum correctly', () => {
    sendPaymentRequestToApi(100, 20);
    expect(stub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
  });

  it('console.log logs correct message', () => {
    const consoleSpy = sinon.spy(console, 'log');
    sendPaymentRequestToApi(100, 20);
    expect(consoleSpy.calledOnceWithExactly('The total is: 10')).to.be.true;
    consoleSpy.restore();
  });
});
