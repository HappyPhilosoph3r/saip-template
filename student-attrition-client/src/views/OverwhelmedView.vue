<script setup lang="ts">

import { useRouter } from "vue-router";

const router = useRouter()
function goToPerformanceMetric() {
  return router.push({name: 'performanceMetric'})
}

</script>
<template>
  <h2>First things first, it is completely okay to feel overwhelmed or overloaded!</h2>
  <h3>
    Sometimes having to many thoughts or two many things that need doing can cause a feeling of paralysis which
    results in not being able to achieve anything productive.
  </h3>
  <p>
    If this is the case then sometimes writing everything down can help. The first step is to write down a stream of
    consciousness, just write down everything going through your head, seeing everything written down can aid in
    clarifying what needs doing.
  </p>
  <p>
    The next step is then breaking each task down into manageable tasks. For example if the task is complete an
    assignment, this can be broken down into smaller tasks, such as "Read assignment brief",
    "write down initial thoughts" and "research topic" etc.
  </p>
  <p> Below is a text-box, feel free to use this to write down your stream of consciousness. It will not be saved
    anywhere and will be destroyed when you refresh the page, feel free to use a text-editor or programme of your
    choice instead.</p>
  <h3 style="color: red; margin-bottom: 1.5em">Do NOT use this if you want your work to be saved. </h3>
  <v-row justify="center">
    <v-card width="1000" flat>
      <v-textarea auto-grow></v-textarea>
    </v-card>
  </v-row>
  <p>
    If you want to improve your performance at university then this site is designed to provide easy to find guidance
    on various topics. If you know what areas you want to improve on then feel free to go straight there using
    the navigation menu.
  </p>
  <p>
    If you are not sure what you need to do to improve then this site also contains a performance analysis,
    where you enter your information and then the site will tell you the area that should help you improve the most.
  </p>
  <v-row justify="center" class="mb-2">
    <v-btn color="primary" @click.prevent="goToPerformanceMetric">Click here to analyse your performance</v-btn>
  </v-row>
</template>
<style scoped>
  h2, h3 {
    text-align: center;
  }
  p {
    margin: 1em;
  }
</style>