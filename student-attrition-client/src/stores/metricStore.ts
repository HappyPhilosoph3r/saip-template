import { defineStore } from "pinia";
import type { IMetricState } from "../../@types/metrics";
import axios from "axios";
import { useErrorStore } from "@/stores/errorStore";
import type { AxiosError } from "axios";

const academicMetrics = ["application_mode", "application_order", "previous_qualification",
  "curricular_units_1st_semester_credited", "curricular_units_1st_semester_enrolled",
  "curricular_units_1st_semester_evaluations", "curricular_units_1st_semester_approved",
  "curricular_units_1st_semester_credited", "curricular_units_1st_semester_grade",
  "curricular_units_1st_semester_without_evaluations", "curricular_units_2nd_semester_credited",
  "curricular_units_2nd_semester_enrolled", "curricular_units_2nd_semester_evaluations",
  "curricular_units_2nd_semester_approved", "curricular_units_2nd_semester_grade",
  "curricular_units_2nd_semester_without_evaluations"]

const supportNetworkMetrics = ["marital_status", "mothers_qualification", "fathers_qualification",
  "mothers_occupation", "fathers_occupation", "displaced", "educational_special_needs", "international"]

const financeMetrics = ["debtor", "tuition_fees_up_to_date", "scholarship_holder", "unemployment_rate",
  "inflation_rate", "gdp"]

const backgroundMetrics = ["course", "attendance_type", "nationality", "gender", "age_at_enrolment"]

const numericMetrics = ["application_order", "age_at_enrolment", "curricular_units_1st_semester_credited",
  "curricular_units_1st_semester_enrolled", "curricular_units_1st_semester_evaluations",
  "curricular_units_1st_semester_approved", "curricular_units_1st_semester_credited",
  "curricular_units_1st_semester_grade", "curricular_units_1st_semester_without_evaluations",
  "curricular_units_2nd_semester_credited", "curricular_units_2nd_semester_enrolled",
  "curricular_units_2nd_semester_evaluations", "curricular_units_2nd_semester_approved",
  "curricular_units_2nd_semester_grade", "curricular_units_2nd_semester_without_evaluations", "unemployment_rate",
  "inflation_rate", "gdp"]

export const useMetricStore = defineStore('metricStore', {
  state: (): IMetricState => ({
    data: {
      marital_status: null,
      application_mode: null,
      application_order: null,
      course: null,
      attendance_type: null,
      previous_qualification: null,
      nationality: null,
      mothers_qualification: null,
      fathers_qualification: null,
      mothers_occupation: null,
      fathers_occupation: null,
      displaced: null,
      educational_special_needs: null,
      debtor: null,
      tuition_fees_up_to_date: null,
      gender: null,
      scholarship_holder: null,
      age_at_enrolment: null,
      international: null,
      curricular_units_1st_semester_credited: null,
      curricular_units_1st_semester_enrolled: null,
      curricular_units_1st_semester_evaluations: null,
      curricular_units_1st_semester_approved: null,
      curricular_units_1st_semester_grade: null,
      curricular_units_1st_semester_without_evaluations: null,
      curricular_units_2nd_semester_credited: null,
      curricular_units_2nd_semester_enrolled: null,
      curricular_units_2nd_semester_evaluations: null,
      curricular_units_2nd_semester_approved: null,
      curricular_units_2nd_semester_grade: null,
      curricular_units_2nd_semester_without_evaluations: null,
      unemployment_rate: null,
      inflation_rate: null,
      gdp: null
    },
    analysingPerformance: false,
    resultsExist: false,
    results: {
      featureDict: {
        academic: 0,
        finance: 0,
        supportNetwork: 0
      },
      featureMain: "",
      featureStrength: 0,
      label: "",
      score: 0,
      optimumCategory: "",
      optimumCategoryValue: 0
    }

  }),
  getters: {
    metricKeyCount: (state) => Object.keys(state.data).length || 0,
    metricValueCount: (state) => (<any>Object).values(state.data).filter((value: any) => value !== null && value !== '').length || 0,
    percentageComplete(): number {
      return (100 / this.metricKeyCount) * this.metricValueCount
    },
    academicMetricsComplete(state): number {
      const relevant_entries = (<any>Object).entries(state.data).filter((key: any[]) => academicMetrics.includes(key[0]));
      const relevant_values = relevant_entries.filter((entry: any[]) => entry[1] !== null && entry[1] !== '' || entry[1] == 0).length
      return (100 / relevant_entries.length) * relevant_values
    },
    supportNetworkMetricsComplete(state): number {
      const relevant_entries = (<any>Object).entries(state.data).filter((key: any[]) => supportNetworkMetrics.includes(key[0]));
      const relevant_values = relevant_entries.filter((entry: any[]) => entry[1] !== null && entry[1] !== '').length
      return (100 / relevant_entries.length) * relevant_values
    },
    financeMetricsComplete(state): number {
      const relevant_entries = (<any>Object).entries(state.data).filter((key: any[]) => financeMetrics.includes(key[0]));
      const relevant_values = relevant_entries.filter((entry: any[]) => entry[1] !== null && entry[1] !== '').length
      return (100 / relevant_entries.length) * relevant_values
    },
    backgroundMetricsComplete(state): number {
      const relevant_entries = (<any>Object).entries(state.data).filter((key: any[]) => backgroundMetrics.includes(key[0]));
      const relevant_values = relevant_entries.filter((entry: any[]) => entry[1] !== null && entry[1] != '').length
      return (100 / relevant_entries.length) * relevant_values
    },
    resultsScore(state): string {
      if(!state.results.score){
        return ""
      }
      return (state.results.score * 100).toFixed(2)

    }

  },
  actions: {
    async submitMetrics(){
      if(this.metricKeyCount !== this.metricValueCount){
        return
      }
      try {
        this.analysingPerformance = true;
        // this.data.curricular_units_1st_semester_credited = parseInt(String(this.data.curricular_units_1st_semester_credited))
        (<any>Object).keys(this.data).forEach((key:string) => {
          if(numericMetrics.includes(key)){
            // @ts-ignore
            this.data[(key as keyof typeof this.data)] = parseFloat(String(this.data[(key as keyof typeof this.data)]))
          }
        })
        const results = await axios.post('/api/performance-analysis', this.data).catch(e => {
          const error = useErrorStore()
          const err = e as AxiosError
          error.displayError(err.message)
        })
        this.analysingPerformance = false
        // update results
        if(!results || !results.data){
          this.analysingPerformance = false
          await this.resetResults()
          return
        }
        const { data } = results;
        this.results.featureDict = Object.assign({}, {
          "academic": data.feature_dict.academic,
          "finance": data.feature_dict.finance,
          "supportNetwork": data.feature_dict.support_network
        });
        this.results.featureMain = data.feature_main;
        this.results.featureStrength = data.feature_strength;
        this.results.label = data.label;
        this.results.score = data.score;
        this.results.optimumCategory = data.optimum_category;
        this.results.optimumCategoryValue=  data.optimum_category_value;
        this.resultsExist = true

        return results
      } catch (err) {
        this.analysingPerformance = false
      }
    },
    async resetResults() {
      this.resultsExist = false;
      this.results = Object.assign({}, {
        featureDict: {
          academic: 0,
            finance: 0,
            supportNetwork: 0
        },
        featureMain: "",
          featureStrength: 0,
          label: "",
          score: 0,
          optimumCategory: "",
          optimumCategoryValue: 0
      })
    }
  }
})