FROM node:16-alpine AS build

WORKDIR /webpanel

COPY package*.json ./
RUN npm install

EXPOSE 4200

COPY . .
RUN npm run build

CMD [ "npm", "start", "--" ,"--host", "0.0.0.0" ]