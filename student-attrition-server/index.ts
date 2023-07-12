import express, { json, Router, Request, Response, NextFunction } from "express"
import { DATABASE_IP, PORT } from "./utils/habitat";
import logger from "./utils/logger"
import mongoose from "mongoose";
import * as models from './models/index'
import fs from "fs";
import path from "path";
import { RequestError } from "./utils/RequestError";

const app = express()

// Import all database models before connecting to database.
models.init()

// Set up connection to MongoDb database
const databaseName = 'student_attrition_intervention_2'
mongoose.connect(`mongodb://${DATABASE_IP}/${databaseName}`);

const db = mongoose.connection;
// Check the mongoose connection is copacetic;
db.on('error', err => {
  logger.error(err)
});
db.once('open', () => {
  logger.info(`Successfully connected to ${databaseName} database`)
})

// Set up routers
const routeFiles = fs.readdirSync(__dirname + "/routes")

//Unprotected routes
const apiRouter = Router()
apiRouter.use(json())

// Add routes to router
routeFiles.forEach(routeFile => {
  require(path.join(__dirname, 'routes', routeFile))(apiRouter)
})

// Add next function which captures the full error and sends a limited response to the client
apiRouter.use(function(err: RequestError, req: Request, res: Response, next: NextFunction) {
  logger.error(err)
  res.status(err.status || 500).send({message: err.message})
})

// Bind the routers to their respective mount points
app.use('/api', json(), apiRouter);

// Start server
app.listen(PORT, () => {
  logger.info(`server started on ${PORT}`)
})