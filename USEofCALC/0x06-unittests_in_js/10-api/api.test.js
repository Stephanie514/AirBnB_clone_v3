const request = require('request');
const { expect } = require('chai');
const axios = require('axios');

describe('Cart page', () => {
  it('Correct status code when :id is a number', (done) => {
    request.get('http://localhost:7865/cart/12', (error, response, body) => {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('Correct status code when :id is NOT a number (=> 404)', (done) => {
    request.get('http://localhost:7865/cart/hello', (error, response, body) => {
      expect(response.statusCode).to.equal(404);
      done();
    });
  });
});

describe('API integration test', () => {
  const API_URL = 'http://localhost:7865';

  it('GET / returns correct response', async () => {
    const response = await axios.get(`${API_URL}/`);
    expect(response.status).to.equal(200);
    expect(response.data).to.equal('Welcome to the payment system');
  });

  it('GET /cart/:id returns correct response for valid :id', async () => {
    const response = await axios.get(`${API_URL}/cart/47`);
    expect(response.status).to.equal(200);
    expect(response.data).to.equal('Payment methods for cart 47');
  });

  it('GET /cart/:id returns 404 response for negative number values in :id', async () => {
    try {
      await axios.get(`${API_URL}/cart/-47`);
    } catch (error) {
      expect(error.response.status).to.equal(404);
    }
  });

  it('GET /cart/:id returns 404 response for non-numeric values in :id', async () => {
    try {
      await axios.get(`${API_URL}/cart/hello`);
    } catch (error) {
      expect(error.response.status).to.equal(404);
    }
  });

  describe('/available_payments endpoint', () => {
    it('GET /available_payments returns correct response', async () => {
      const response = await axios.get(`${API_URL}/available_payments`);
      expect(response.status).to.equal(200);
      expect(response.data).to.deep.equal({
        payment_methods: {
          credit_cards: true,
          paypal: false
        }
      });
    });
  });

  describe('/login endpoint', () => {
    it('POST /login returns correct response', async () => {
      const response = await axios.post(`${API_URL}/login`, { userName: 'Betty' }, {
        headers: {
          'Content-Type': 'application/json'
        }
      });
      expect(response.status).to.equal(200);
      expect(response.data).to.equal('Welcome Betty');
    });

    it('POST /login without userName returns 400', async () => {
      try {
        await axios.post(`${API_URL}/login`, {}, {
          headers: {
            'Content-Type': 'application/json'
          }
        });
      } catch (error) {
        expect(error.response.status).to.equal(400);
      }
    });
  });
});
