<script setup lang="ts">
import { computed } from "vue";
import { useErrorStore } from "@/stores/errorStore";

const error = useErrorStore()
const props = defineProps({
  modelValue: Boolean,
  title: String,
})
const emit = defineEmits(['update:modelValue'])
const displayError = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value)
})

</script>
<template>
  <v-dialog v-model="displayError" width="500">
    <v-card >
      <h1>{{ error.title }}</h1>
      <h3>{{ error.message }}</h3>
      <v-card-actions class="justify-center">
        <v-btn @click.prevent="error.clearError()">Continue</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<style scoped>
  h1 {
    color: red;
  }
  h1, h3{
    text-align: center;
  }

</style>