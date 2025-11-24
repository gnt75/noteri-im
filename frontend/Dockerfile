FROM node:18
WORKDIR /app
COPY . .
RUN npm install || true
RUN npm run build || true
EXPOSE 3000
CMD ["npm", "start"]
