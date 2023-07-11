import { defineStore } from "pinia";
import type { IError } from "../../@types/errors";

export const useErrorStore = defineStore('errorStore', {
  state: (): IError => ({
    errorOccurred: false,
    title: "An Error Occurred",
    message: null
  }),
  getters: {},
  actions: {
    displayError(err: string, title: null | string = null,){
      this.title = title ? title : "An Error Occurred"
      this.message = err
      this.errorOccurred = true
    },
    clearError(){
      this.errorOccurred = false
      this.title = "An Error Occurred"
      this.message = null
    }
  }
})