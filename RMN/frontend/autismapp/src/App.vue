<!-- using and arranging our components-->
<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <br>
  <GameImage/>
  <GameBackground/>
</template>

<script>
// importing our components
import GameImage from './components/GameImage.vue';
import GameBackground from './components/GameBackground.vue';


export default {
  name: 'App',
  components: {
    GameImage,
    GameBackground
  }
}
</script>

<!-- optional style section for CSS -->
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
