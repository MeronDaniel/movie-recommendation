<template>
  <div class="search-wrapper">
    <div class="search-card">
      <h1>Movie Recommendation</h1>

      <form @submit.prevent="handleLogin">
        <label>Movie: </label>
        <input type="text" v-model="movie" placeholder="Enter movie here" required />
  
        <button type="submit">Search</button>
      </form>
    </div>
  </div>
</template>


  
<script>
export default {
  name: 'Login',
  data() {
    return {
      email: '',
      password: ''
    }
  },
  methods: {
    async handleLogin() {
      try {
        const response = await fetch('http://192.168.2.19:5000/api/auth/movieinput', {
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


<style scoped>


</style>
