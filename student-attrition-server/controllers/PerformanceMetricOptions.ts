import {NextFunction, Request, Response} from "express";
import {IPerformanceMetricOptions, PerformanceMetricOptions} from "../models/PerformanceMetricOptions";
import logger from "../utils/logger";
import {createPerformanceMetricOptions} from "../services/PerformanceMetricOptions";

export async function getPerformanceMetricOptions(req: Request, res: Response, next: NextFunction){
  /**  If performance metric options exists then returns all options to the client. If not generates the required
   * options in the database, then returns them to the client. */
  try {
    const options = await PerformanceMetricOptions.findOne({name: "performanceMetricOptions"});
    if(!options){
      logger.error("Performance Metric Options could not be found.")
      throw Error("Performance Metric Options could not be found.")
    }
    return res.json(options)
  } catch (err) {
    await createPerformanceMetricOptions()
    try {
      const options = await PerformanceMetricOptions.findOne({name: "performanceMetricOptions"});
      if(!options){
        logger.error("Performance Metric Options could not be found.")
        throw Error("Performance Metric Options could not be found.")
      }
      return res.json(options)
    } catch (err) {
      next(err)
    }
  }
}