FROM node:20-alpine

WORKDIR /app

ENV NODE_ENV=production \
    PORT=3000

# Cài đặt dependencies backend
COPY package*.json ./
RUN npm ci --omit=dev

# Copy toàn bộ mã nguồn backend vào container (bao gồm cả thư mục mssv)
COPY . ./

# Đảm bảo file mssv.txt có sẵn ở cả /app/mssv/mssv.txt và /app/mssv.txt
RUN if [ -f ./mssv/mssv.txt ]; then cp ./mssv/mssv.txt ./mssv.txt; fi

EXPOSE 3000

CMD ["node", "server.js"]
