<template>
  <!-- The main container for the cart -->
  <div class="cart-container">
    
    <!-- 1. The Cart Icon (Using a simple SVG or font icon) -->
    <span class="cart-icon">🛒</span>
    
    <!-- 2. The Number Badge (Only shows if there is at least 1 item) -->
    <div v-if="cartCount > 0" class="badge">
      {{ cartCount }}
    </div>

  </div>

  <router-link to="/movieinput" class="cart-link">
    <!-- This is a simple link to the cart page -->
     <p>Continue Shopping</p>
  </router-link>

</template>

<script setup>
import { ref } from 'vue'

// This holds the number of items. In a real app, this might come from 
// a state manager like Pinia, Vuex, or a prop passed from a parent component.
const cartCount = ref(3) 

// A simple function to simulate clicking the cart
const goToCart = () => {
  console.log("Navigating to cart page...")
}
</script>

<style scoped>
/* Keeps the icon and badge together */
.cart-container {
  position: relative;
  display: inline-block;
  cursor: pointer;
  padding: 10px;
}

/* Make the icon a nice size */
.cart-icon {
  font-size: 2rem;
}

.cart-link {
  text-decoration: none;
  color: #0033ff;
  font-weight: bold;
  margin-top: 10px;
  display: inline-block;
}

/* Style the badge and position it in the top-right corner */
.badge {
  position: absolute;
  top: 0;
  right: 0;
  background-color: #ff3838; /* Bright red color to grab attention */
  color: white;
  border-radius: 50%; /* Makes the badge a perfect circle */
  padding: 2px 6px;
  font-size: 0.8rem;
  font-weight: bold;
  min-width: 18px;
  text-align: center;
}
</style>