FROM jwilder/nginx-proxy:alpine

# Set Max Client Size
COPY containers/proxy-ssl/client_max_body_size.conf /etc/nginx/conf.d

# Copy Local Certs into the Proxy
COPY ./keys/local.projectscapa.com.crt /etc/nginx/certs/local.projectscapa.com.crt
COPY ./keys/local.projectscapa.com.key /etc/nginx/certs/local.projectscapa.com.key
