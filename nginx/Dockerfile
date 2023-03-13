FROM nginx:latest

COPY nginx.conf /etc/nginx/nginx.conf
COPY default.conf /etc/nginx/conf.d/


CMD ["nginx", "-g", "daemon off;"]
