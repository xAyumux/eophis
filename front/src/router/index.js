//import { createRouter, createWebHashHistory } from 'vue-router'
import { createRouter,createWebHistory} from 'vue-router'
import Home from '../views/Home.vue'
import Select from '../views/Select.vue'
import key from '../views/Key.vue'
import Audio from '../components/Audio.vue'

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
    path: '/select',
    name: 'Selct',
    component: Select
  },
  {
    path: '/key',
    name: 'Key',
    component: key
  },
  {
    path: '/Audio',
    name: 'audio',
    component: Audio
  }
]

const router = createRouter({
  mode: "history",
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
