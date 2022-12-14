<template>
    <div>
      <h1>Game Menu</h1>
      <p>Select a game mode:</p>
      <ul>
        <li v-on:click="selectGameMode('emotion mode')">Emotion Mode</li>
        <li v-on:click="selectGameMode('background mode')">Background Mode</li>
        <li v-on:click="selectGameMode('admin')" v-if="isAdmin">Admin Mode</li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
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
  