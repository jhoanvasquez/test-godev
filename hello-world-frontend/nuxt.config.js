export default {
  target: 'static',
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/dotenv',
  ],

  plugins: [
    '~/plugins/axios.js',
  ],

  axios: {
    // Axios module configuration
    baseURL: 'https://rickandmortyapi.com/api/character', // Set the base URL for API requests
  },
}