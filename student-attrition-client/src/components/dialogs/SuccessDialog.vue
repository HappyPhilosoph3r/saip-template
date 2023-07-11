<script setup lang="ts">
import { computed } from "vue";
  const props = defineProps({
    modelValue: Boolean,
    title: String,
    message: String
  })
  const emit = defineEmits(['update:modelValue'])
  const success = computed({
    get: () => props.modelValue,
    set: (value) => emit('update:modelValue', value)
  })

  const title_value = props.title ? props.title : "Success";
  const message_value = props.message ? props.message: null

</script>
<template>
  <div>
    <v-dialog v-model="success" width="500">
      <v-card>
        <h1>{{ title_value }}</h1>
        <h2>{{ message_value }}</h2>
        <v-card-actions class="justify-center">
          <v-btn @click.prevent="success = false" color="primary">Continue</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>
<style scoped>
  h1, h2 {
    text-align: center;
  }
</style>