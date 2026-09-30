# 1. Base Image: Start with the lightweight Alpine version
FROM nginx:alpine

# 2. Workdir: Set the "current directory" inside the container
# Any command we run after this happens here.
WORKDIR /usr/share/nginx/html

# 3. Copy: Take the code from your laptop and BAKE it into the image
# (Replaces the need for a Bind Mount in production)
COPY website/ .

# 4. Expose: Document that this container listens on Port 80
# (This is for humans/documentation; it doesn't actually open the port)
EXPOSE 80

# 5. Command: Start Nginx
CMD ["nginx", "-g", "daemon off;"]
