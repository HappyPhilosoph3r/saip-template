import { NextFunction, Request, Response } from "express";
import logger from "../utils/logger";
import axios from "axios";

export async function performanceAnalysis(req: Request, res: Response, next: NextFunction){
  /** Takes user performance data, interfaces with the ML model server and returns the results to the user. */
  try {
    console.log(req.body)
    const results = await axios.post("http://127.0.0.1:6000/api/performance_analysis", req.body).then(response => {
      return response.data
    }).catch(err => logger.error(err))

    return res.json(results)
  } catch (err){
    next(err)
  }
}