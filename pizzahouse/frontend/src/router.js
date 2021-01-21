import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      component: () => import('@/views/dashboard/Index'),
      children: [
        // Dashboard
        {
          name: 'Prise de commandes',
          path: '',
          component: () => import('@/views/dashboard/Dashboard'),
        },
        // Pages
        {
          name: 'Catégories',
          path: 'pages/user',
          component: () => import('@/views/dashboard/pages/Categories'),
        },
        {
          name: 'Notifications',
          path: 'components/notifications',
          component: () => import('@/views/dashboard/component/Notifications'),
        },
        {
          name: 'Menus',
          path: 'components/Menus',
          component: () => import('@/views/dashboard/component/Menus'),
        },
        {
          name: 'Supplements',
          path: 'components/Supplements',
          component: () => import('@/views/dashboard/component/Supplements'),
        },
        // Maps
        {
          name: 'Profiles',
          path: 'maps/Profiles',
          component: () => import('@/views/dashboard/maps/Profiles'),
        },
        // Upgrade
        {
          name: 'Upgrade',
          path: 'upgrade',
          component: () => import('@/views/dashboard/Upgrade'),
        },
      ],
    },
  ],
})
