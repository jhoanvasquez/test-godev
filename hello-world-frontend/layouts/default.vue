<template>
  <div>
    <header class="header">
    <h1>Rick and Morty</h1>
  </header>

    <main>
      <div>
        <characterList :characters="charactersData.results" />
      </div>
    </main>
  </div>
</template>

<script>
import CharacterList from '~/components/CharacterList.vue';

export default {
  name: 'DefaultLayout',
  components: {
    CharacterList
  },
  data() {
    return {
      charactersData: {
        info: {},
        results: []
      }
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      this.$axios.get(process.env.POKEAPI_URL)
        .then(response => {
          this.$store.commit('updateContent', response.data);
          this.charactersData = response.data;
        })
        .catch(error => {
          console.error(error);
        });
    },
  }
};
</script>

<style scoped>
@import '../static/characterList.css';
</style>