import { Router } from "express";
import * as PerformanceMetricController from "../controllers/PerformanceMetric";

module.exports = function (router: Router){
  router.route('/performance-analysis')
    .post(PerformanceMetricController.performanceAnalysis)
}