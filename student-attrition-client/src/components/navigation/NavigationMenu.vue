<script setup lang="ts">
import { useRoute, useRouter } from "vue-router";
import { computed, ref } from "vue";
import FeedbackForm from "@/components/feedback/FeedbackForm.vue";

const router = useRouter()
let drawer = ref(true)


function goTo(route: string | null, name: string){
  if(!route || route === name){
    return
  }
  return router.push({name})
}

const route = computed(() => {
  let name = useRoute().name
    if(name) {
      return name.toString()
    }
    return null
})

</script>
<template>
  <v-app-bar app v-if="route !== 'preface'" color="primary">
    <v-icon icon="mdi-menu" @click.prevent="drawer = !drawer" class="ml-4"></v-icon>
    <v-divider />
    <feedback-form />
  </v-app-bar>
  <v-navigation-drawer
      v-model="drawer"
      temporary
  >
    <v-list density="compact" nav>
      <v-list-item prepend-icon="mdi-view-dashboard" title="Home" @click.prevent="goTo(route,'home')">
      </v-list-item>
      <v-list-item prepend-icon="mdi-forum" title="About" @click.prevent="goTo(route,'about')">
      </v-list-item>
      <v-list-item prepend-icon="mdi-chart-line" title="Performance Metric"
                   @click.prevent="goTo(route,'performanceMetric')">
      </v-list-item>
      <v-list-item prepend-icon="mdi-lifebuoy" title="Feeling Overwhelmed?"
                   @click.prevent="goTo(route,'overwhelmed')">
      </v-list-item>
      <v-list-group value="Advice">
        <template v-slot:activator="{ props }">
          <v-list-item
              v-bind="props"
              prepend-icon="mdi-lifebuoy"
              title="Advice"
          ></v-list-item>
        </template>
        <v-list-item prepend-icon="mdi-school" title="Academic"
                     @click.prevent="goTo(route,'academic')">
        </v-list-item>
        <v-list-item prepend-icon="mdi-home-city" title="Accommodation"
                     @click.prevent="goTo(route,'accommodation')">
        </v-list-item>
        <v-list-item prepend-icon="mdi-currency-gbp" title="Financial"
                     @click.prevent="goTo(route,'finances')">
        </v-list-item>
        <v-list-item prepend-icon="mdi-head-plus" title="Mental Health"
                     @click.prevent="goTo(route,'mentalHealth')">
        </v-list-item>
        <v-list-item prepend-icon="mdi-medical-bag" title="Physical Health"
                     @click.prevent="goTo(route,'physicalHealth')">
        </v-list-item>
        <v-list-item prepend-icon="mdi-account-group" title="Support Network"
                     @click.prevent="goTo(route,'social')">
        </v-list-item>
      </v-list-group>
    </v-list>
  </v-navigation-drawer>
</template>
