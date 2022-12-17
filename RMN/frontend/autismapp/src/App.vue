<!-- using and arranging our components-->
<template>
  <div>
    <button v-on:click="currentComponent = 'GameImage'"> Play Emotion Guessing </button>
    <button v-on:click="currentComponent = 'GameBackground'">Play Background Game</button>
    <component :is="currentComponent"></component>
  </div>
  <img alt="Vue logo" src="./assets/logo.png">
  <br>
  <WebcamUploader/>
  <ClassifyButton/>
  <EmoLookup/>
  <!--
  <GameImage/>
  <GameBackground/>
  -->
  
</template>

<script>
// importing our components
import GameImage from './components/GameImage.vue';
import GameBackground from './components/GameBackground.vue';
import WebcamUploader from './components/WebcamUploader.vue'
import EmoLookup from './components/EmoLookup.vue';
import ClassifyButton from './components/ClassifyButton.vue'


export default {
  name: 'App',
  data() {
    return {
      currentComponent: 'component-a',
    }
  },
  components: {
    GameImage,
    GameBackground,
    WebcamUploader,
    EmoLookup, 
    ClassifyButton

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
