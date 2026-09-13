<template>
  <div class="login-wrapper">
    <div class="login-card">
      <h1>Login</h1>

      <form @submit.prevent="handleLogin">
        <label>Email: </label>
        <input type="email" v-model="email" required />
  
        <label>Password: </label>
        <input type="password" v-model="password" required />
  
        <button type="submit">Log In</button>
      </form>
  
      <!-- ✅ Sign Up Prompt -->
      <p class="signup-link">
        New user?
        <router-link to="/register">Sign up</router-link>
      </p>
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
        const response = await fetch('http://192.168.2.19:5000/api/auth/login', {
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
        this.$router.push('/movieinput') // once user pushes login they get sent to movieinput page
      } catch (err) {
        alert(err.message)
        console.error('Login error:', err)
      }
    }
  }
}
</script>


<style scoped>
.login-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #920909;
}

.login-card {
  background-color: #fff;
  padding: 2rem;
  align-items: center;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(112, 101, 101, 0.1);
  width: 250px;
}


input[type="email"], input[type="password"] {
  margin-bottom: 1rem;
}

</style>
