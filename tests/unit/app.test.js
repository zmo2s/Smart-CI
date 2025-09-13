const request = require('supertest');
const app = require('../../app');

describe('GET /hello', () => {
  it('should respond with "Hello, world!"', async () => {
    const res = await request(app).get('/hello');
    expect(res.statusCode).toBe(200);
    expect(res.body.message).toBe('Hello, world!');
  });
});

