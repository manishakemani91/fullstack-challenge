<template>
<div class="flex items-center justify-center min-h-screen bg-gray-100">
    <div class="bg-white p-6 rounded-lg shadow-lg w-full max-w-md">
        <h2 class="text-2xl font-bold mb-4 text-center text-gray-900">Login</h2>
        <form @submit.prevent="login">
            <div class="mb-4">
                <label for="username" class="block text-gray-700">Username:</label>
                <input type="text" v-model="username" id="username" class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 text-gray-900" required />
            </div>
            <div class="mb-4">
                <label for="password" class="block text-gray-700">Password:</label>
                <input type="password" v-model="password" id="password" class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 text-gray-900" required />
            </div>
            <button type="submit" class="w-full bg-indigo-500 text-white py-2 px-4 rounded-md hover:bg-indigo-600">Login</button>
        </form>
    </div>
</div>
</template>

<script>
export default {
    data() {
        return {
            username: '',
            password: ''
        };
    },
    methods: {
        login() {
            if (this.username === 'admin' && this.password === 'admin') {
                localStorage.setItem('loggedIn', 'true');
                this.$router.push('/');
            } else {
                alert('Invalid credentials')
            }
        }
    }
}
</script>
