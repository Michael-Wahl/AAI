<template>
  <h1> Background matching </h1>

  <h3> Does the emotion fit the background? </h3>
    <div class="emotion-game">
      <div class="face-container">
        <img :src="faceImage" alt="face" />
      </div>
      <div class="background-container">
        <img :src="backgroundImage" alt="background" />
      </div>
      <button @click="checkAnswer">Right</button>
      <button @click="checkAnswer">Wrong</button>
      <p v-if="isAnswerCorrect">Correct!</p>
      <p v-else>Incorrect.</p>
    </div>
</template>
  
<script>
  export default {
    data() {
      return {
        faceImage: '',
        backgroundImage: 'https://reparadius.de/img/868/fahrradwerkstatt-radlmeister-979.jpg?h=&w=1123&mode=max&scale=down&autorotate=true',
        isAnswerCorrect: null,
      };
    },
    methods: {
      checkAnswer() {
        // Check if the emotion of the face matches the background,
        // and set the isAnswerCorrect flag accordingly.
      },
      
    },
  };
</script>
  
<style>
  .emotion-game {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .face-container,
  .background-container {
    width: 200px;
    height: 200px;
  }
  
  img {
    max-width: 100%;
    max-height: 100%;
  }
  
  button {
    margin-top: 20px;
  }
</style>
  