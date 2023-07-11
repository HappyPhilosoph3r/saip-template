import { Router } from "express";
import * as FeedbackController from "../controllers/Feedback";

module.exports = function (router: Router){
  router.route('/feedback')
    .post(FeedbackController.createFeedback)
}