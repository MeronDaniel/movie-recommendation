<script>
export default {
  name: 'Display',
  data() {
    return {
      searchResults: []
    }
  },
  mounted() {
    // Retrieve search results from localStorage
    const results = localStorage.getItem('searchResults')
    if (results) {
      this.searchResults = JSON.parse(results)
    }
  }
}
</script>
