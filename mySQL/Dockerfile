FROM mysql:latest


ENV MYSQL_ROOT_PASSWORD=pass_to_root
ENV MYSQL_DATABASE=nimbus
ENV MYSQL_USER=worker
ENV MYSQL_PASSWORD=worker

EXPOSE 3306

HEALTHCHECK --interval=10s --timeout=5s --retries=5 \
  CMD mysql --user=root --password=$MYSQL_ROOT_PASSWORD --execute="SELECT 1;" || exit 1


