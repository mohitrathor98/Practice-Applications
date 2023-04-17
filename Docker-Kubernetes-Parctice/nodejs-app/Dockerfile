FROM node 
#from node image present in docker hub

# setting up a working directory
WORKDIR /app

# copy the code to the container
COPY . /app

# Run Command when image is created
RUN npm install

# expose port 80 to outside environment
# as our application is listening on port 80
EXPOSE 80

# Run command when container is created
CMD ["node", "server.js"]