<template>
    <button @click="handleClick">Classify all uploaded images</button>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    methods: {
      async handleClick() {
        try {
          const response = await axios.get('http://127.0.0.1:5000/classify');
          console.log(response.data);
        } catch (error) {
          console.error(error);
        }
      }
    }
  }
  </script>
  