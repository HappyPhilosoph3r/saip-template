<script setup lang="ts">
import { ref } from "vue";

let valid = ref()
let username = ref()
let password = ref()

function login(){
  return null
}

</script>
<template>
  <v-row justify="center">
    <v-card width="500">
      <h1>Login</h1>
      <v-form ref="loginForm" v-model="valid" @submit.prevent="login">
        <v-text-field v-model="username" label="Username"></v-text-field>
        <v-text-field v-model="password" label="Password" type="password"></v-text-field>
        <v-card-actions class="justify-center">
          <v-btn type="submit">Login</v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-row>
</template>