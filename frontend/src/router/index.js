import { createRouter, createWebHistory } from "vue-router";
import Login from "../components/Login.vue";
import Register from "../components/Register.vue";
import MovieInput from "../components/MovieInput.vue";

const routes = [
    { path: '/', redirect: '/login' },
    { path: "/login", name: "Login", component: Login },
    { path: "/register", name: "Register", component: Register },
    { path: "/movieinput", name: "MovieInput", component: MovieInput },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
