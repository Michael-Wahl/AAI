<template>
    <form @submit.prevent="handleSubmit">
      <input v-model="imageFileName" />
      <button type="submit">Send</button>
      <p>{{ data }}</p>
    </form>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        imageFileName: '',
        data: null
      }
    },
    methods: {
      async handleSubmit() {
        try {
          const response = await axios.post('http://127.0.0.1:5000/getEmotion', 
          { string: this.imageFileName }, 
          { headers: { 'Access-Control-Allow-Origin': '*'}});

          this.data = response.data
          console.log(response.data);

        } catch (error) {
          console.error(error);
        }
      }
    }
  }
  </script>
  