<template>
  <div class="register-wrapper">
    <div class="register-card">
      <h1>Register</h1>

      <form @submit.prevent="handleRegister">

        <div class="form-row">
          <label>Email: </label>
          <input type="email" v-model="email" required />
        </div>
        
  
        <div class="form-row">
          <label>Password: </label>
          <input type="password" v-model="password" required />
        </div>
        

        <div class="form-row">
          <label>Confirm Password: </label>
          <input type="password" v-model="confirmPassword" required />
        </div>
        

        <button type="submit">Register</button>
      </form>
  
      <!-- ✅ Sign Up Prompt -->
      <p class="signup-link">
        New user?
        <router-link to="/login">Sign Up</router-link>
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
        const response = await fetch('http://192.168.2.19:5000/api/auth/register', {
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

        // Store register flag and redirect
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

<style scoped>

.register-wrapper {
  display: flex;
  padding: 10px 40px 10px 40px; /* top right bottom left */
  justify-content: center;
  align-items: center;
  height: 90vh;
  background-color: #920909;
}

.register-card {
  background-color: #fff;
  padding: 10px 40px 10px 40px; /* top right bottom left */
  align-items: center;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(112, 101, 101, 0.1);
  width: 350px;
}

input[type="email"], input[type="password"] { /* adds space between each input field and the button */
  margin-bottom: 1rem;
}

.form-row {
  margin-right: 1rem;
}

</style>

  
