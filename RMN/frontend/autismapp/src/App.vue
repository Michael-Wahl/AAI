<!-- using and arranging our components-->
<template>
    <!--
        <main>
        <component @nextStep="changeStep" v-bind:is="selectedComponent"></component>
    </main>
    -->
    <img alt="Vue logo" src="./assets/baby1.jpg">
    <br>

    <GameImage /> 
    <HelloWorld msg="Welcome to Your Vue.js App" /> 



    <AdminWindow msg="Administration" />


</template>

<script>


// importing our components
    import HelloWorld from './components/HelloWorld.vue'
   import GameImage from './components/GameImage.vue'
    import AdminWindow from './components/AdminWindow.vue';


export default {
 
  
  name: 'App',
  components: {
     HelloWorld,
     GameImage,
     AdminWindow
        },
/*
 * data() {
            return {
                selectedComponent: "HelloWorld"
            }
        },
 */
   
   /*
    *  methods: {
            changeStep(step: string) {
                this.selectedComponent = step;
            }
        },
    */
  
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
