<!-- using and arranging our components-->
<template>
    <div>
        <button v-on:click="currentComponent = 'GameImage'"> Play Emotion Guessing </button>
        <button v-on:click="currentComponent = 'GameBackground'">Play Background Game</button>
        <button v-on:click="currentComponent = 'AdminWindow'">Go to Admin Window</button>
        <component :is="currentComponent"></component>
    </div>
    <!-- <img alt="Vue logo" src="./assets/logo.png">-->
    <br>
    <WebcamUploader />
    <BackgroundCarousel />
    <HelloWorld />
    <AdminWindow />

    <!--
    <GameImage/>
    <GameBackground/>
    -->

</template>

<script>


// importing our components
//import HelloWorld from './components/HelloWorld.vue'
import GameImage from './components/GameImage.vue'
import AdminWindow from './components/AdminWindow.vue';
import GameBackground from './components/GameBackground.vue';
import WebcamUploader from './components/WebcamUploader.vue'
import BackgroundCarousel from './components/BackgroundCarousel.vue';


export default {
 
  
  name: 'App',
  data() {
    return {
      currentComponent: 'component-a',
    }
  },
        components: {
            
AdminWindow,
    GameImage,
    GameBackground,
    WebcamUploader,
    BackgroundCarousel

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
