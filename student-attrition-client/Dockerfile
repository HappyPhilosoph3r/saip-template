FROM node:lts-alpine as build-stage

WORKDIR /student-attrition-client

COPY package*.json ./

RUN npm install

COPY . .

CMD ["npm", "run", "dev", "--", "--host"]

EXPOSE 5173