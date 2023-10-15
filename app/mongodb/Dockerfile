# Use the official MongoDB image as the base image
FROM mongo:latest

# Copy the init-mongodb.js script to the container
COPY init-mongodb.js /docker-entrypoint-initdb.d/

# Set the script to execute during container startup
CMD ["mongod", "--fork", "--logpath=/var/log/mongod.log", "--replSet=rs0"]

# Expose the default MongoDB port
EXPOSE 27017
