# docker build -t arq-express-app .
# docker run arq-express-app -p 3000:3000

FROM node:10.15.3

RUN mkdir /app
WORKDIR /app

COPY app.js .
COPY package.json .
COPY package-lock.json .

RUN npm install

ENTRYPOINT ["node", "app.js"]
