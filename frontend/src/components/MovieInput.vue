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
        const response = await fetch('http://192.168.2.19:5000/api/movieinput/search', {
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

        // Store movie search results and redirect
        localStorage.setItem('searchResults', JSON.stringify({movie: data.movie}))
        console.log("Movie Data:", data.movie)
        console.log("Poster URL:", data.movie.Poster)
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


<style>

.search-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.search-card {
  background-color: #fff;
  padding: 2rem;
  align-items: center;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(112, 101, 101, 0.1);
  width: 250px;
}

.movie-background { 
  background: url('../images/movie_collection.jpg');
  background-size: cover;
  background-position: center;
  min-height: 100vh;
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
