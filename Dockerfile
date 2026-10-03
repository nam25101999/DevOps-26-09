# Multi-stage Dockerfile cho Dictionary App (Bài 2 Jenkins Pipeline)

# Stage 1: Build Frontend (React + Vite)
FROM node:18-alpine AS frontend-builder
WORKDIR /app/frontend
COPY giuaky_Cao_Khanh_Linh/frontend/package*.json ./
RUN npm install
COPY giuaky_Cao_Khanh_Linh/frontend/ ./
RUN npm run build

# Stage 2: Production Backend (Express API + Static React Frontend)
FROM node:18-alpine
WORKDIR /app
COPY giuaky_Cao_Khanh_Linh/backend/package*.json ./
RUN npm install --production
COPY giuaky_Cao_Khanh_Linh/backend/ ./
# Copy các file frontend đã build vào thư mục public của backend để Express serve
COPY --from=frontend-builder /app/frontend/dist ./public

EXPOSE 3000
CMD ["npm", "start"]
