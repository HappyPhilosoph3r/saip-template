import path from "path";
import { createLogger, format, transports } from "winston";
import { NODE_ENV } from "./habitat";

const logPath = path.join(__dirname, '..', '..', 'logs')

const dirError = path.join(logPath, 'error.log')
const dirInfo = path.join(logPath, 'combined.log')
const dirException =  path.join(logPath, 'exception.log')

const loggerProduction = createLogger({
  level: 'info',
  format: format.combine(
    format.timestamp(),
    format.errors(),
    format.json()
  ),
  transports: [
    new transports.File({ filename: dirError, level: 'error'}),
    new transports.File({ filename: dirInfo})
  ],
  exceptionHandlers: [
    new transports.File({ filename: dirException})
  ]
})

const loggerDeveloper = createLogger({
  format: format.combine(
    format.simple(),
    format.errors({stack: true}),
  ),
  transports: [
    new transports.Console()
  ]
})

const logger = NODE_ENV === 'production' ? loggerProduction : loggerDeveloper;

export default logger