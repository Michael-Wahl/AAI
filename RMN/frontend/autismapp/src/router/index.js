import { createRouter, createWebHistory } from 'vue-router'

// importing our components
import HomePage from '../components/HomePage.vue';
import GameImage from '../components/GameImage.vue';
import GameBackground from '../components/GameBackground.vue';
//import GameMenu from './components/GameMenu.vue';
/*
import WebcamUploader from './components/WebcamUploader.vue'
import ClassifyButton from './components/ClassifyButton.vue'
import BackgroundCarousel from './components/BackgroundCarousel.vue';

import NavigationBar from './components/NavigationBar.vue'
*/


const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
  routes: [
    {
        path: '/',
        name: 'HomePage',
        component: HomePage,
      },
    {
      path: '/gameimage',
      name: 'gameimage',
      component: GameImage,
    },
    {
      path: '/GameBackground',
      name: 'GameBackground',
      component: GameBackground,
    },
  ]
})
export default router