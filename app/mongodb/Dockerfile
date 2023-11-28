# Use the official MongoDB image as the base image
FROM mongo:latest

# Copy the init-mongodb.js script to the container
COPY init-mongodb.js /docker-entrypoint-initdb.d/

# Set the script to execute during container startup
CMD ["mongod", "--bind_ip_all"]
# Expose the default MongoDB port
EXPOSE 27017
