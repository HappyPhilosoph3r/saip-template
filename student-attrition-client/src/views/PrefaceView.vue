<script setup lang="ts">
  import { useRouter } from 'vue-router'
  const router = useRouter()
  function goHome () {
    return router.push({path: 'home'})
  }
</script>

<template>
    <div>
        <v-col>
          <h1>Welcome to the Student Active Intervention Platform Template</h1>
          <h2>This site accompanies the paper: <br> Exploring the use of machine learning in developing an active intervention
            platform to reduce university student attrition rates.</h2>
          <h3>Author: Thomas Rees</h3>
          <h3>Project Supervisor: Dr. Mahesha Samaratunga</h3>
          <h3>Institution: Queen Mary University of London</h3>

          <p>
            This project investigates the use of machine learning to help identify students that are encountering
            circumstances that may lead to them withdrawing from / dropping out of their university degree.
            The philosophy of this site stems from the belief that people can feel powerless when dealing with situations
            that appear overwhelming and inevitable. This site is designed to provide information that can re-empower
            individuals and help them in becoming an active participant in finding alternative solutions to dropping out.
          </p>
          <p>
            This project is part of an Masters project for the Data Science and Artificial Intelligence Conversion MSc at
            Queen Mary University of London, any issues or concerns regarding the project should be addressed to either the
            author or the project supervisor.
          </p>
          <p>This template is designed in a way in which it provides the fundamentals needed to make the model function
            but is completely customisable. Please see the LICENSE file in the github repository for details.
            This platform was developed with ethics by design principles. we ask that you respect these same principles
            when developing your site.
          </p>
          <p>However you use this template... Good luck and feel free to get in contact if you have any questions.</p>
          <v-row justify="center" class="mt-4">
            <v-btn @click.prevent="goHome">Continue to site...</v-btn>
          </v-row>
        </v-col>
    </div>
</template>
<style scoped>
  h1 {
      text-align: center;
      margin-bottom: 1em;
  }
  h2{
      margin-bottom: 0.5em;
  }
  h3 {
      margin-bottom: 0.35em;
      margin-left: 1em;

  }
  p {
      margin: 1em;
  }
  li {
      margin-left: 3em;
  }
</style>
