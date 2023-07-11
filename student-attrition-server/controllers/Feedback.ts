import { NextFunction, Request, Response } from "express";
import { Feedback } from "../models/Feedback";
import logger from "../utils/logger";

export async function createFeedback(req: Request, res: Response, next: NextFunction){
  /** Takes user feedback and creates an instance in the database */
  try {
    req.body.ipAddress = req.headers['x-forwarded-for'] || req.socket.remoteAddress;
    const feedback = new Feedback(req.body)
    await feedback.save()
    logger.info(`new feedback created with ipAddress ${feedback.ipAddress})`)
    return res.send()
  } catch (err) {
    next(err)
  }
}
