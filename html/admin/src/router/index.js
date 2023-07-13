import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)


const routes = [
    {
        path: '/login',
        component: () => import('@/views/Login')
    },
    {
        path: '/',
        component: () => import('@/views/Layout'),
        children: [
            {
                path: '/',
                component: () => import('@/views/Home'),
            },
            {
                path: '/sc',
                component: () => import('@/views/SingleChoice'),
                children: [
                    {
                        path: 'published',  // 也可以写成 /sc/published
                        component: () => import('@/views/SingleChoice/PublishedList'),
                    },
                    {
                        path: 'unpublished',
                        component: () => import('@/views/SingleChoice/UnPublishedList')
                    },
                ]
            },
            {
                path: '/level',
                component: () => import('@/views/Level'),
            },
            {
                path: '/category',
                component: () => import('@/views/Category'),
            },
        ]
    }

]


const router = new VueRouter({
    mode: 'history',
    routes
})

export default router
