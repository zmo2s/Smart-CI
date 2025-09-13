const request = require('supertest');
const app = require('../../app');

describe('GET /hello', () => {
  it('should respond with JSON containing "Hello, world!"', async () => {
    const res = await request(app).get('/hello');
    expect(res.statusCode).toBe(200);
    expect(res.body).toEqual({ message: 'Hello, world!' });
  });
});
