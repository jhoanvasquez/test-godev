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
import { ref, onMounted } from 'vue';
import axios from 'axios';
import CharacterList from '~/components/CharacterList.vue';

export default {
  name: 'DefaultLayout',
  components: {
    CharacterList
  },
  setup() {    
    const charactersData = ref({
      info: {},
      results: []
    });

    const fetchData = async () => {
      try {
        const response = await axios.get(process.env.POKEAPI_URL);
        charactersData.value = response.data;
        counter.value++;
      } catch (error) {
        console.error(error);
      }
    };

    onMounted(() => {
      fetchData();
    });

    return {
      counter,
      charactersData
    };
  }
};
</script>

<style scoped>
@import '../static/characterList.css';
</style>