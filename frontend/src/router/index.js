import { createRouter, createWebHistory } from "vue-router";
import Login from "../components/Login.vue";
import Register from "../components/Register.vue";
import MovieInput from "../components/MovieInput.vue";
import Display from "../components/Display.vue";
import Theatre from "../components/Theatre.vue";
import Posters from "../components/Posters.vue";
import Recommendation from "../components/Recommendation.vue";
import Cart from "../components/Cart.vue";

const routes = [
    { path: '/', redirect: '/login' },
    { path: "/login", name: "Login", component: Login },
    { path: "/register", name: "Register", component: Register },
    { path: "/movieinput", name: "MovieInput", component: MovieInput },
    { path: "/display", name: "Display", component: Display },
    { path: "/theatre", name: "Theatre", component: Theatre },
    { path: "/posters", name: "Posters", component: Posters },
    { path: "/recommendations", name: "Recommendation", component: Recommendation },
    { path: "/cart", name: "Cart", component: Cart }
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
