FROM node:14-buster-slim
WORKDIR /app
COPY package*.json ./
RUN yarn
COPY docker-entrypoint.sh .
ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["start"]
