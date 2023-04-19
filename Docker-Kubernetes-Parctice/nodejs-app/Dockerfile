FROM node
WORKDIR /app

# Only copy package.json first
# required for npn installation
COPY package.json /app

RUN npm install

# Now when source code will change, it won't affect
# the upper layers of image
COPY . /app

EXPOSE 80
CMD ["node", "server.js"]