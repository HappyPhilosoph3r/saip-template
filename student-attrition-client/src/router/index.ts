import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import PrefaceView from '../views/PrefaceView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'preface',
      component: PrefaceView
    },
    {
      path: '/home',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    //  topics
    {
      path: '/topic/academic',
      name: 'academic',
      component: () => import('../views/topics/AcademicView.vue')
    },
    {
      path: '/topic/accommodation',
      name: 'accommodation',
      component: () => import('../views/topics/AccommodationView.vue')
    },
    {
      path: '/topic/finances',
      name: 'finances',
      component: () => import('../views/topics/FinancesView.vue')
    },
    {
      path: '/topic/mental-health',
      name: 'mentalHealth',
      component: () => import('../views/topics/MentalHealthView.vue')
    },
    {
      path: '/topic/physical-health',
      name: 'physicalHealth',
      component: () => import('../views/topics/PhysicalHealth.vue')
    },
    {
      path: '/topic/social',
      name: 'social',
      component: () => import('../views/topics/SocialView.vue')
    },
    {
      path: '/glossary',
      name: 'glossary',
      component: () => import('../views/GlossaryView.vue')
    },
    {
      path: '/performance-metric',
      name: 'performanceMetric',
      component: () => import('../views/PerformanceMetricView.vue')
    },
    {
      path: '/overwhelmed',
      name: 'overwhelmed',
      component: () => import('../views/OverwhelmedView.vue')
    },
    // wildcard path - any unnamed route will redirect to home.
    {
      path:  "/:catchAll(.*)",
      redirect: '/home'
    }
  ]
})

export default router
