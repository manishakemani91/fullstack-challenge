<template>
  <header class="bg-gradient-to-r from-blue-500 to-purple-600 text-white p-6 shadow-lg w-full">
    <div class="container mx-auto flex justify-between items-center">
      <h1 class="text-3xl font-bold">PropertyMap Explorer</h1>
      <nav>
        <ul 
        class="flex space-x-4">
          <li> <button @click="logout">Logout</button></li>
        </ul>
      </nav>
    </div>
  </header>
</template>

<script>
export default {
  name: 'Header',
  methods: {
    logout() {
      // Clear local storage
      localStorage.clear();
     this.$router.push('/login');
    }
  }
}
</script>

<style scoped>
/* Scoped styles here if needed */
</style>

