<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/admin">Admin</router-link>
  </nav>
  <router-view/>
</template>


<script>
export default {
  
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
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


nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
