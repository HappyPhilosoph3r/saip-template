<script setup lang="ts">
import OverwhelmedCard from "@/components/InfoCards/OverwhelmedCard.vue";
import FinancesCard from "@/components/InfoCards/FinancesCard.vue";
import AcademicCard from "@/components/InfoCards/AcademicCard.vue";
import MentalHealthCard from "@/components/InfoCards/MentalHealthCard.vue";
import PhysicalHealthCard from "@/components/InfoCards/PhysicalHealthCard.vue";
import AccommodationCard from "@/components/InfoCards/AccommodationCard.vue";
import SocialCard from "@/components/InfoCards/SocialCard.vue";
import { useDisplay } from "vuetify";
import {computed} from "vue";
import GlossaryCard from "@/components/InfoCards/GlossaryCard.vue";
import UniversityStrugglesCard from "@/components/InfoCards/UniversityStrugglesCard.vue";

let display = useDisplay()

let columnWidth = computed(() => {
  return display.smAndDown.value ? 12 : 4
})

</script>

<template>
  <v-row v-if="columnWidth > 4" justify="space-between">
    <v-col :cols="columnWidth" class="d-flex justify-center">
      <university-struggles-card />
    </v-col>
    <v-col :cols="columnWidth" class="d-flex justify-center">
      <overwhelmed-card />
    </v-col>
    <v-col :cols="columnWidth" class="d-flex justify-center">
      <glossary-card />
    </v-col>
  </v-row>
  <v-row justify="space-between">
    <v-col :cols="columnWidth" class="d-flex justify-center">
      <academic-card />
    </v-col>
    <v-col :cols="columnWidth" class="d-flex justify-center">
      <social-card />
    </v-col>
    <v-col :cols="columnWidth" class="d-flex justify-center">
      <mental-health-card />
    </v-col>
  </v-row>
  <v-row v-if="columnWidth <= 4" justify="space-around">
    <university-struggles-card />
    <overwhelmed-card />
    <glossary-card />
  </v-row>
  <v-row justify="space-between">
    <v-col :cols="columnWidth" class="d-flex justify-center">
      <finances-card />
    </v-col>
    <v-col :cols="columnWidth" class="d-flex justify-center">
      <physical-health-card />
    </v-col>
    <v-col :cols="columnWidth" class="d-flex justify-center">
      <accommodation-card />
    </v-col>
  </v-row>
</template>
<style scoped>
  h1, p {
    text-align: center;
  }
</style>