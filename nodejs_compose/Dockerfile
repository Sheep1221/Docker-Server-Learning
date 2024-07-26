# Use the official Node.js 14 image as the base image
FROM node:14

# Install nvm
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

# Set up environment variables for nvm
ENV NVM_DIR /root/.nvm
ENV NODE_VERSION 14.17.0

# Install the desired Node.js version
RUN . $NVM_DIR/nvm.sh && nvm install $NODE_VERSION

# Create and change to the app directory
WORKDIR /usr/src/app

# Copy the package.json and package-lock.json files
COPY package*.json ./

# Install dependencies using nvm's node
RUN . $NVM_DIR/nvm.sh && nvm use $NODE_VERSION && npm install

# Copy the rest of the application files
COPY . .

# Expose the port the app runs on
EXPOSE 3000

# Start the application
CMD ["/bin/bash", "-c", ". $NVM_DIR/nvm.sh && nvm use $NODE_VERSION && npm start"]

