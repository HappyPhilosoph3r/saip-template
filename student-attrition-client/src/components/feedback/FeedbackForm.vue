<script setup lang="ts">
  import { ref, reactive} from "vue";
  import { useRoute } from "vue-router";
  import SuccessDialog from "@/components/dialogs/SuccessDialog.vue";
  import axios from "axios";
  import { useErrorStore } from "@/stores/errorStore";
  import type { AxiosError } from "axios";

  const route = useRoute()

  let openFeedbackDialog = ref(false)
  let openSuccessDialog = ref(false)
  const feedbackTypes = ['Bug Report', 'Feature Request', 'General Feedback']

  interface IInfo {
    genus: string;
    content: string;
    routeName: string | null
  }

  let info: IInfo = reactive({
    genus: "General Feedback",
    content: "",
    routeName: ""
  })

  function getRouteName(route_info: any){
    const name = route_info.name
    if(name) {
      return name.toString()
    }
    return null
  }

  async function submitFeedback(){
    try{
      info.routeName = getRouteName(route)
      await axios.post("/api/feedback", info).then(() => {
        openFeedbackDialog.value = false
        openSuccessDialog.value = true
      }).catch(e => {
        const error = useErrorStore()
        const err = e as AxiosError
        error.displayError(err.message)
      })
    } catch (err) {
      const error = useErrorStore()
      error.displayError("Could not submit feedback")
    }

  }

</script>
<template>
  <v-btn @click.prevent="openFeedbackDialog = !openFeedbackDialog">Feedback</v-btn>
  <v-dialog v-model="openFeedbackDialog" width="500">
    <v-card>
      <h1> Provide Feedback </h1>
      <v-form ref="feedbackForm" @submit.prevent="submitFeedback">
        <v-autocomplete v-model="info.genus"
                        :items="feedbackTypes"
                        label="Feedback Type"
        >
        </v-autocomplete>
        <v-textarea v-model="info.content"
                    label="Feedback"
        >
        </v-textarea>
        <v-card-actions class="justify-space-around">
          <v-btn @click.prevent="openFeedbackDialog = !openFeedbackDialog" color="error">Cancel</v-btn>
          <v-btn type="submit" color="primary">Submit</v-btn>
        </v-card-actions>
      </v-form>
    </v-card>
  </v-dialog>
  <success-dialog v-model="openSuccessDialog"
                  title="Feedback Successfully Submitted"
                  message="Thank you for taking the time!">
  </success-dialog>
</template>
<style scoped>
  h1 {
    text-align: center;
  }

</style>