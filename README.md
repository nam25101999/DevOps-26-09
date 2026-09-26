<div align="center">

# 🌟 DevOps-26-09 🌟
**Monorepo Fullstack Architecture**

[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![Vite](https://img.shields.io/badge/Vite-B73BFE?style=for-the-badge&logo=vite&logoColor=FFD62E)](https://vitejs.dev/)
[![Spring Boot](https://img.shields.io/badge/Spring_Boot-F2F4F9?style=for-the-badge&logo=spring-boot)](https://spring.io/projects/spring-boot)
[![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=java&logoColor=white)](https://www.java.com/)
[![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)](https://jwt.io/)
[![H2 Database](https://img.shields.io/badge/H2-%23000000.svg?style=for-the-badge&logo=apache&logoColor=white)](#)
[![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)

*Một dự án mẫu Fullstack hiện đại được thiết kế với giao diện UI tuyệt đẹp, API bảo mật tối đa và sẵn sàng để triển khai hệ thống lớn.*

<br/>

[Khám phá Frontend](#-hướng-dẫn-cài-đặt) .
[Khám phá Backend](#1-khởi-động-backend-api) .
[API Docs](#-api-endpoints)

</div>

---

## 🎨 Cấu Trúc Khổng Lồ (Monorepo)

Dự án được phân chia một cách khoa học để mở rộng thành hệ thống Microservices hoặc nhiều Apps dùng chung tài nguyên:

<details open>
<summary><b>🔥 Click để xem Chi tiết Kiến trúc Cây</b></summary>
<br/>

```text
my-project/
├── 🌈 apps/
│   ├── ⚛️ web/           # 💻 Frontend App (React 18, Vite, TS, Vanilla CSS)
│   └── ☕ api/           # ⚙️ Backend App (Spring Boot 3, Spring Security JWT)
├── 📦 packages/          # 🧩 Thư viện nội bộ (Shared Utils, Type Definitions)
├── 🚀 infrastructure/    # 🐋 Cấu hình System (Docker, Nginx, Kubernetes scripts)
└── 📚 docs/              # 📖 Tài liệu kỹ thuật, Sơ đồ cơ sở dữ liệu 
```
</details>

---

## 💎 Điểm Nổi Bật

✨ **Giao Diện Siêu Mượt:** Sử dụng phong cách thiết kế **Glassmorphism**, đổ bóng mềm mại, animation cực kỳ hiện đại.  
🔒 **Bảo Mật Kép:** Spring Security kết hợp với JWT Token. Các Endpoint được bảo vệ nghiêm ngặt.  
⚡ **Tốc Độ Bàn Thờ:** Nhờ Vite, Frontend build và Hot-Reload (HMR) trong chớp mắt. Backend dùng H2 Database in-memory chạy mượt mà không cần cài cắm phức tạp.  
🧱 **Kiến Trúc Mở Rộng:** Sẵn sàng kết nối cơ sở dữ liệu lớn (PostgreSQL, MySQL), tích hợp CI/CD và Docker.  

---

## 🚀 Hướng Dẫn Cài Đặt

### 🛠 Yêu Cầu Môi Trường
> [!IMPORTANT]
> Máy tính của bạn cần được cài đặt sẵn các phần mềm sau:
- 🟢 **Node.js** (>= 18.x)
- ☕ **Java JDK** (>= 17.x)
- 🌀 **Apache Maven**

---

### 1️⃣ Khởi động Backend (API)

Mở **Terminal / PowerShell** và tiến hành chạy lệnh:

```bash
cd apps/api
mvn spring-boot:run
```

| Dịch vụ | Đường dẫn Truy cập | Trạng Thái |
| :--- | :--- | :---: |
| **Trang chủ API** | [http://localhost:8080](http://localhost:8080) | 🟢 |
| **H2 Database Console** | [http://localhost:8080/h2-console](http://localhost:8080/h2-console) | 🟠 |
> *JDBC URL:* `jdbc:h2:mem:testdb` | *User:* `sa` | *Password:* `password`

---

### 2️⃣ Khởi động Frontend (Web UI)

Mở **Terminal mới**, chạy 2 dòng lệnh thần thánh này để chiêm ngưỡng giao diện:

```bash
cd apps/web
npm install
npm run dev
```
> Trình duyệt sẽ tự động mở lên tại **[http://localhost:3000](http://localhost:3000)** (Hoặc `5173`).

---

## 🔐 API Endpoints

Hệ thống cung cấp sẵn các cổng giao tiếp bảo mật để test tính năng:

| Endpoint (POST) | Chức Năng | Auth Required | Payload / Body (JSON) |
| :--- | :--- | :---: | :--- |
| 🛡️ `/api/auth/register` | Đăng ký tài khoản | ❌ Không | `{ "name": "A", "email": "a@b.c", "password": "123" }` |
| 🔑 `/api/auth/login` | Đăng nhập hệ thống | ❌ Không | `{ "email": "a@b.c", "password": "123" }` |

> 💡 **Mẹo:** Các API chức năng khác (sau này) bắt buộc truyền Token theo Header: `Authorization: Bearer <Your_JWT_Token>`

---

## 🐧 Tài Liệu Thực Hành Linux Commands

<details>
<summary><b>🔥 Click để xem Linux Commands cho DevOps</b></summary>
<br/>

| Phần | Nội Dung | Link |
|:---:|:---|:---:|
| 📌 | Lệnh cơ bản: `pwd`, `whoami`, `hostname`, `date`, `echo`, `which` | [Xem →](./docs/linux-commands/README.md#️-1-lệnh-cơ-bản) |
| 📁 | Quản lý thư mục: `mkdir`, `cd`, `rmdir`, `tree` | [Xem →](./docs/linux-commands/README.md#-2-quản-lý-thư-mục) |
| 📄 | Quản lý file: `touch`, `cp`, `mv`, `rm`, `echo >` | [Xem →](./docs/linux-commands/README.md#-3-quản-lý-file) |
| 👀 | Đọc file: `cat`, `head`, `tail`, `wc`, `less` | [Xem →](./docs/linux-commands/README.md#-4-đọc-file) |
| ✏️ | Chỉnh sửa: `nano`, `vim` | [Xem →](./docs/linux-commands/README.md#️-5-chỉnh-sửa-file) |
| 🔍 | Tìm kiếm: `find . -name`, `find -type f` | [Xem →](./docs/linux-commands/README.md#-6-tìm-kiếm-file-find) |
| 🔎 | GREP: `grep`, `grep -i`, `grep -n`, `grep -r` | [Xem →](./docs/linux-commands/README.md#-7-grep--cực-kỳ-quan-trọng) |
| 🏷️ | Alias: `alias`, `unalias` | [Xem →](./docs/linux-commands/README.md#️-8-alias) |

**📸 Screenshots thực hành trên Ubuntu WSL2:**

| Screenshot | Nội dung |
|:---:|:---|
| [01-basic-commands.jpg](./docs/linux-commands/screenshots/01-basic-commands.jpg) | Lệnh cơ bản + Quản lý thư mục |
| [02-file-management.jpg](./docs/linux-commands/screenshots/02-file-management.jpg) | Quản lý file + Đọc file |
| [03-grep-find.jpg](./docs/linux-commands/screenshots/03-grep-find.jpg) | Tìm kiếm file + GREP |

**🎬 Video Demo:**
- [`linux-commands-real.cast`](./docs/linux-commands/videos/linux-commands-real.cast) — Asciinema recording thực tế (phát bằng `asciinema play`)
- [`demo-script.sh`](./docs/linux-commands/videos/demo-script.sh) — Script demo đầy đủ

📖 **[Xem tài liệu đầy đủ →](./docs/linux-commands/README.md)**

</details>

---

<div align="center">
  <b>🌟 🌟 🌟 Roadmap Phát Triển Tương Lai 🌟 🌟 🌟</b>
</div>

- [x] Khởi tạo cấu trúc dự án chuẩn Monorepo.
- [x] Xây dựng UI Đăng nhập / Đăng ký hiện đại.
- [x] Xây dựng JWT Authentication (Backend).
- [x] 🐧 Thực hành Linux Commands cơ bản trên Ubuntu WSL2.
- [ ] 🐳 Cấu hình `docker-compose.yml` chạy siêu mượt.
- [x] 🤖 Tự động hoá triển khai với GitHub Actions (Build & Push Docker Image lên GHCR).
- [ ] 🐘 Chuyển đổi Database sang PostgreSQL.

---
<div align="center">
  <i>Được thiết kế và phát triển với ❤️ trong dự án DevOps-26-09</i>
</div>
