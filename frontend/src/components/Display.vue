<template>
  <div class="image-wrapper">
    <div class="image-card">
      <h1>{{ movie_title }}</h1>

      <img :src="poster_url" 
      @click="handleClick"
      alt="Movie Poster" />

      <div v-if="showPlot"> <!--Display the plot summary when the poster is clicked-->
        <h2>Plot Summary</h2>
        <p>{{ movie_plot }}</p>
      </div> 

    </div>
  </div>
</template>

<script>
export default {
  name: 'Display',
  data() {
    return {
      poster_url: '',
      movie_title: '',
      movie_plot: '',
      showPlot: false
    }
  },
  methods: {
    handleClick() {
      this.showPlot = !this.showPlot
      // Display the plot summary when the poster is clicked
    }
  },
  mounted() {
    const movie = localStorage.getItem("searchResults")

    if (movie) {
      const parsedMovie = JSON.parse(movie)
      
      console.log("poster_url:", this.poster_url)
      console.log("movie_title:", this.movie_title)
      
      this.poster_url = parsedMovie.movie.Poster
      this.movie_title = parsedMovie.movie.Title
      this.movie_plot = parsedMovie.movie.Plot

    } 
  }
}
</script>

<style>
.image-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}
  
.image-card {
  background-color: #4389ec;
  padding: 2rem;
  align-items: center;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(112, 101, 101, 0.1);
  color: #000;
  width: 350px;
}
</style>