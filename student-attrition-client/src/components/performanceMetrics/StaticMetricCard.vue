<script setup lang="ts">

import {ref} from "vue";
import {useMetricStore} from "@/stores/metricStore";
import {useMetricOptionsStore} from "@/stores/MetricOptionsStore";

const title = ref("Background Metrics")
const { data } = useMetricStore()
const metric = useMetricStore()
const metricOptions = useMetricOptionsStore()

</script>
<template>
  <v-card>
    <h1>{{ title }}</h1>
    <p>Academic Metrics Completed: {{ metric.backgroundMetricsComplete.toFixed(2) }}%</p>
    <v-autocomplete v-model="data.course"
                    class="ml-2 mr-2"
                    label="course"
                    :items="metricOptions.course"
    >
    </v-autocomplete>
    <v-autocomplete v-model="data.attendance_type"
                    class="ml-2 mr-2"
                    label="Attendance Type"
                    :items="metricOptions.attendance_type"
    >
    </v-autocomplete>
    <v-autocomplete v-model="data.nationality"
                    class="ml-2 mr-2"
                    label="Nationality"
                    :items="metricOptions.nationality"
    >
    </v-autocomplete>
    <v-autocomplete v-model="data.gender"
                    class="ml-2 mr-2"
                    label="Gender"
                    :items="metricOptions.gender"
    >
    </v-autocomplete>
    <v-text-field v-model="data.age_at_enrolment"
                  class="ml-2 mr-2"
                  label="Age at Enrollment"
                  type="number"
    >
    </v-text-field>
  </v-card>
</template>
<style scoped>
h1,p {
  text-align: center;
}
</style>