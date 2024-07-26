# Use an official Node.js runtime as the base image
FROM node:latest AS dev

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json to the working directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code to the working directory
COPY . .

# Expose port 5173
EXPOSE 8000

# Run the Vue.js application in development mode
CMD ["npm", "run", "dev"]
