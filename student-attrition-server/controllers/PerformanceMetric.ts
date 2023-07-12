import { NextFunction, Request, Response } from "express";
import logger from "../utils/logger";
import axios from "axios";
import { MODEL_IP } from "../utils/habitat";

export async function performanceAnalysis(req: Request, res: Response, next: NextFunction){
  /** Takes user performance data, interfaces with the ML model server and returns the results to the user. */
  try {
    const results = await axios.post(`http://${MODEL_IP}/api/performance_analysis`, req.body).then(response => {
      return response.data
    }).catch(err => logger.error(err))
    return res.json(results)
  } catch (err){
    next(err)
  }
}