<template>
    <div class="recommendation">
        <!-- <h2>Recommended for You</h2> -->

    </div>

    <div class="page-wrapper">

        <div class="input-wrapper">
            <div class="input-card">
            <!-- <h1>Movie Recommendation</h1> -->

            <form @submit.prevent="handleInput">

                <input type="text" v-model="recommends" placeholder="Ask me for a movie recommendation!" required /> <!-- use v-model instead of value since movie value will be updated dynamically -->

                <button type="submit">Search</button>
            </form>
            </div>
        </div>
    </div>


  

</template>

<script>
    export default {
        name: 'Recommendation',
        data() {
            return {
                recommends: ''
            }
        },
        methods: {
            async handleInput() {
                try {
                    const response = await fetch('http://localhost:5000/api/recommendations/ask', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({
                            recommends: this.recommends
                        })
                    });

                    const data = await response.json();

                    localStorage.setItem("Recommendation", JSON.stringify({
                        user: this.recommends,
                        ai: data.recommendation
                    }));
                    this.$router.push('/aichat_displays');
                }
                
                catch (err) {
                    alert(err.message);
                    console.error('Recommendation error:', err);
                }
            }
        }
    }
</script>


<style scoped>

.page-wrapper{
    display: flex;
    flex-direction: column;
    min-height: 95vh;   /* allows bottom placement */
}

.input-wrapper {
    display: flex;
    margin-top: auto;
    width: auto;
    justify-content: center;
    align-items: center;
    height: 18vh;
    background-color: #920909;
}

.input-card {
    background-color: #fff;
    padding: 2rem;
    align-items: center;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(112, 101, 101, 0.1);
    width: 600px;
}

input[type="text"] {
    width: 50%;
}

button[type="submit"] {
    margin-left: 10px;
}

</style>