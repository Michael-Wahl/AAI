<template>
    <div>
      <h1>Welcome to Autmotion</h1>
      Making it easy to read emotions since 2022
    </div>
    <div class="game-menu">
      <h2>GAME MENU</h2>
      <nav>
      <router-link to="/BackgroundCarousel" custom v-slot="{ navigate }">
      <button @click="navigate" role="link">
        Background Game
      </button>
    </router-link>
    <b></b>
    <router-link to="/GameImage" custom v-slot="{ navigate }">
      <button @click="navigate" role="link">
        Emoguess
      </button>
    </router-link>
    </nav>
  </div>
</template>

<script>


export default {
 
}
</script>

