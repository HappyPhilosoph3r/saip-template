<script setup lang="ts">
import { RouterView } from 'vue-router'
import NavigationMenu from "@/components/navigation/NavigationMenu.vue";
import {useErrorStore} from "@/stores/errorStore";
import ErrorDialog from "@/components/dialogs/ErrorDialog.vue";
const error = useErrorStore()
</script>

<template>
  <div>
    <error-dialog v-model="error.errorOccurred" />
    <v-app>
      <navigation-menu />
      <br><br><br>
      <main>
        <RouterView />
      </main>
    </v-app>
  </div>
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}


nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
