<script setup lang="ts">
import { useRouter } from "vue-router";

const router = useRouter()
function goToOverwhelmed() {
  return router.push({name: 'overwhelmed'})
}
</script>
<template>
  <v-card width="300" flat>
    <h1>If you are feeling</h1>
    <h1>overwhelmed</h1>
    <h1>or</h1>
    <h1>overloaded</h1>
    <v-card-actions class="justify-center">
      <v-btn @click.prevent="goToOverwhelmed">click here</v-btn>
    </v-card-actions>
  </v-card>
</template>
<style scoped>
h1 {
  text-align: center;
}
</style>