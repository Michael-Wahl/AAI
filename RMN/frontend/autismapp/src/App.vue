<!-- using and arranging our components-->
<template>
  <div>
    <button v-on:click="currentComponent = 'GameImage'"> Play Emotion Guessing </button>
    <button v-on:click="currentComponent = 'GameBackground'">Play Background Game</button>
    <component v-if="currentView === 'GameImage'" v-bind:is="home"></component>
    <component v-else-if="currentView === 'GameBackground'" v-bind:is="about"></component>
  </div>
 
 
</template>

<script>
// importing our components
import HomePage from './components/HomePage.vue';
import GameImage from './components/GameImage.vue'
import GameBackground from './components/GameBackground.vue';
import WebcamUploader from './components/WebcamUploader.vue'
import ClassifyButton from './components/ClassifyButton.vue'
import BackgroundCarousel from './components/BackgroundCarousel.vue';



export default {
    name: "App",
    components: { 
      HomePage,
      GameImage,
    GameBackground,
    WebcamUploader,
    ClassifyButton,
    BackgroundCarousel },
  data() {
    return {
      currentView: 'HomePage'
    }
  },
  methods: {
    changeView(view) {
      this.currentView = view
    }
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
}
body {
  /* Set the background to a linear gradient */
  background: linear-gradient(to bottom, #393939, #727272);
  
  /* Center and scale the background image */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
.logo-container {
  position: absolute;
  bottom: 0;
  left: 0;
  margin: 10px;
}

header {
  background-color: #336699;
  color: white;
  padding: 20px;
  text-align: center;
}

header h1 {
  margin: 0;
  font-size: 24px;
  font-weight: bold;
}
button {
  display: inline-block;
  margin: 10px;
  padding: 10px 20px;
  background-color: #336699;
  color: white;
  cursor: pointer;
  border-radius: 5px;
}
button:hover {
  background-color: #224488;
}
</style>
