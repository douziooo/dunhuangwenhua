<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script setup>
</script>

<style>
#app {
  min-height: 100vh;
  font-family: 'Inter', 'PingFang SC', 'HarmonyOS Sans', sans-serif;
}

/* 确保body和html有基本样式 */
html, body {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
}
</style>

