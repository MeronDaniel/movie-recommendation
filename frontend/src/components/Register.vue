<template>
  <div class="login-wrapper">
    <div class="login-card">
      <h1>Register</h1>

      <form @submit.prevent="handleRegister">
        <label>Email</label>
        <input type="email" v-model="email" required />
  
        <label>Password</label>
        <input type="password" v-model="password" required />

        <label>Confirm Password</label>
        <input type="password" v-model="confirmPassword" required />

        <button type="submit">Register</button>
      </form>
  
      <!-- ✅ Sign Up Prompt -->
      <p class="signup-link">
        New user?
        <router-link to="/login">Sign up</router-link>
      </p>
    </div>
  </div>
</template>


  
<script>
export default {
  name: 'Register',
  data() {
    return {
      email: '',
      password: '',
      confirmPassword: ''
    }
  },
  methods: {
    async handleRegister() {
      try {
        const response = await fetch('http://localhost:3000/api/auth/register', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            email: this.email,
            password: this.password,
            confirmPassword: this.confirmPassword
          })
        })

        const data = await response.json()

        if (!response.ok) {
          throw new Error(data.message || 'Registration failed')
        }

        // Store login flag and redirect
        localStorage.setItem('token', data.token)
        localStorage.setItem('isLoggedIn', 'true')
        this.$router.push('/')
      } catch (err) {
        alert(err.message)
        console.error('Registration error:', err)
      }
    }
  }
}
</script>

  
