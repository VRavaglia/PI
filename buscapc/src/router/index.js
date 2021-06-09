import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Mobo from '../views/Mobo.vue'
import Cpu from '../views/Cpu.vue'
import Gpu from '../views/Gpu.vue'
import Case from '../views/Case.vue'
import Ram from '../views/Ram.vue'
import Fonte from '../views/Fonte.vue'
import Armazenamento from '../views/Armazenamento.vue'
import Lista from '../views/Lista.vue'
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  
  {
    path: '/mobo',
    name: 'Mobo',
    component: Mobo
  },

  {
    path: '/cpu',
    name: 'Cpu',
    component: Cpu
  },
  {
    path: '/gpu',
    name: 'Gpu',
    component: Gpu
  },
  {
    path: '/case',
    name: 'Case',
    component: Case
  },
  {
    path: '/ram',
    name: 'Ram',
    component: Ram
  },
  {
    path: '/fonte',
    name: 'Fonte',
    component: Fonte
  },
  {
    path: '/armazenamento',
    name: 'Armazenamento',
    component: Armazenamento
  },
  {
    path: '/lista',
    name: 'Lista',
    component: Lista
  }


]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
