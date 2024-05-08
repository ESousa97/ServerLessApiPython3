// next.config.js
module.exports = {
  async rewrites() {
    return [
      {
        source: '/api/:path*',
        destination: process.env.NODE_ENV === 'production' ? 'https://server-less-api-python3.vercel.app/api/:path*' : 'http://localhost:5002/:path*',
      },
      {
        source: '/upload-excel*',
        destination: process.env.NODE_ENV === 'production' ? 'https://server-less-api-python3.vercel.app/upload-excel*' : 'http://localhost:5002/upload-excel',
      }
    ]
  },
};
