import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Account from '../views/Account.vue'
import Income from '../views/Income.vue'
import Expense from '../views/Expense.vue'
import Budget from '../views/Budget.vue'
import Main from '../views/Main'

Vue.use(VueRouter)

const routes = [
  // {
  //   path: '/',
  //   name: 'Home',
  //   component: Home
  // },
  // {
  //   path: '/about',
  //   name: 'About',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // },
  {
    path:"/",
    name:"Main",
    component:Main
  },
    {
    path:"/account",
    name:"Account",
    component:Account
  },
    {
    path:"/income",
    name:"Income",
    component:Income
  },
    {
    path:"/expense",
    name:"Expense",
    component:Expense
  },
    {
    path:"/budget",
    name:"Budget",
    component:Budget
  }
]

const router = new VueRouter({
  routes
})

export default router
