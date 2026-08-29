# 🚀 DevOps-26-09 Project

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Vite](https://img.shields.io/badge/Vite-B73BFE?style=for-the-badge&logo=vite&logoColor=FFD62E)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-F2F4F9?style=for-the-badge&logo=spring-boot)
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=java&logoColor=white)

Một dự án mẫu Fullstack sử dụng kiến trúc Monorepo, bao gồm Frontend xây dựng bằng React/Vite và Backend API bằng Java Spring Boot. Dự án đã được tích hợp sẵn tính năng xác thực người dùng bằng JWT (JSON Web Token).

## 📁 Cấu Trúc Dự Án

Dự án được chia thành các thư mục độc lập để dễ dàng mở rộng và quản lý:

```text
my-project/
├── apps/
│   ├── web/        # Mã nguồn Frontend (React + Vite + TypeScript)
│   └── api/        # Mã nguồn Backend (Spring Boot + Spring Security)
├── packages/       # Các thư viện hoặc config dùng chung (Shared libraries)
├── infrastructure/ # Cấu hình Docker, Nginx, CI/CD, Script triển khai
└── docs/           # Tài liệu kỹ thuật, kiến trúc và database
```

## 🛠 Công Nghệ Sử Dụng

- **Frontend:** React 18, Vite, React Router DOM, Vanilla CSS.
- **Backend:** Java 17, Spring Boot 3, Spring Security, Spring Data JPA.
- **Database:** H2 Database (In-memory) - Sẵn sàng chuyển sang MySQL/PostgreSQL.
- **Authentication:** JWT (JSON Web Token).

## ⚙️ Hướng Dẫn Cài Đặt và Chạy Dự Án

### Yêu Cầu Cần Thiết (Prerequisites)
- [Node.js](https://nodejs.org/) (>= 18.x)
- [Java JDK](https://adoptium.net/) (>= 17.x)
- [Maven](https://maven.apache.org/)

---

### 1. Khởi động Backend (API)

Di chuyển vào thư mục API và chạy máy chủ Spring Boot:

```bash
cd apps/api
mvn spring-boot:run
```

- Server sẽ khởi chạy tại: `http://localhost:8080`
- Bảng điều khiển H2 Database: `http://localhost:8080/h2-console`
  - **JDBC URL:** `jdbc:h2:mem:testdb`
  - **Username:** `sa`
  - **Password:** `password`

### 2. Khởi động Frontend (Web UI)

Mở một Terminal khác, di chuyển vào thư mục Web, cài đặt dependencies và chạy máy chủ phát triển:

```bash
cd apps/web
npm install
npm run dev
```

- Trình duyệt sẽ tự động mở hoặc bạn có thể truy cập: `http://localhost:3000` (hoặc `http://localhost:5173`)

## 🔑 API Endpoints (Xác thực)

| Method | Endpoint                  | Mô tả                                  | Yêu cầu bảo mật |
|--------|---------------------------|----------------------------------------|-----------------|
| `POST` | `/api/auth/register`      | Đăng ký người dùng mới                 | Không           |
| `POST` | `/api/auth/login`         | Đăng nhập và nhận chuỗi Token (JWT)    | Không           |

*Mọi request tới các endpoint khác đều cần gắn token vào Header:*
`Authorization: Bearer <Your_JWT_Token>`

## 📝 Roadmap Phát Triển
- [x] Khởi tạo cấu trúc dự án.
- [x] Xây dựng UI Đăng nhập / Đăng ký (Frontend).
- [x] Xây dựng JWT Authentication (Backend).
- [ ] Cấu hình `docker-compose` để chạy ứng dụng bằng Docker.
- [ ] Viết CI/CD pipelines với GitHub Actions.
