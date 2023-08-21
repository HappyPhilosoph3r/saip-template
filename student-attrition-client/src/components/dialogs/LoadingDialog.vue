<script setup lang="ts">
import { computed } from "vue";
const props = defineProps({
  modelValue: Boolean,
  title: String,
})
const emit = defineEmits(['update:modelValue'])
const isLoading = computed({
  get: () => props.modelValue,
  set: (value) => emit('update:modelValue', value)
})

const title_value = props.title ? props.title : "Loading";

</script>
<template>
  <v-dialog v-model="isLoading" width="500">
    <v-card color="primary">
      <h1>{{ title_value }}</h1>
      <v-row justify="center" class="mt-4 mb-4">
        <v-progress-circular indeterminate></v-progress-circular>
      </v-row>
    </v-card>
  </v-dialog>
</template>
<style scoped>
h1, h2 {
  text-align: center;
}
</style>