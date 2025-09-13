const app = require('../../app');
const request = require('supertest');

describe('GET /hello', () => {
  it('should return Hello message', async () => {
    const res = await request(app).get('/hello');
    expect(res.statusCode).toBe(200);
    expect(res.body.message).toBe('Hello, world!');
  });
});