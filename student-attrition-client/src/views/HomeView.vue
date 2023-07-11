<script setup lang="ts">
import OverwhelmedCard from "@/components/InfoCards/OverwhelmedCard.vue";
import FinancesCard from "@/components/InfoCards/FinancesCard.vue";
import AcademicCard from "@/components/InfoCards/AcademicCard.vue";
import MentalHealthCard from "@/components/InfoCards/MentalHealthCard.vue";
import PhysicalHealthCard from "@/components/InfoCards/PhysicalHealthCard.vue";
import AccommodationCard from "@/components/InfoCards/AccommodationCard.vue";
import SocialCard from "@/components/InfoCards/SocialCard.vue";
</script>

<template>
  <div>
    <v-row justify="space-between">
      <v-col cols="4" class="d-flex justify-center">
        <academic-card />
      </v-col>
      <v-col cols="4" class="d-flex justify-center">
        <social-card />
      </v-col>
      <v-col cols="4" class="d-flex justify-center">
        <mental-health-card />
      </v-col>
    </v-row>
    <v-row justify="space-around">
      <v-card width=300 flat>
        <h1>University Struggles</h1>
        <p>
          If you think university is hard, you are not alone! However whilst your situation is unique to you, there are
          some common themes that can affect a lot of students. This site investigates these themes in the hope that you
          may find something useful and possibly help to make your journey easier!
        </p>
      </v-card>
      <overwhelmed-card />
      <v-card width=300 flat :to="{name: 'glossary'}">
        <h1>Words are just letters in a sequence.</h1>
        <p>
          Acronyms, Abbreviations and the misappropriation of words can be the biggest barrier to learning. So we have
          provided a glossary to help give the 411 to awc!
        </p>
        <v-card-actions class="justify-center">
          <v-btn>click here</v-btn>
        </v-card-actions>
      </v-card>
    </v-row>
    <v-row justify="space-between">
      <v-col cols="4" class="d-flex justify-center">
        <finances-card />
      </v-col>
      <v-col cols="4" class="d-flex justify-center">
        <physical-health-card />
      </v-col>
      <v-col cols="4" class="d-flex justify-center">
        <accommodation-card />
      </v-col>
    </v-row>
  </div>
</template>
<style scoped>
  h1, p {
    text-align: center;
  }
</style>