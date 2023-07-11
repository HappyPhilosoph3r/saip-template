export interface RequestError {
  status: number
}

export class RequestError extends Error {
  constructor(message?: string, code?: number){
    super(message)
    Object.setPrototypeOf(this, new.target.prototype)
    Error.captureStackTrace(this, RequestError)
    this.status = code || 500
  }
}