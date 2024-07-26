<template>
  <footer class="bg-gray-800 text-white p-6 mt-8 relative w-full">
    <div class="container mx-auto text-center">
      <p>&copy; 2024 PropertyMap Explorer. All rights reserved.</p>
      <div class="absolute bottom-0 left-0 w-full h-1 bg-gradient-to-r from-blue-500 to-purple-600 animate-gradient-x"></div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer',
}
</script>

<style scoped>
@keyframes gradient-x {
  0% {
    background-position: 0% 50%;
  }
  100% {
    background-position: 100% 50%;
  }
}

.animate-gradient-x {
  background-size: 200% 200%;
  animation: gradient-x 3s linear infinite;
}
</style>
