<template>
  <div class="image-wrapper">
    <div class="image-card">
      <h1>{{ movie_title }}</h1>
      <img :src="poster_url" alt="Movie Poster" />
      
    </div>
  </div>
</template>

<script>
export default {
  name: 'Display',
  data() {
    return {
      poster_url: '',
      movie_title: ''
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

    }
    
  }
}
</script>
