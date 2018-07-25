import Vue from 'vue'
import Router from 'vue-router'
import Header from '@/components/Header'
import Protected from '@/components/Protected'
import Questionnaire from '@/components/Questionnaire'
import Auth from '@/components/Auth'
import Accueil from '@/components/Accueil'


Vue.use(Router)

export const routes = [
      {
        path: '/Accueil',
        name: 'Accueil',
        component: Accueil
      },
      {
        path: '/Protected',
        name: 'Protected',
        component: Protected
      },
      {
        path: '/Questionnaire',
        name: 'Questionnaire',
        component: Questionnaire
      },
      {
        path: '/Auth',
        name: 'Auth',
        component: Auth
      }
]
