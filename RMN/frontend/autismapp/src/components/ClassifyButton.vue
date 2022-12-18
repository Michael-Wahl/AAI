<template>
    <button @click="handleClick">Classify all uploaded images</button>
    <p>{{ data }}</p>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
    return {
      data: null
    }
  },
    methods: {
      async handleClick() {
        try {
          const response = await axios.get('http://127.0.0.1:5000/classify');
          this.data = response.data
          console.log(response.data);
        } catch (error) {
          console.error(error);
        }
      }
    }
  }
  </script>
  