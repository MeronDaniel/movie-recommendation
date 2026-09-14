<template>
    <div class="chat-wrapper">
        <div class="user-message">
            <h3>You asked: </h3>
            <p>{{ userInput }}</p>
        </div>

        <div class="ai-response">
            <h3>AI Response:</h3>
            <p>{{ aiResponse }}</p>
        </div>
    </div>
</template>

<script>
export default {

    name: 'AIChat_Displays',
    data() {
        return {
            userInput: '',
            aiResponse: ''
        }
    },
    mounted() {
        const stored = JSON.parse(localStorage.getItem("Recommendation"))

    if (stored) {
      this.userInput = stored.user
      this.aiResponse = stored.ai
    }
    },
}
</script>


<style scoped>
    .display-wrapper {
    max-width: 800px;
    margin: auto;
    padding: 2rem;
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    }

    .chat-wrapper {
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    .user-message {
    background-color: #ffe4e1;
    border-left: 6px solid #ff6b6b;
    }

    .ai-response {
    background-color: #e8f4ff;
    border-left: 6px solid #4a90e2;
    }
</style>