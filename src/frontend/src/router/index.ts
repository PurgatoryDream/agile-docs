import { createRouter, createWebHistory } from 'vue-router'
import LoginScreen from '../views/LoginScreen.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: LoginScreen,
    }
  ],
})

export default router
