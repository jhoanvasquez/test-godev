<template>
  <div class="character-list">
    <div v-for="character in characters" :key="character.id" class="character-card">
      <img :src="character.image" :alt="character.name" class="character-image" />
      <h2>{{ character.name }}</h2>
      <p>Status: {{ character.status }}</p>
      <p>Species: {{ character.species }}</p>
      <p>Gender: {{ character.gender }}</p>
      <p>Origin: {{ character.origin.name }}</p>
      <p>Location: {{ character.location.name }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CharacterList',
  props: {
    characters: {
      type: Array,
      required: true
    }
  }
};
</script>

<style scoped>
@import '../static/characterList.css';
</style>