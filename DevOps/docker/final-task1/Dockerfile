# Dockerfile
FROM wordpress:latest
COPY wp-config.php /var/www/html/
RUN chown www-data:www-data /var/www/html/wp-config.php
RUN apt update && apt install -y default-mysql-client
