<script setup lang="ts">

import {ref} from "vue";
import {useMetricStore} from "@/stores/metricStore";
import {useMetricOptionsStore} from "@/stores/MetricOptionsStore";

const title = ref("Finance Metrics")
const { data } = useMetricStore()
const metric = useMetricStore()
const metricOptions = useMetricOptionsStore()
</script>
<template>
  <v-card>
    <h1>{{ title }}</h1>
    <p>Finance Metrics Completed: {{ metric.financeMetricsComplete.toFixed(2) }}%</p>
    <v-autocomplete v-model="data.debtor"
                    class="ml-2 mr-2"
                    label="Debtor"
                    :items="metricOptions.binary"
    >
    </v-autocomplete>
    <v-autocomplete v-model="data.tuition_fees_up_to_date"
                    class="ml-2 mr-2"
                    label="tuition_fees_up_to_date"
                    :items="metricOptions.binary"
    >
    </v-autocomplete>
    <v-autocomplete v-model="data.scholarship_holder"
                    class="ml-2 mr-2"
                    label="Scholarship Holder"
                    :items="metricOptions.binary"
    >
    </v-autocomplete>
    <v-text-field v-model="data.unemployment_rate"
                  class="ml-2 mr-2"
                  label="Unemployment Rate"
                  type="number"
    >
    </v-text-field>
    <v-text-field v-model="data.inflation_rate"
                  class="ml-2 mr-2"
                  label="Inflation Rate"
                  type="number"
    >
    </v-text-field>
    <v-text-field v-model="data.gdp"
                  class="ml-2 mr-2"
                  label="GDP"
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