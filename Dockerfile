FROM node:14.17.5

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install

COPY . .

# For development the testing is done on port 8001
EXPOSE 8001
CMD [ "node", "server.js" ]