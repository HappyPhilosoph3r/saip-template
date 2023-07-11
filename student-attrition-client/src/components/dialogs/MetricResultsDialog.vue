<script setup lang="ts">
import { computed } from "vue";
import { useMetricStore } from "@/stores/metricStore";
import {useRoute, useRouter} from "vue-router";

const props = defineProps({
  modelValue: Boolean,
})
const emit = defineEmits(['update:modelValue'])
const displayResults = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value)
})

const { results } = useMetricStore()
let resultStyle = results.label === "Graduate" ? "color: green;" : "color: red"

const router = useRouter()
const route = computed(() => {
  let name = useRoute().name
  if(name) {
    return name.toString()
  }
  return null
})
async function goToAdvice(route: string | null){
  const routeNames = {
    "academic": "academic",
    "finance": "finances",
    "supportNetwork": "social"
  }

  const optimumCategory = results.optimumCategory as keyof typeof routeNames;
  const name = routeNames[optimumCategory]

  if(!route || route === name){
    return
  }
  return router.push({name})
}


</script>
<template>
  <div>
    <v-dialog v-model="displayResults" width="500">
      <v-card>
        <h1>Performance Results</h1>
        <h2>The analysis predicts that given the current dataset the result will be:</h2>
        <h1 :style="resultStyle">{{ results.label }} </h1>
        <h2>With a probability of:</h2>
        <h2 :style="resultStyle">{{ results.score.toFixed(2) }}% </h2>
        <h2>The analysis also suggests that the area to focus on to improve your results the most is: </h2>
        <h1>{{ results.optimumCategory.toUpperCase() }} </h1>
        <v-card-actions class="justify-space-evenly">
          <p hidden>{{ route }}</p>
          <v-btn @click.prevent="displayResults = false" color="error">Cancel</v-btn>
          <v-btn @click.prevent="goToAdvice(route)" color="primary">
            Go To {{ results.optimumCategory.toUpperCase() }} Advice
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
<style scoped>
h1, h2 {
  text-align: center;
  margin-left: 0.5em;
  margin-right: 0.5em;
}
</style>