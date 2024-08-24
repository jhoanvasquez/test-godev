export default function ({ $axios, store }) {
  $axios.interceptors.response.use(
    response => {
      store.commit('updateData', response.data)
      return response;
    },
    error => {
      return Promise.reject(error);
    }
  );
}