import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../components/HomePage.vue'
import BackgroundCarousel from '../components/BackgroundCarousel.vue'
import AdminWindow from '../components/AdminWindow.vue'
import GameImage from '../components/GameImage.vue'
import WebcamUploader from '../components/WebcamUploader.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/BackgroundCarousel',
    name: 'BackgroundCarousel',
    component: BackgroundCarousel
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    //component: () => import('../components/BackgroundCarousel.vue')
  },
  {
    path: '/admin',
    name: 'admin',
    component: AdminWindow
  },
  {
    path: '/GameImage',
    name: 'gameimage',
    component: GameImage
  },
  {
    path: '/WebcamUploader',
    name: 'webcamuploader',
    component: WebcamUploader

  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
