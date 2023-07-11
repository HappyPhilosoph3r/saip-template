import { Router } from "express";
import * as PerformanceMetricOptionsController from "../controllers/PerformanceMetricOptions";

module.exports = function (router: Router){
  router.route('/performance-metric-options')
    .get(PerformanceMetricOptionsController.getPerformanceMetricOptions)
}