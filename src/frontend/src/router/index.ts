import { createRouter, createWebHistory } from 'vue-router'
import LoginScreen from '../views/LoginScreen.vue'
import RegisterScreen from '../views/RegisterScreen.vue'
import ProjectListScreen from '../views/ProjectListScreen.vue'
import ProjectScreen from '../views/ProjectScreen.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
		{
			path: '/',
			name: 'login',
			component: LoginScreen,
		},
		{
			path: '/register',
			name: 'register',
			component: RegisterScreen,
		},
		{
			path: '/projects',
			name: 'projectlist',
			component: ProjectListScreen,
		},
		{
			path: '/projects/:id',
			name: 'project',
			component: ProjectScreen
		}

	],
});

export default router
