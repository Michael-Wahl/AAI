<template>
    <div class="home">
      <h1>Game Menu</h1>
      <p>Select a game mode:</p>
      <ul>
        <button v-on:click="currentComponent = 'GameImage'"> Play Emotion Guessing </button>
        <button v-on:click="currentComponent = 'GameBackground'">Play Background Game</button>
        <component :is="currentComponent"></component>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        currentComponent: 'GameMenu',
        isAdmin: false,
      }
    },
    methods: {
      selectGameMode(mode) {
        if (mode === 'admin') {
          if (!this.isAdmin) {
            return;
          }
        }
        // Code for starting the selected game mode

      }
    }
  }
  </script>

  