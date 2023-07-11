<script setup lang="ts">

import {ref} from "vue";
import {useMetricStore} from "@/stores/metricStore";
import {useMetricOptionsStore} from "@/stores/MetricOptionsStore";

const title = ref("Support Network Metrics")
const { data } = useMetricStore()
const metric = useMetricStore()
const metricOptions = useMetricOptionsStore()
</script>
<template>
  <v-card>
    <h1>{{ title }}</h1>
    <p>Support Network Metrics Completed: {{ metric.supportNetworkMetricsComplete.toFixed(2) }}%</p>
    <v-autocomplete v-model="data.marital_status"
                    class="ml-2 mr-2"
                    label="Marital Status"
                    :items="metricOptions.marital_status"
    >
    </v-autocomplete>
    <v-autocomplete v-model="data.mothers_qualification"
                    class="ml-2 mr-2"
                    label="Mother's Qualification"
                    :items="metricOptions.parental_qualification"
    >
    </v-autocomplete>
    <v-autocomplete v-model="data.fathers_qualification"
                    class="ml-2 mr-2"
                    label="Father's Qualification"
                    :items="metricOptions.parental_qualification"
    >
    </v-autocomplete>
    <v-autocomplete v-model="data.mothers_occupation"
                    class="ml-2 mr-2"
                    label="Mother's Occupation"
                    :items="metricOptions.parental_occupation"
    >
    </v-autocomplete>
    <v-autocomplete v-model="data.fathers_occupation"
                    class="ml-2 mr-2"
                    label="Father's Occupation"
                    :items="metricOptions.parental_occupation"
    >
    </v-autocomplete>
    <v-autocomplete v-model="data.displaced"
                    class="ml-2 mr-2"
                    label="Displaced"
                    :items="metricOptions.binary"
    >
    </v-autocomplete>
    <v-autocomplete v-model="data.educational_special_needs"
                    class="ml-2 mr-2"
                    label="Educational Special Needs"
                    :items="metricOptions.binary"
    >
    </v-autocomplete>
    <v-autocomplete v-model="data.international"
                    class="ml-2 mr-2"
                    label="International"
                    :items="metricOptions.binary"
    >
    </v-autocomplete>
  </v-card>
</template>
<style scoped>
h1,p {
  text-align: center;
}
</style>