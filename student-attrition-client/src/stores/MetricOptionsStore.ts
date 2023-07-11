import { defineStore } from "pinia";
import axios from "axios";
import type { IMetricOptions } from "../../@types/metrics";
import { useErrorStore } from "@/stores/errorStore";
import type { AxiosError } from "axios";


export const useMetricOptionsStore = defineStore('metricOptionsStore', {
  state: (): IMetricOptions =>  ({
    name: null,
    marital_status: [],
    application_mode: [],
    course: [],
    attendance_type: [],
    previous_qualification: [],
    nationality: [],
    parental_qualification: [],
    parental_occupation: [],
    binary: [],
    gender: []
  }),
  getters: {
  },
  actions: {
    async getMetricOptions(){
      try {
        const results = await axios.get('/api/performance-metric-options').then(response => {
          return response.data
        }).catch(e => {
          const error = useErrorStore()
          const err = e as AxiosError
          error.displayError(err.message)
        })
        this.name = results.name
        this.marital_status = results.marital_status
        this.application_mode = results.application_mode
        this.course = results.course
        this.attendance_type = results.attendance_type
        this.previous_qualification = results.previous_qualification
        this.nationality = results.nationality
        this.parental_qualification = results.parental_qualification
        this.parental_occupation = results.parental_occupation
        this.binary = results.binary
        this.gender = results.gender

      } catch (err) {
        const error = useErrorStore()
        error.displayError("Could not access performance metric options from server")
      }
    }
  }
})