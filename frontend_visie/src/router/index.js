import { createRouter, createWebHashHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'person',
    component: () => import(/* webpackChunkName: "login" */ '../views/PersonView.vue')
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
