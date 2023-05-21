
import Vue from 'vue'
import VueRouter from 'vue-router'
Vue.use(VueRouter)
export default new VueRouter({
  routes: [
    {
      path: '/',
      name: 'Main',
      redirect: '/home'
    },

    {
      path: '/login',
      name: 'login',
      component: () => import('../views/login.vue')
    },

    {
      path: '/register',
      name: 'register',
      component: () => import('../views/register.vue')
    },

    {
      path: '/home',
      name: 'home',
      component: () => import('../views/home.vue')
    },

    {
      path: '/baike',
      name: 'baike',
      component: () => import('../views/baike.vue')
    },

    {
      path: '/chat',
      name: 'chat',
      component: () => import('../views/chat.vue')

    },

    {
      path: '/person',
      name: 'person',
      component: () => import('../views/person.vue')

    },

    {
      path: '/article2',
      name: 'article2',
      component: () => import('../views/article2.vue')

    },

    {
      path: '/article3',
      name: 'article3',
      component: () => import('../views/article3.vue')

    },

    {
      path: '/article',
      name: 'article',
      component: () => import('../views/article.vue')

    },

    {
      path: '/exerise',
      name: 'exerise',
      component: () => import('../views/exerise.vue')
    },

    {
      path: '/health',
      name: 'health',
      component: () => import('../views/health.vue')
    },

    {
      path: '/yingyang',
      name: 'yingyang',
      component: () => import('../views/yingyang.vue')
    },

    {
      path: '/tupu',
      name: 'tupu',
      component: () => import('../views/tupu.vue')
    },

    {
      path: '/life',
      name: 'life',
      component: () => import('../views/life.vue')
    }

  ]
})
