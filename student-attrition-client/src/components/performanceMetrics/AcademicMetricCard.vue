<script setup lang="ts">

  import { ref } from "vue";
  import { useMetricStore } from "@/stores/metricStore";
  import { useMetricOptionsStore } from "@/stores/MetricOptionsStore";

  const title = ref("Academic Metrics")
  const { data } = useMetricStore()
  const metric = useMetricStore()
  const metricOptions = useMetricOptionsStore()

  const rules = {
    required: (value:any) => !!value || 'Field is required',
    restricted: (value:number) => !!value && 20 > value && value > 0 || 'number must be between 0 and 20',
  }

</script>
<template>
  <v-card>
    <h1>{{ title }}</h1>
    <p>Academic Metrics Completed: {{ metric.academicMetricsComplete.toFixed(2) }}%</p>
    <v-autocomplete v-model="data.application_mode"
                    class="ml-2 mr-2"
                    label="application_mode"
                    :items="metricOptions.application_mode"
    >
    </v-autocomplete>
    <v-text-field v-model="data.application_order"
                  class="ml-2 mr-2"
                  label="application_order"
                  type="number"
    >
    </v-text-field>
    <v-autocomplete v-model="data.previous_qualification"
                    class="ml-2 mr-2"
                    label="Previous qualification"
                    :items="metricOptions.previous_qualification"
    >
    </v-autocomplete>
    <v-text-field v-model="data.curricular_units_1st_semester_credited"
                  class="ml-2 mr-2"
                  label="curricular_units_1st_semester_credited"
                  type="number"
                  :rules="[rules.required, rules.restricted]"
    >
    </v-text-field>
    <v-text-field v-model="data.curricular_units_1st_semester_enrolled"
                  class="ml-2 mr-2"
                  label="curricular_units_1st_semester_enrolled"
                  type="number"
    >
    </v-text-field>
    <v-text-field v-model="data.curricular_units_1st_semester_evaluations"
                  class="ml-2 mr-2"
                  label="curricular_units_1st_semester_evaluations"
                  type="number"
    >
    </v-text-field>
    <v-text-field v-model="data.curricular_units_1st_semester_approved"
                  class="ml-2 mr-2"
                  label="curricular_units_1st_semester_approved"
                  type="number"
    >
    </v-text-field>
    <v-text-field v-model="data.curricular_units_1st_semester_grade"
                  class="ml-2 mr-2"
                  label="curricular_units_1st_semester_grade"
                  type="number"
    >
    </v-text-field>
    <v-text-field v-model="data.curricular_units_1st_semester_without_evaluations"
                  class="ml-2 mr-2"
                  label="curricular_units_1st_semester_without_evaluations"
                  type="number"
    >
    </v-text-field>
    <v-text-field v-model="data.curricular_units_2nd_semester_credited"
                  class="ml-2 mr-2"
                  label="curricular_units_2nd_semester_credited"
                  type="number"
    >
    </v-text-field>
    <v-text-field v-model="data.curricular_units_2nd_semester_enrolled"
                  class="ml-2 mr-2"
                  label="curricular_units_2nd_semester_enrolled"
                  type="number"
    >
    </v-text-field>
    <v-text-field v-model="data.curricular_units_2nd_semester_evaluations"
                  class="ml-2 mr-2"
                  label="curricular_units_2nd_semester_evaluations"
                  type="number"
    >
    </v-text-field>
    <v-text-field v-model="data.curricular_units_2nd_semester_approved"
                  class="ml-2 mr-2"
                  label="curricular_units_2nd_semester_approved"
                  type="number"
    >
    </v-text-field>
    <v-text-field v-model="data.curricular_units_2nd_semester_grade"
                  class="ml-2 mr-2"
                  label="curricular_units_2nd_semester_grade"
                  type="number"
    >
    </v-text-field>
    <v-text-field v-model="data.curricular_units_2nd_semester_without_evaluations"
                  class="ml-2 mr-2"
                  label="curricular_units_2nd_semester_without_evaluations"
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