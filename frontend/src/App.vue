<template>
  <div class="movie-background">
    <header class="top-bar">

      <nav class="nav-links">
        <router-link to="/theatre">Theatre</router-link>
        <router-link to="/posters">Posters</router-link>
        <router-link to="/recommendations">Recommendations</router-link>
      </nav>
      <nav class="nav-cart">
        <router-link to="/cart">
          <span class="cart-icon">🛒</span>
        </router-link>
        
      </nav>

    </header>
    <router-view />
  </div>
</template>

<script>

export default {
  name: 'App',
  data() {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    async handleLogin() {
      try {
        const response = await fetch('http://localhost:3000/api/auth/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            email: this.email,
            password: this.password
          })
        })

        const data = await response.json()

        if (!response.ok) {
          throw new Error(data.message || 'Login failed')
        }

        // Store login flag and redirect
        localStorage.setItem('token', data.token)
        localStorage.setItem('isLoggedIn', 'true')
        this.$router.push('/')
      } catch (err) {
        alert(err.message)
        console.error('Login error:', err)
      }
    }
  }


}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

.movie-background { 
  background: url('../src/images/movie_collection.jpg') no-repeat center center fixed;
  background-size: cover;
  background-position: center;
  min-height: 100vh;
}

.login-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
}

.top-bar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  flex-direction: row;
  display: flex;
  background-color: #333;
  color: white;
  padding: 1rem 2rem;
}

.nav-links a {
  position: left;
  color: white;
  margin-left: 1.5rem;
  text-decoration: none;
}

.nav-cart a {
  margin-left: 70rem;
  color: white;
  text-decoration: none;
  width: 100%;
}

.nav-links a:hover {
  text-decoration: underline;
}
</style>
