FROM node:lts-alpine3.12 as build

# The /app directory should act as the main application directory
WORKDIR /app

COPY . .

RUN npm install


CMD [ "npm", "run", "build" ]
