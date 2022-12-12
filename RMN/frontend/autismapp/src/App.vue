<!-- using and arranging our components-->
<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <br>
  <GameImage/>
  <HelloWorld msg="Welcome to Your Vue.js App"/>
</template>

<script>
// importing our components
import HelloWorld from './components/HelloWorld.vue'
import GameImage from './components/GameImage.vue';


export default {
  name: 'App',
  components: {
    HelloWorld,
    GameImage
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
