<template>
  <div class="search-wrapper">
    <div class="search-card">
      <h1>Movie Recommendation</h1>

      <form @submit.prevent="handleSearch">
        <label>Movie: </label>
        <input type="text" v-model="movie" placeholder="Enter movie here" required /> <!-- use v-model instead of value since movie value will be updated dynamically -->
  
        <button type="submit">Search</button>
      </form>
    </div>
  </div>
</template>


  
<script>
export default {
  name: 'MovieInput',
  data() {
    return {
      movie: ''
    }
  },
  methods: {
    async handleSearch() {
      try {
        const response = await fetch('http://192.168.2.19:5000/api/auth/movieinput', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            movie: this.movie
          })
        })

        const data = await response.json()

        if (!response.ok) {
          throw new Error(data.message || 'Search failed')
        }

        // Store search results and redirect
        localStorage.setItem('searchResults', JSON.stringify(data))
        localStorage.setItem('isLoggedIn', 'true')
        this.$router.push('/display') //once search input is successful, redirect to display page to display movie recommended
      } catch (err) {
        alert(err.message)
        console.error('Search error:', err)
      }
    }
  }
}
</script>


<style scoped>


</style>
