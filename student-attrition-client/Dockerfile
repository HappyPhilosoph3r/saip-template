FROM node:lts-alpine AS build-stage

WORKDIR /student-attrition-client

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

FROM nginx:stable-alpine AS production-stage

COPY  ./nginx.conf /etc/nginx/conf.d/default.conf

COPY --from=build-stage /student-attrition-client/dist /usr/share/nginx/html

EXPOSE 80

 CMD ["nginx", "-g", "daemon off;"]
