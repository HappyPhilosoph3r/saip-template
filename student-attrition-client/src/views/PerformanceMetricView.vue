<script setup lang="ts">
  import { ref, computed, onMounted } from "vue";
  import AcademicMetricCard from "@/components/performanceMetrics/AcademicMetricCard.vue";
  import { useMetricStore } from "@/stores/metricStore";
  import StaticMetricCard from "@/components/performanceMetrics/StaticMetricCard.vue";
  import SupportNetworkMetricCard from "@/components/performanceMetrics/SupportNetworkMetricCard.vue";
  import FinanceMetricCard from "@/components/performanceMetrics/FinanceMetricCard.vue";
  import LoadingDialog from "@/components/dialogs/LoadingDialog.vue";
  import { useMetricOptionsStore } from "@/stores/MetricOptionsStore";
  import MetricResultsDialog from "@/components/dialogs/MetricResultsDialog.vue";


  let tab = ref("tab-1")
  let consent = ref(false)
  const metric = useMetricStore()
  const metricOptions = useMetricOptionsStore()


  const tabCount = computed(() => {
    return metric.percentageComplete == 100 ? "5" : "4"
  })

  function previousTab(){
    const tabSplit = tab.value.split("-")
    tab.value = tabSplit[1] == "1" ? "tab-1" :`tab-${parseInt(tabSplit[1]) - 1}`
    return
  }
  function nextTab(){
    const tabSplit = tab.value.split("-")
    tab.value = tabSplit[1] === tabCount.value ? `tab-${tabCount.value}` :`tab-${parseInt(tabSplit[1]) + 1}`
    return
  }
  function provideConsent(){
    consent.value = true
  }

  async function submitMetrics(){
    await metric.submitMetrics()
  }

  onMounted(() => {
    metricOptions.getMetricOptions()
  })

</script>
<template>
  <h1>Performance Metric</h1>
  <h2>
    This performance metric can provide insight into how you are coping with your course and the likelihood of you
    graduating given your current circumstances. It can also help to highlight areas that can be explored and
    improved to increase your chances.
  </h2>
  <h2>
    Please Note ...
  </h2>
  <h3>This is a machine learning project and the algorithms are not 100% accurate.</h3>
  <h3>
    If the prediction is not graduate, do not despair! There are plenty of resources that can help you to get back on
  track.
  </h3>
  <v-row v-if="!consent" justify="center" dense class="mt-2">
    <v-btn @click.prevent="provideConsent" color="primary">Begin performance analysis</v-btn>
  </v-row>
  <v-row v-if="consent" justify="center" dense class="mt-2">
    <v-card class="ml-2 mr-2">
      <v-tabs
          v-model="tab"
          bg-color="deep-purple-accent-4"
          centered
          stacked
      >
        <v-tab value="tab-1">
          <v-icon>mdi-account</v-icon>
          Background
        </v-tab>
        <v-tab value="tab-2">
          <v-icon>mdi-book</v-icon>
          Academic
        </v-tab>
        <v-tab value="tab-3">
          <v-icon>mdi-account-supervisor</v-icon>
          Support Network
        </v-tab>
        <v-tab value="tab-4">
          <v-icon>mdi-currency-gbp</v-icon>
          Finance
        </v-tab>
        <v-tab value="tab-5" v-if="metric.percentageComplete === 100">
          <v-icon>mdi-send</v-icon>
          Submit
        </v-tab>
      </v-tabs>
      <v-window v-model="tab">
        <v-window-item :value="'tab-1'"
        >
          <static-metric-card />
        </v-window-item>
        <v-window-item :value="'tab-2'"
        >
          <academic-metric-card />
        </v-window-item>
        <v-window-item :value="'tab-3'"
        >
          <support-network-metric-card />
        </v-window-item>
        <v-window-item :value="'tab-4'"
        >
          <finance-metric-card />
        </v-window-item>
        <v-window-item :value="'tab-5'"
        >
          <v-row justify="center">
            <v-btn @click.prevent="submitMetrics()"
                   class="mt-6 mb-6">
              Get Results
            </v-btn>
          </v-row>
        </v-window-item>
      </v-window>
      <v-row dense justify="center" align="center" class="mt-2 mb-2">
        <v-btn icon="mdi-chevron-left" @click.prevent="previousTab"  class="mr-2" flat :disabled="tab === 'tab-1'">
        </v-btn>
        <p>Total Completed: {{ metric.percentageComplete.toFixed(2) }}%</p>
        <v-btn @click.prevent="nextTab"
               icon="mdi-chevron-right"
               class="ml-2"
               flat
               :disabled="tab === `tab-${tabCount}`">
        </v-btn>
      </v-row>
    </v-card>
  </v-row>
  <loading-dialog v-model="metric.analysingPerformance" title="Analysing Performance ..."/>
  <metric-results-dialog v-model="metric.resultsExist" />
</template>
<style scoped>
  h1, h2, h3 {
    text-align: center;
  }
  h3 {
    color: red;
  }
</style>