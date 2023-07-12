export const PORT = process.env.PORT || 4001;
export const NODE_ENV = process.env.NODE_ENV || 'development';
export const DOCKER = true;
export const MODEL_IP = DOCKER ? 'model:3001' : '127.0.0.1:3001';
export const DATABASE_IP = DOCKER ? 'database' : '127.0.0.1:27017';