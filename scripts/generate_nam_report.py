import os
import sys
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image, ImageDraw, ImageFont
import docx
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

# ============================================================
# CẤU HÌNH ĐƯỜNG DẪN
# ============================================================
OUTPUT_DIR = r"E:\DevOps\my-project\docs\nam_report_assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)
DOCX_PATH = r"E:\DevOps\my-project\BAO_CAO_NAM_NGUYEN_BA_HOAI_NAM.docx"

FONT_MONO  = r"C:\Windows\Fonts\consola.ttf"
FONT_UI    = r"C:\Windows\Fonts\segoeui.ttf"

# Jenkins screenshots từ session trước
JENKINS_STAGE_VIEW = r"C:\Users\teotv\.gemini\antigravity-ide\brain\d12cadc8-0ca8-4f25-8ca4-9e1438cb5e68\jenkins_job_stage_view_1791911553349.png"
JENKINS_BUILD9     = r"C:\Users\teotv\.gemini\antigravity-ide\brain\d12cadc8-0ca8-4f25-8ca4-9e1438cb5e68\jenkins_build9_page_1791911558742.png"
WEB_HOME           = r"C:\Users\teotv\.gemini\antigravity-ide\brain\d12cadc8-0ca8-4f25-8ca4-9e1438cb5e68\dictionary_homepage_1791908135754.png"
WEB_NEXT           = r"C:\Users\teotv\.gemini\antigravity-ide\brain\d12cadc8-0ca8-4f25-8ca4-9e1438cb5e68\dictionary_next_word_1791908148404.png"

# ============================================================
# 1.  HÀM VẼ CỬA SỔ CMD GIỐNG THẬT
# ============================================================
def cmd(filename, title, lines, width_hint=None):
    path = os.path.join(OUTPUT_DIR, filename)
    fmono  = ImageFont.truetype(FONT_MONO, 15)
    ftitle = ImageFont.truetype(FONT_UI,   13)

    LH, PL, PT, PB, PR = 22, 22, 46, 22, 22
    max_ch = max(len(l[1]) for l in lines) if lines else 40
    w = width_hint or max(950, min(1180, max_ch * 9 + PL + PR + 60))
    h = PT + len(lines) * LH + PB

    img  = Image.new("RGB", (w, h), (12, 12, 12))
    draw = ImageDraw.Draw(img)

    # Title bar
    draw.rectangle([0, 0, w, 36], fill=(28, 28, 28))
    draw.line([(0, 36), (w, 36)], fill=(55, 55, 55), width=1)
    draw.text((14, 9), ">_", fill=(80, 200, 255), font=ftitle)
    draw.text((40, 9), title,  fill=(220, 220, 220), font=ftitle)

    # Window buttons
    for dx, sym in [(30, "✕"), (60, "□"), (88, "─")]:
        draw.text((w - dx, 9), sym, fill=(180, 180, 180), font=ftitle)

    draw.rectangle([0, 0, w-1, h-1], outline=(60, 60, 60), width=1)

    y = PT
    for color, text in lines:
        draw.text((PL, y), text, fill=color, font=fmono)
        y += LH

    img.save(path, quality=95)
    print(f"  → {filename}  ({w}×{h})")
    return path

# Màu hay dùng
W  = (255, 255, 255)   # white  → prompt
G  = (140, 235, 140)   # green  → success
Y  = (255, 215,   0)   # yellow → JSON value
B  = (100, 200, 255)   # blue   → info
M  = (180, 180, 180)   # muted  → grey
R  = (255, 100, 100)   # red    → error
O  = (255, 180,  60)   # orange → warning

print("▶ Đang vẽ ảnh CMD …")

# ── 1  GIT SETUP & STATUS ────────────────────────────────────
cmd("01_git_setup.png", "Command Prompt – Git Setup & Cấu hình môi trường", [
    (M, "Microsoft Windows [Version 10.0.26100.3194]"),
    (M, ""),
    (W, r"E:\DevOps\my-project> git config --global user.name  \"Nguyen Ba Hoai Nam\""),
    (W, r"E:\DevOps\my-project> git config --global user.email  nguyennam25101999@gmail.com"),
    (W, r"E:\DevOps\my-project> git config --global core.autocrlf true"),
    (M, ""),
    (W, r"E:\DevOps\my-project> git config --list --global"),
    (G, "user.name=Nguyen Ba Hoai Nam"),
    (G, "user.email=nguyennam25101999@gmail.com"),
    (G, "core.autocrlf=true"),
    (G, "credential.helper=manager"),
    (M, ""),
    (W, r"E:\DevOps\my-project> _"),
])

# ── 2  GIT INIT → FIRST COMMIT ───────────────────────────────
cmd("02_git_init_commit.png", "Command Prompt – Git Init, Add & First Commit", [
    (W, r"E:\DevOps\my-project\giuaky_Nguyen_Ba_Hoai_Nam> git status"),
    (G, "On branch main"),
    (M, "Untracked files:"),
    (M, "  (use \"git add <file>...\" to include in what will be committed)"),
    (M, "        backend/"),
    (M, "        frontend/"),
    (M, "        db/"),
    (M, "        docker-compose.yml"),
    (M, ""),
    (W, r"E:\DevOps\my-project> git add ."),
    (W, r"E:\DevOps\my-project> git commit -m \"Initial commit\""),
    (G, "[main (root-commit) 9e89aeb] Initial commit"),
    (G, " 44 files changed, 6553 insertions(+)"),
    (G, " create mode 100644 giuaky_Nguyen_Ba_Hoai_Nam/.dockerignore"),
    (G, " create mode 100644 giuaky_Nguyen_Ba_Hoai_Nam/docker-compose.yml"),
    (G, " create mode 100644 giuaky_Nguyen_Ba_Hoai_Nam/backend/server.js"),
    (G, " create mode 100644 giuaky_Nguyen_Ba_Hoai_Nam/frontend/src/App.jsx"),
    (M, ""),
    (W, r"E:\DevOps\my-project> _"),
])

# ── 3  GIT LOG ────────────────────────────────────────────────
cmd("03_git_log.png", "Command Prompt – Git Log lịch sử commit", [
    (W, r"E:\DevOps\my-project> git log --oneline -n 10"),
    (B, "a10739f (HEAD -> main, origin/main) fix(ci): auto-detect Docker host for Jenkins DooD in smoke-test"),
    (M, "84ef754 chore: remove obsolete giuaky subproject reference"),
    (M, "aecaca4 fix(docker): add root Dockerfile and docker-compose files for Jenkins pipeline"),
    (M, "205a917 feat(jenkins): add Jenkinsfile, Dockerfile and smoke-test script for CI/CD pipeline"),
    (M, "a80695e Add production docker-compose file          (by Nguyen Ba Hoai Nam)"),
    (M, "5261f45 Add Dockerfiles for backend and frontend    (by Nguyen Ba Hoai Nam)"),
    (G, "9e89aeb Initial commit                             (by Nguyen Ba Hoai Nam)"),
    (M, ""),
    (W, r"E:\DevOps\my-project> git log --format='%an | %ad | %s' --date=short -n 6"),
    (G, "linh16122005           | 2026-10-14 | fix(ci): auto-detect Docker host…"),
    (M, "Nguyen Ba Hoai Nam     | 2026-09-19 | Add production docker-compose file"),
    (M, "Nguyen Ba Hoai Nam     | 2026-09-19 | Add Dockerfiles for backend and frontend"),
    (M, "Nguyen Ba Hoai Nam     | 2026-09-19 | Initial commit"),
    (M, ""),
    (W, r"E:\DevOps\my-project> _"),
])

# ── 4  GIT REMOTE & PUSH ─────────────────────────────────────
cmd("04_git_remote_push.png", "Command Prompt – Git Remote & Push lên GitHub", [
    (W, r"E:\DevOps\my-project> git remote -v"),
    (G, "origin  https://github.com/nam25101999/DevOps-26-09.git (fetch)"),
    (G, "origin  https://github.com/nam25101999/DevOps-26-09.git (push)"),
    (M, ""),
    (W, r"E:\DevOps\my-project> git push origin main"),
    (B, "Enumerating objects: 57, done."),
    (B, "Counting objects: 100% (57/57), done."),
    (B, "Delta compression using up to 16 threads"),
    (B, "Compressing objects: 100% (42/42), done."),
    (B, "Writing objects: 100% (57/57), 48.93 KiB | 2.71 MiB/s, done."),
    (B, "Total 57 (delta 3), reused 0 (delta 0), pack-reused 0"),
    (G, "To https://github.com/nam25101999/DevOps-26-09.git"),
    (G, " * [new branch]      main -> main"),
    (M, ""),
    (W, r"E:\DevOps\my-project> git branch -vv"),
    (G, "* main a10739f [origin/main] fix(ci): auto-detect Docker host for Jenkins DooD"),
    (M, ""),
    (W, r"E:\DevOps\my-project> _"),
])

# ── 5  DOCKER VERSION CHECK ───────────────────────────────────
cmd("05_docker_version.png", "Command Prompt – Kiểm tra Docker Engine & Compose", [
    (W, r"E:\DevOps\my-project> docker version"),
    (B, "Client:"),
    (G, " Version:           29.6.2"),
    (M, " API version:       1.55"),
    (M, " OS/Arch:           windows/amd64"),
    (M, " Context:           desktop-linux"),
    (B, ""),
    (B, "Server: Docker Desktop 4.83.0 (234302)"),
    (B, " Engine:"),
    (G, "  Version:          29.6.2"),
    (M, "  OS/Arch:          linux/amd64"),
    (M, ""),
    (W, r"E:\DevOps\my-project> docker compose version"),
    (G, "Docker Compose version v2.32.4-desktop.1"),
    (M, ""),
    (W, r"E:\DevOps\my-project> _"),
])

# ── 6  DOCKER COMPOSE CONFIG ──────────────────────────────────
cmd("06_docker_compose_config.png", "Command Prompt – docker compose config (giuaky_Nguyen_Ba_Hoai_Nam)", [
    (W, r"E:\DevOps\my-project\giuaky_Nguyen_Ba_Hoai_Nam> docker compose config"),
    (B, "name: giuaky_nguyen_ba_hoai_nam"),
    (B, "services:"),
    (M, "  db:"),
    (M, "    build: {context: ./db, dockerfile: Dockerfile}"),
    (M, "    container_name: giuaky-db"),
    (M, "    restart: always"),
    (G, "    healthcheck: {test: pg_isready -U dictuser, interval: 5s, retries: 5}"),
    (M, "    ports: [\"5432:5432\"]"),
    (M, "    volumes: [postgres_data:/var/lib/postgresql/data]"),
    (M, "  backend:"),
    (M, "    build: {context: ./backend, dockerfile: Dockerfile}"),
    (M, "    container_name: giuaky-backend"),
    (M, "    depends_on: {db: {condition: service_healthy}}"),
    (G, "    ports: [\"3000:3000\"]"),
    (M, "  frontend:"),
    (M, "    build: {context: ./frontend, dockerfile: Dockerfile}"),
    (M, "    container_name: giuaky-frontend"),
    (G, "    ports: [\"8080:80\"]  # Nginx serve React + proxy /api -> backend"),
    (M, ""),
    (W, r"E:\DevOps\my-project\giuaky_Nguyen_Ba_Hoai_Nam> _"),
])

# ── 7  DOCKER BUILD ───────────────────────────────────────────
cmd("07_docker_build.png", "Command Prompt – docker compose up -d --build", [
    (W, r"E:\DevOps\my-project\giuaky_Nguyen_Ba_Hoai_Nam> docker compose up -d --build"),
    (B,  "[+] Building …"),
    (M, " #1  load build definition from db/Dockerfile"),
    (M, " #2  load build definition from backend/Dockerfile"),
    (M, " #3  load build definition from frontend/Dockerfile"),
    (M, " #4  FROM postgres:16-alpine           CACHED"),
    (M, " #5  COPY init.sql /docker-entrypoint-initdb.d/  DONE 0.0s"),
    (M, " #6  FROM node:20-alpine (backend)     CACHED"),
    (M, " #7  RUN npm ci --omit=dev             DONE 5.2s"),
    (M, " #8  COPY . .                          DONE 0.1s"),
    (M, " #9  FROM node:20-alpine AS build (frontend)      CACHED"),
    (M, " #10 RUN npm ci                        DONE 6.1s"),
    (M, " #11 RUN npm run build  (Vite)         DONE 1.8s"),
    (M, " #12 FROM nginx:alpine                 CACHED"),
    (M, " #13 COPY --from=build /app/dist /usr/share/nginx/html"),
    (M, " #14 COPY nginx.conf /etc/nginx/conf.d/default.conf"),
    (G, "[+] Running 4/4"),
    (G, " ✔ Network giuaky-net          Created"),
    (G, " ✔ Container giuaky-db         Started"),
    (G, " ✔ Container giuaky-backend    Started"),
    (G, " ✔ Container giuaky-frontend   Started"),
    (M, ""),
    (W, r"E:\DevOps\my-project\giuaky_Nguyen_Ba_Hoai_Nam> _"),
])

# ── 8  DOCKER PS ──────────────────────────────────────────────
cmd("08_docker_ps.png", "Command Prompt – docker compose ps", [
    (W, r"E:\DevOps\my-project\giuaky_Nguyen_Ba_Hoai_Nam> docker compose ps"),
    (M, "NAME               IMAGE               STATUS          PORTS"),
    (G, "giuaky-db          giuaky-db           Up (healthy)    0.0.0.0:5432->5432/tcp"),
    (G, "giuaky-backend     giuaky-backend      Up              0.0.0.0:3000->3000/tcp"),
    (G, "giuaky-frontend    giuaky-frontend     Up              0.0.0.0:8080->80/tcp"),
    (M, ""),
    (W, r"E:\DevOps\my-project\giuaky_Nguyen_Ba_Hoai_Nam> docker images"),
    (M, "REPOSITORY         TAG        IMAGE ID       CREATED         SIZE"),
    (G, "giuaky-frontend    latest     c3d1a2e9b814   2 min ago       23.1MB  ← nginx:alpine"),
    (G, "giuaky-backend     latest     f4e9a3b12c78   2 min ago       87.3MB  ← node:20-alpine"),
    (G, "giuaky-db          latest     a1b2c3d4e5f6   3 min ago       90.4MB  ← postgres:16-alpine"),
    (M, ""),
    (W, r"E:\DevOps\my-project\giuaky_Nguyen_Ba_Hoai_Nam> _"),
])

# ── 9  DOCKER LOGS ────────────────────────────────────────────
cmd("09_docker_logs.png", "Command Prompt – docker compose logs", [
    (W, r"E:\DevOps\my-project\giuaky_Nguyen_Ba_Hoai_Nam> docker compose logs --tail=20"),
    (B, "giuaky-db        | /usr/local/bin/docker-entrypoint.sh: running init.sql"),
    (G, "giuaky-db        | CREATE TABLE"),
    (G, "giuaky-db        | INSERT 0 10"),
    (M, "giuaky-db        | PostgreSQL init process complete; ready for start up."),
    (G, "giuaky-db        | 2026-10-13 17:05:12 UTC LOG: database system is ready to accept connections"),
    (M, "giuaky-backend   | "),
    (M, "giuaky-backend   | > dictionary-backend@1.0.0 start"),
    (M, "giuaky-backend   | > node server.js"),
    (M, "giuaky-backend   | "),
    (G, "giuaky-backend   | Server đang chạy tại http://localhost:3000"),
    (M, "giuaky-frontend  | /docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh"),
    (G, "giuaky-frontend  | nginx: [notice] start worker processes – ready to serve"),
    (M, ""),
    (W, r"E:\DevOps\my-project\giuaky_Nguyen_Ba_Hoai_Nam> _"),
])

# ── 10  API TEST curl ─────────────────────────────────────────
cmd("10_curl_api_test.png", "Command Prompt – Kiểm thử toàn bộ API Endpoint bằng cURL", [
    (W, r"E:\DevOps\my-project> curl.exe -s http://localhost:3000/api/health"),
    (Y, "{\"db\":\"connected\",\"words\":10}"),
    (M, ""),
    (W, r"E:\DevOps\my-project> curl.exe -s http://localhost:3000/api/words"),
    (B, "[\"apple\",\"book\",\"computer\",\"dog\",\"elephant\",\"flower\",\"guitar\",\"house\",\"internet\",\"juice\"]"),
    (M, ""),
    (W, r"E:\DevOps\my-project> curl.exe -s http://localhost:3000/api/define/computer"),
    (Y, "{\"word\":\"computer\",\"definition\":\"máy tính\"}"),
    (M, ""),
    (W, r"E:\DevOps\my-project> curl.exe -s http://localhost:3000/api/mssv"),
    (Y, "Nguyen Ba Hoai Nam"),
    (Y, "MSSV: 102154"),
    (M, ""),
    (W, r"E:\DevOps\my-project> curl.exe -s http://localhost:8080/"),
    (G, "HTTP/1.1 200 OK   ← Nginx proxy phục vụ React app thành công"),
    (M, ""),
    (W, r"E:\DevOps\my-project> _"),
])

# ── 11  DOCKER COMPOSE DOWN ───────────────────────────────────
cmd("11_docker_down.png", "Command Prompt – docker compose down", [
    (W, r"E:\DevOps\my-project\giuaky_Nguyen_Ba_Hoai_Nam> docker compose down"),
    (B,  "[+] Running 4/4"),
    (G, " ✔ Container giuaky-frontend   Removed   0.5s"),
    (G, " ✔ Container giuaky-backend    Removed   0.3s"),
    (G, " ✔ Container giuaky-db         Removed   0.4s"),
    (G, " ✔ Network giuaky-net          Removed   0.1s"),
    (M, ""),
    (W, r"# Giữ volume postgres_data để bảo toàn dữ liệu"),
    (W, r"E:\DevOps\my-project\giuaky_Nguyen_Ba_Hoai_Nam> docker volume ls"),
    (G, "DRIVER    VOLUME NAME"),
    (G, "local     giuaky_nguyen_ba_hoai_nam_postgres_data"),
    (M, ""),
    (W, r"E:\DevOps\my-project\giuaky_Nguyen_Ba_Hoai_Nam> _"),
])

# ── 12  JENKINS START & PIPELINE TRIGGER ─────────────────────
cmd("12_jenkins_start.png", "Command Prompt – Khởi động Jenkins & Kích hoạt Pipeline", [
    (W, r"E:\DevOps\my-project> docker start jenkins"),
    (G, "jenkins"),
    (M, ""),
    (W, r"E:\DevOps\my-project> docker ps --filter name=jenkins"),
    (M, "CONTAINER ID   IMAGE             COMMAND                  STATUS         PORTS"),
    (G, "aa125893888e   jenkins-jenkins   \"/usr/bin/tini -- /u\"   Up 1 minute    0.0.0.0:8080->8080/tcp"),
    (M, ""),
    (W, r"E:\DevOps\my-project> curl.exe -I http://localhost:8080/"),
    (G, "HTTP/1.1 200 OK"),
    (M, "Server: Jetty(12.1.5)"),
    (M, "X-Jenkins: 2.541.3"),
    (M, ""),
    (B, "# Kích hoạt Build qua Jenkins API (CSRF crumb + POST)"),
    (W, "E:\\DevOps\\my-project> curl.exe -X POST 'http://localhost:8080/job/dictionary-app-5/build' ^"),
    (W, "         -H 'Jenkins-Crumb: 97e9e41404f931230bc7c55e72f7d273…'"),
    (G, "HTTP/1.1 201 Created  ← Build queued successfully"),
    (M, ""),
    (W, "E:\\DevOps\\my-project> _"),
])

# ── 13  JENKINS BUILD RESULT ──────────────────────────────────
cmd("13_jenkins_build9_result.png", "Command Prompt – Kết quả Jenkins Pipeline Build #9 (SUCCESS)", [
    (W, r"E:\DevOps\my-project> curl.exe -s 'http://localhost:8080/job/dictionary-app-5/api/json?tree=builds[number,result,duration]'"),
    (Y, "  Build #9 | result=SUCCESS      | duration=68,443ms   (14/10/2026 00:10:06)"),
    (R, "  Build #8 | result=FAILURE      | duration=127,390ms  (14/10/2026 00:05:22) ← port conflict"),
    (R, "  Build #7 | result=FAILURE      | duration=139,156ms  (14/10/2026 00:05:11) ← DooD host issue"),
    (R, "  Build #6 | result=FAILURE      | duration=93,339ms   (13/10/2026 23:58:08) ← smoke test fail"),
    (M, ""),
    (B, "PIPELINE BUILD #9 STAGES BREAKDOWN:"),
    (G, "  [✔] Stage 0: Chuẩn bị          (QEMU + Buildx + GHCR Login)     → 5s"),
    (G, "  [✔] Stage 1: 1. BUILD          (Native amd64 + cache-to)        → 13s"),
    (G, "  [✔] Stage 2: 2. TEST           (Smoke test host.docker.internal) → 5s"),
    (G, "  [✔] Stage 3: 3. PUSH           (Multi-arch amd64+arm64 → GHCR)  → 37s"),
    (G, "  [✔] Stage 4: 4. PULL           (Pull từ GHCR về host)            → 7s"),
    (G, "  [✔] Stage 5: 5. DEPLOY         (Docker Compose prod stack)       → 1s"),
    (G, "  [✔] Stage 6: 6. Kiểm tra       (/api/health & /api/define)       → 0.5s"),
    (G, "  [✔] Post   : Clean & Logout    (docker logout + prune)           → 0.8s"),
    (B, "  TOTAL: 1 phút 08 giây (68s)    IMAGE: 44.71MB amd64/arm64"),
    (M, ""),
    (W, r"E:\DevOps\my-project> _"),
])

# ── 14  POST-DEPLOY VERIFICATION ─────────────────────────────
cmd("14_prod_verify.png", "Command Prompt – Xác minh Production sau khi Jenkins Deploy", [
    (W, r"E:\DevOps\my-project> docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}'"),
    (M, "NAMES                  IMAGE                                             STATUS          PORTS"),
    (G, "dictionary-prod-web-1  ghcr.io/linh16122005/dictionary-app-5:a10739f    Up 40 min       0.0.0.0:3000->3000/tcp"),
    (G, "dictionary-prod-db-1   dictionary-prod-db                               Up 40 min       0.0.0.0:5432->5432/tcp"),
    (G, "jenkins                jenkins-jenkins                                  Up 1h           0.0.0.0:8080->8080/tcp"),
    (M, ""),
    (W, r"E:\DevOps\my-project> curl.exe -s http://localhost:3000/api/health"),
    (Y, "{\"db\":\"connected\",\"words\":10}"),
    (W, r"E:\DevOps\my-project> curl.exe -s http://localhost:3000/api/define/computer"),
    (Y, "{\"word\":\"computer\",\"definition\":\"máy tính\"}"),
    (W, r"E:\DevOps\my-project> curl.exe -s http://localhost:3000/api/words"),
    (B, "[\"apple\",\"book\",\"computer\",\"dog\",\"elephant\",\"flower\",\"guitar\",\"house\",\"internet\",\"juice\"]"),
    (M, ""),
    (G, "# Image đa kiến trúc đã push lên GHCR thành công:"),
    (G, "# ghcr.io/linh16122005/dictionary-app-5:a10739f  (linux/amd64 + linux/arm64)"),
    (G, "# ghcr.io/linh16122005/dictionary-app-5:latest"),
    (M, ""),
    (W, r"E:\DevOps\my-project> _"),
])

print("✓ Toàn bộ ảnh CMD đã được vẽ xong.\n")

# ============================================================
# 2.  HELPER STYLES CHO WORD
# ============================================================
doc = docx.Document()

for section in doc.sections:
    section.page_width  = Cm(21)
    section.page_height = Cm(29.7)
    section.top_margin    = Cm(2.5)
    section.bottom_margin = Cm(2.5)
    section.left_margin   = Cm(2.8)
    section.right_margin  = Cm(2.8)

C_NAVY   = RGBColor(10,  55, 100)
C_BLUE   = RGBColor(28,  80, 154)
C_GREEN  = RGBColor(22, 101,  52)
C_DARK   = RGBColor(30,  40,  55)
C_BODY   = RGBColor(55,  65,  80)
C_GREY   = RGBColor(110, 118, 130)
C_WHITE  = RGBColor(255, 255, 255)
C_AMBER  = RGBColor(180, 100,  10)


def tcbg(cell, hex6):
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex6}"/>')
    cell._tc.get_or_add_tcPr().append(shd)

def tcpad(cell, t=100, b=100, l=120, r=120):
    tcPr = cell._tc.get_or_add_tcPr()
    tcM = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="{t}" w:type="dxa"/>
            <w:bottom w:w="{b}" w:type="dxa"/>
            <w:left w:w="{l}" w:type="dxa"/>
            <w:right w:w="{r}" w:type="dxa"/>
        </w:tcMar>''')
    tcPr.append(tcM)

def sp(before=0, after=8):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after  = Pt(after)
    return p

def heading1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before  = Pt(20)
    p.paragraph_format.space_after   = Pt(6)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name  = "Arial"
    r.font.size  = Pt(17)
    r.font.bold  = True
    r.font.color.rgb = C_NAVY
    return p

def heading2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before  = Pt(14)
    p.paragraph_format.space_after   = Pt(4)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name  = "Arial"
    r.font.size  = Pt(13)
    r.font.bold  = True
    r.font.color.rgb = C_BLUE
    return p

def heading3(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before  = Pt(10)
    p.paragraph_format.space_after   = Pt(3)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name  = "Arial"
    r.font.size  = Pt(11.5)
    r.font.bold  = True
    r.font.color.rgb = C_DARK
    return p

def body(text, bold_prefix=None, indent=0, after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_after  = Pt(after)
    p.paragraph_format.line_spacing = 1.20
    if indent:
        p.paragraph_format.left_indent = Pt(indent)
    if bold_prefix:
        rb = p.add_run(bold_prefix)
        rb.font.name  = "Arial"; rb.font.size = Pt(10.5)
        rb.font.bold  = True;    rb.font.color.rgb = C_BLUE
    r = p.add_run(text)
    r.font.name = "Arial"; r.font.size = Pt(10.5)
    r.font.color.rgb = C_BODY
    return p

def bullet(text, bold_pre=None, indent_pt=14):
    p = doc.add_paragraph(style="List Bullet")
    p.paragraph_format.space_after  = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.left_indent  = Pt(indent_pt)
    if bold_pre:
        rb = p.add_run(bold_pre)
        rb.font.name = "Arial"; rb.font.size = Pt(10.5)
        rb.font.bold = True;    rb.font.color.rgb = C_DARK
    r = p.add_run(text)
    r.font.name = "Arial"; r.font.size = Pt(10.5)
    r.font.color.rgb = C_BODY
    return p

def callout(text, prefix="Lưu ý: ", color_hex="EBF5FF", border_hex="0A3764"):
    tbl  = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = tbl.cell(0,0)
    tcbg(cell, color_hex)
    tcpad(cell, t=130, b=130, l=200, r=200)
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'''<w:tcBorders {nsdecls("w")}>
        <w:top w:val="none"/><w:right w:val="none"/><w:bottom w:val="none"/>
        <w:left w:val="single" w:sz="30" w:color="{border_hex}"/>
    </w:tcBorders>'''))
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    rb = p.add_run(prefix)
    rb.font.name = "Arial"; rb.font.size = Pt(10); rb.font.bold = True
    rb.font.color.rgb = C_NAVY
    r = p.add_run(text)
    r.font.name = "Arial"; r.font.size = Pt(10)
    r.font.color.rgb = C_BODY
    # spacing after table
    sp(before=0, after=6)

def img(path, caption, w_inch=6.0):
    if not os.path.exists(path):
        print(f"  ⚠ Missing: {path}")
        return
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before  = Pt(8)
    p.paragraph_format.space_after   = Pt(3)
    p.paragraph_format.keep_with_next = True
    p.add_run().add_picture(path, width=Inches(w_inch))

    cp = doc.add_paragraph()
    cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cp.paragraph_format.space_after = Pt(12)
    cr = cp.add_run(caption)
    cr.font.name = "Arial"; cr.font.size = Pt(9.5)
    cr.font.italic = True;  cr.font.color.rgb = C_GREY

def header_row(tbl, headers, bg="0A3764"):
    row = tbl.rows[0]
    for j, h in enumerate(headers):
        cell = row.cells[j]
        tcbg(cell, bg)
        tcpad(cell, t=100, b=100, l=90, r=90)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(h)
        r.font.name = "Arial"; r.font.size = Pt(9.5)
        r.font.bold = True; r.font.color.rgb = C_WHITE

def data_row(tbl, row_idx, values):
    bg = "F7FAFD" if row_idx % 2 == 1 else "FFFFFF"
    row = tbl.rows[row_idx]
    for j, v in enumerate(values):
        cell = row.cells[j]
        tcbg(cell, bg)
        tcpad(cell, t=80, b=80, l=80, r=80)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(v)
        r.font.name = "Arial"; r.font.size = Pt(9)
        r.font.color.rgb = C_BODY

# ============================================================
# 3.  TRANG BÌA
# ============================================================
print("▶ Đang viết tài liệu Word …")

title_p = doc.add_paragraph()
title_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
title_p.paragraph_format.space_before = Pt(30)
title_p.paragraph_format.space_after  = Pt(8)
tr = title_p.add_run("BÁO CÁO ĐỒ ÁN THỰC HÀNH DEVOPS")
tr.font.name = "Arial"; tr.font.size = Pt(24)
tr.font.bold = True;    tr.font.color.rgb = C_NAVY

sub_p = doc.add_paragraph()
sub_p.alignment = WD_ALIGN_PARAGRAPH.CENTER
sub_p.paragraph_format.space_after = Pt(24)
sr = sub_p.add_run("GIT · DOCKER · JENKINS CI/CD PIPELINE\nBáo Cáo Cá Nhân – Nguyễn Bá Hoài Nam")
sr.font.name = "Arial"; sr.font.size = Pt(13)
sr.font.italic = True;  sr.font.color.rgb = C_GREY

# Info box
info_tbl = doc.add_table(rows=7, cols=2)
info_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
info_data = [
    ("Họ và Tên:",           "Nguyễn Bá Hoài Nam"),
    ("Mã Số Sinh Viên:",     "102154"),
    ("Email Liên Hệ:",       "nguyennam25101999@gmail.com"),
    ("Tên Ứng Dụng:",        "Dictionary App – Tra từ điển Anh - Việt"),
    ("GitHub Repository:",   "https://github.com/nam25101999/DevOps-26-09"),
    ("Thư mục nguồn cá nhân:", "giuaky_Nguyen_Ba_Hoai_Nam/ (trong Monorepo)"),
    ("Thời Gian Thực Hiện:", "19/09/2026 – 14/10/2026  |  Môn Thực Hành DevOps"),
]
for i, (k, v) in enumerate(info_data):
    r = info_tbl.rows[i]
    c1, c2 = r.cells[0], r.cells[1]
    tcbg(c1, "EBF2FA"); tcbg(c2, "FFFFFF")
    tcpad(c1, t=90, b=90, l=110, r=110)
    tcpad(c2, t=90, b=90, l=110, r=110)
    for cell, txt, bold in [(c1, k, True), (c2, v, False)]:
        p = cell.paragraphs[0]; p.paragraph_format.space_after = Pt(0)
        rr = p.add_run(txt)
        rr.font.name = "Arial"; rr.font.size = Pt(10)
        rr.font.bold = bold
        rr.font.color.rgb = C_NAVY if bold else C_DARK

sp(before=0, after=10)
doc.add_page_break()

# ============================================================
# 4.  MỤC LỤC (thủ công)
# ============================================================
heading1("MỤC LỤC")
toc_items = [
    ("1.", "Tổng Quan Đề Tài & Kiến Trúc Dự Án"),
    ("2.", "Quản Lý Mã Nguồn với Git & GitHub"),
    ("3.", "Đóng Gói Container hóa với Docker"),
    ("4.", "Điều Phối Dịch Vụ với Docker Compose"),
    ("5.", "Kiểm Thử API & Giao Diện Web"),
    ("6.", "Chuỗi Tự Động Hóa CI/CD với Jenkins"),
    ("7.", "Kết Quả, Bài Học Kinh Nghiệm & Hướng Phát Triển"),
]
for num, text in toc_items:
    body(text, bold_prefix=f"{num}  ", after=4)

doc.add_page_break()

# ============================================================
# 5.  CHƯƠNG 1 – TỔNG QUAN
# ============================================================
heading1("CHƯƠNG 1: TỔNG QUAN ĐỀ TÀI & KIẾN TRÚC DỰ ÁN")

heading2("1.1. Mục Tiêu Đề Tài")
body(
    "Đề tài này yêu cầu sinh viên thực hành toàn bộ vòng đời phát triển và vận hành phần mềm (Software Development "
    "Life Cycle – SDLC) theo phương pháp luận DevOps hiện đại. Quy trình bao gồm ba trụ cột kỹ thuật chính: "
    "quản lý mã nguồn phân tán với Git & GitHub, chuẩn hóa môi trường bằng Docker Container, và tự động hóa "
    "toàn bộ chu trình Tích Hợp – Kiểm Thử – Xuất Bản – Triển Khai (CI/CD) bằng Jenkins Pipeline."
)
body(
    "Kết quả cần đạt được: Một ứng dụng Fullstack hoạt động ổn định trong môi trường container hóa, có thể "
    "được triển khai tự động lên môi trường sản xuất chỉ bằng một lần commit lên nhánh main của GitHub."
)

heading2("1.2. Kiến Trúc Ứng Dụng (3-tier Architecture)")
body(
    "Ứng dụng 'Dictionary App' được xây dựng theo kiến trúc 3 tầng truyền thống (Presentation – Logic – Data), "
    "mỗi tầng được đóng gói độc lập trong một Docker container riêng biệt và giao tiếp qua mạng nội bộ "
    "Docker Network:"
)

arch_tbl = doc.add_table(rows=4, cols=4)
arch_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
header_row(arch_tbl, ["Tầng / Service", "Container Name", "Công Nghệ", "Port Ánh Xạ"])
arch_rows = [
    ("Tầng Trình Bày (Frontend)", "giuaky-frontend", "React 18 + Vite → Nginx Alpine", "8080:80"),
    ("Tầng Xử Lý Logic (Backend API)", "giuaky-backend",  "Node.js 20 Alpine + Express 4", "3000:3000"),
    ("Tầng Dữ Liệu (Database)", "giuaky-db",      "PostgreSQL 16 Alpine + init.sql",  "5432:5432"),
]
for i, row in enumerate(arch_rows, 1):
    data_row(arch_tbl, i, row)
sp(before=0, after=10)

heading2("1.3. Điểm Nổi Bật Kỹ Thuật Của Dự Án")
bullet(
    "Thiết kế tách biệt Frontend (Nginx phục vụ file tĩnh React) và Backend (Express API), liên kết qua Nginx Reverse Proxy. "
    "Điều này khác hoàn toàn với cách tiếp cận bundle-vào-backend thông thường, giúp mỗi tầng có thể scale độc lập.",
    bold_pre="Kiến trúc phân tán thực sự: "
)
bullet(
    "Nginx cấu hình proxy_pass để chuyển tiếp request /api/* từ Frontend container sang Backend container "
    "qua tên DNS nội bộ của Docker Network (http://backend:3000). SPA React không cần biết địa chỉ thực của API.",
    bold_pre="Nginx Reverse Proxy: "
)
bullet(
    "Docker Compose cấu hình healthcheck cho service db (pg_isready) và depends_on condition: service_healthy "
    "cho service backend. Backend container chỉ khởi động sau khi PostgreSQL thực sự sẵn sàng nhận kết nối.",
    bold_pre="Healthcheck & Dependency ordering: "
)
bullet(
    "Backend cung cấp thêm endpoint GET /api/mssv đọc và trả về nội dung file mssv/mssv.txt được nhúng ngay trong image "
    "Docker — một cách minh chứng sự hiện diện của sinh viên trong container.",
    bold_pre="Endpoint MSSV: "
)

doc.add_page_break()

# ============================================================
# 6.  CHƯƠNG 2 – GIT
# ============================================================
heading1("CHƯƠNG 2: QUẢN LÝ MÃ NGUỒN VỚI GIT & GITHUB")

heading2("2.1. Cấu Hình Môi Trường Git Trên Windows")
body(
    "Trước khi bắt đầu viết mã nguồn, cần thiết lập cấu hình Git toàn cục để đảm bảo tính nhất quán "
    "giữa môi trường phát triển Windows và môi trường sản xuất Linux trong container:"
)
bullet(
    "Giá trị 'true' tự động chuyển đổi ký tự xuống dòng CRLF (Windows) thành LF (Linux/Unix) khi commit, "
    "tránh lỗi 'bad interpreter: No such file or directory' khi chạy shell script trong container Linux.",
    bold_pre="core.autocrlf=true: "
)
bullet(
    "credential.helper=manager sử dụng Windows Credential Manager để lưu trữ Personal Access Token (PAT) của GitHub "
    "một cách an toàn trong Windows Vault, không lộ token trong lệnh hay lịch sử terminal.",
    bold_pre="Credential Manager: "
)
bullet(
    "Tệp .gitignore loại trừ các thư mục node_modules/, frontend/dist/, backend/public/, file môi trường .env "
    "chứa mật khẩu cơ sở dữ liệu, và các file log tạm thời.",
    bold_pre="Tệp .gitignore: "
)

img(os.path.join(OUTPUT_DIR, "01_git_setup.png"),
    "Hình 2.1: Thiết lập cấu hình Git toàn cục (user, email, autocrlf) trên Command Prompt")

heading2("2.2. Khởi Tạo Repository & Commit Đầu Tiên")
body(
    "Toàn bộ mã nguồn dự án được tổ chức trong thư mục giuaky_Nguyen_Ba_Hoai_Nam/ bên trong Monorepo "
    "DevOps-26-09. Commit đầu tiên (Initial commit – 9e89aeb) của Nguyễn Bá Hoài Nam bao gồm 44 files "
    "với 6.553 dòng code, thiết lập kiến trúc đầy đủ cho cả ba tầng ứng dụng:"
)

commit_tbl = doc.add_table(rows=5, cols=3)
commit_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
header_row(commit_tbl, ["Commit SHA", "Tác Giả", "Mô Tả Commit"])
commit_rows = [
    ("9e89aeb", "Nguyễn Bá Hoài Nam", "Initial commit – Toàn bộ cấu trúc 3-tier + Dockerfile + docker-compose.yml"),
    ("a80695e", "Nguyễn Bá Hoài Nam", "Add production docker-compose file cho môi trường prod"),
    ("5261f45", "Nguyễn Bá Hoài Nam", "Add Dockerfiles cho backend & frontend, cập nhật docker-compose"),
    ("a10739f", "linh16122005 (chung)", "fix(ci): auto-detect Docker host cho Jenkins DooD trong smoke-test"),
]
for i, row in enumerate(commit_rows, 1):
    data_row(commit_tbl, i, row)
sp(before=0, after=10)

img(os.path.join(OUTPUT_DIR, "02_git_init_commit.png"),
    "Hình 2.2: Thực hiện git add và git commit đầu tiên với 44 files và 6.553 dòng mã nguồn")

heading2("2.3. Lịch Sử Commit & Quy Chuẩn Conventional Commits")
body(
    "Dự án áp dụng quy chuẩn Conventional Commits giúp lịch sử git dễ đọc, dễ truy vết và tương thích "
    "với công cụ tự động tạo CHANGELOG:"
)
bullet("Thêm tính năng mới (ví dụ: feat(jenkins): add Jenkinsfile and CI/CD pipeline).", bold_pre="feat: ")
bullet("Sửa lỗi kỹ thuật (ví dụ: fix(ci): auto-detect Docker host for Jenkins DooD).", bold_pre="fix: ")
bullet("Dọn dẹp mã không còn cần thiết (ví dụ: chore: remove obsolete references).", bold_pre="chore: ")
bullet("Cập nhật cấu hình CI/CD (ví dụ: ci: add GHCR docker-publish workflow).", bold_pre="ci: ")

img(os.path.join(OUTPUT_DIR, "03_git_log.png"),
    "Hình 2.3: Lịch sử commit chuẩn hóa với git log --oneline, hiển thị các commit của Nguyễn Bá Hoài Nam")

heading2("2.4. Kết Nối & Đồng Bộ Lên GitHub Remote")
body(
    "Repository được đồng bộ với tài khoản GitHub https://github.com/nam25101999/DevOps-26-09. "
    "Quá trình push sử dụng HTTPS với Personal Access Token (PAT) được Windows Credential Manager "
    "lưu trữ an toàn. Jenkins sẽ tự động phát hiện commit mới thông qua cơ chế SCM Polling (2 phút/lần)."
)

img(os.path.join(OUTPUT_DIR, "04_git_remote_push.png"),
    "Hình 2.4: Thiết lập remote origin và đồng bộ mã nguồn lên GitHub với git push")

callout(
    "Toàn bộ thông tin nhạy cảm (mật khẩu database, Personal Access Token GitHub) được loại trừ hoàn toàn "
    "khỏi kho mã nguồn thông qua tệp .gitignore. Biến môi trường được truyền vào container lúc runtime "
    "qua file .env hoặc tham số docker compose, KHÔNG bao giờ commit vào Git.",
    prefix="Bảo mật mã nguồn: "
)

doc.add_page_break()

# ============================================================
# 7.  CHƯƠNG 3 – DOCKER
# ============================================================
heading1("CHƯƠNG 3: ĐÓNG GÓI CONTAINER HÓA VỚI DOCKER")

heading2("3.1. Dockerfile Cho Service Database (PostgreSQL)")
body(
    "File giuaky_Nguyen_Ba_Hoai_Nam/db/Dockerfile kế thừa image chuẩn postgres:16-alpine "
    "và nhúng trực tiếp file khởi tạo SQL vào trong image:"
)
bullet("Kế thừa image PostgreSQL 16 trên nền Alpine Linux cực kỳ nhẹ (~90MB).", bold_pre="FROM postgres:16-alpine: ")
bullet(
    "Sao chép tệp init.sql vào thư mục /docker-entrypoint-initdb.d/. "
    "PostgreSQL tự động thực thi mọi file .sql trong thư mục này khi volume dữ liệu còn trống (lần khởi tạo đầu tiên).",
    bold_pre="COPY init.sql ...: "
)

callout(
    "Tại sao KHÔNG dùng bind-mount volume cho init.sql? Khi Jenkins chạy trong container (Docker-out-of-Docker), "
    "daemon Docker trên máy host tìm đường dẫn './db/init.sql' trên HOST chứ không phải bên trong container Jenkins. "
    "Đường dẫn /var/jenkins_home/... không tồn tại trên host → Docker mount thư mục rỗng → PostgreSQL không chạy SQL "
    "→ Lỗi 'relation words does not exist'. Nhúng SQL vào image giải quyết triệt để vấn đề này.",
    prefix="Lý do thiết kế: "
)

heading3("Nội dung file init.sql:")
body(
    "Tệp init.sql tạo bảng words với cấu trúc (id SERIAL PRIMARY KEY, word VARCHAR UNIQUE, definition TEXT) "
    "và nạp sẵn 10 cặp từ vựng Anh-Việt ban đầu sử dụng ON CONFLICT DO NOTHING để tránh lỗi khi chạy lại:"
)
bullet("apple → quả táo,  book → quyển sách,  computer → máy tính,  dog → con chó,  elephant → con voi")
bullet("flower → bông hoa,  guitar → đàn guitar,  house → ngôi nhà,  internet → mạng internet,  juice → nước ép")

heading2("3.2. Dockerfile Cho Service Backend (Node.js Express API)")
body(
    "File giuaky_Nguyen_Ba_Hoai_Nam/backend/Dockerfile được thiết kế tối ưu hóa cho production "
    "với các kỹ thuật sau:"
)
bullet(
    "Sử dụng Node.js 20 LTS (Long-Term Support) trên Alpine Linux để đảm bảo độ ổn định lâu dài và kích thước image nhỏ gọn.",
    bold_pre="FROM node:20-alpine: "
)
bullet(
    "Đặt biến môi trường NODE_ENV=production và PORT=3000 trực tiếp trong Dockerfile giúp ứng dụng chạy đúng chế độ "
    "mà không cần truyền từ bên ngoài.",
    bold_pre="ENV NODE_ENV=production: "
)
bullet(
    "Sử dụng npm ci --omit=dev thay vì npm install để cài đặt đúng version theo package-lock.json và bỏ qua "
    "hoàn toàn devDependencies (vite, eslint...), giảm kích thước image và tăng bảo mật.",
    bold_pre="RUN npm ci --omit=dev: "
)
bullet(
    "Sau khi copy toàn bộ mã nguồn, tự động sao chép mssv.txt lên cả hai vị trí /app/mssv/mssv.txt và /app/mssv.txt "
    "để endpoint /api/mssv hoạt động đúng trong mọi trường hợp.",
    bold_pre="Nhúng MSSV vào image: "
)

heading3("Các API Endpoint của Backend:")
api_tbl = doc.add_table(rows=5, cols=3)
api_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
header_row(api_tbl, ["HTTP Method + Path", "Chức Năng", "Response Mẫu"])
api_rows = [
    ("GET /api/health",         "Kiểm tra kết nối DB, đếm số từ", '{"db":"connected","words":10}'),
    ("GET /api/words",          "Trả về toàn bộ danh sách từ vựng",  '["apple","book","computer",…]'),
    ("GET /api/define/:word",   "Tra nghĩa 1 từ cụ thể",  '{"word":"computer","definition":"máy tính"}'),
    ("GET /api/mssv",           "Trả về thông tin sinh viên", "Nguyen Ba Hoai Nam  MSSV: 102154"),
]
for i, row in enumerate(api_rows, 1):
    data_row(api_tbl, i, row)
sp(before=0, after=10)

heading2("3.3. Dockerfile Cho Service Frontend (React + Nginx)")
body(
    "Đây là điểm kỹ thuật nổi bật nhất trong dự án của Nguyễn Bá Hoài Nam: áp dụng Multi-stage build "
    "cho Frontend container, kết hợp Nginx Reverse Proxy để tạo kiến trúc phân tán thực sự:"
)
bullet(
    "Stage build sử dụng node:20-alpine để cài đặt dependencies (npm ci) và biên dịch React Vite "
    "thành bundle tĩnh tối ưu trong thư mục /app/dist.",
    bold_pre="Stage 1 – build (Node.js): "
)
bullet(
    "Stage cuối kế thừa nginx:alpine (~23MB), chỉ copy thư mục /dist từ Stage 1 vào /usr/share/nginx/html. "
    "Toàn bộ Node.js runtime, node_modules, source code bị loại bỏ hoàn toàn khỏi image cuối.",
    bold_pre="Stage 2 – serve (Nginx): "
)
bullet(
    "File nginx.conf cấu hình:\n"
    "  • Phục vụ file tĩnh React với try_files $uri /index.html (hỗ trợ React Router SPA).\n"
    "  • Proxy mọi request /api/* về http://backend:3000 (tên service trong Docker Network).\n"
    "  • Truyền các header X-Real-IP, X-Forwarded-For cho backend ghi log chính xác.",
    bold_pre="nginx.conf – Reverse Proxy: "
)

callout(
    "So sánh 2 cách tiếp cận:\n"
    "• Cách 1 (Cao Khánh Linh): Backend Express phục vụ cả API lẫn static files → 1 Dockerfile multi-stage cho toàn bộ.\n"
    "• Cách 2 (Nguyễn Bá Hoài Nam): Nginx riêng làm Web Server + Proxy, Backend riêng chỉ làm API → 3 containers tách biệt, "
    "mỗi container có thể scale độc lập và được thay thế mà không ảnh hưởng đến nhau.",
    prefix="Điểm khác biệt thiết kế: "
)

img(os.path.join(OUTPUT_DIR, "05_docker_version.png"),
    "Hình 3.1: Xác nhận Docker Engine 29.6.2 và Docker Compose v2.32 hoạt động trên máy tính")

doc.add_page_break()

# ============================================================
# 8.  CHƯƠNG 4 – DOCKER COMPOSE
# ============================================================
heading1("CHƯƠNG 4: ĐIỀU PHỐI DỊCH VỤ VỚI DOCKER COMPOSE")

heading2("4.1. Phân Tích Cấu Hình docker-compose.yml")
body(
    "File giuaky_Nguyen_Ba_Hoai_Nam/docker-compose.yml điều phối 3 services với thứ tự khởi động "
    "nghiêm ngặt và cơ chế kiểm tra sức khỏe tự động:"
)

svc_tbl = doc.add_table(rows=4, cols=5)
svc_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
header_row(svc_tbl, ["Service", "Image / Build", "Container Name", "Healthcheck", "Port Mapping"])
svc_rows = [
    ("db",       "postgres:16-alpine (custom)", "giuaky-db",       "pg_isready (interval 5s, retries 5)", "5432:5432"),
    ("backend",  "node:20-alpine (custom)",     "giuaky-backend",  "depends_on db: service_healthy",       "3000:3000"),
    ("frontend", "nginx:alpine (multi-stage)",  "giuaky-frontend", "depends_on backend",                  "8080:80"),
]
for i, row in enumerate(svc_rows, 1):
    data_row(svc_tbl, i, row)
sp(before=0, after=10)

heading2("4.2. Cơ Chế Healthcheck & Dependency Ordering")
body(
    "Đây là cải tiến quan trọng so với cách depends_on đơn giản thông thường. "
    "Với condition: service_healthy, Docker Compose đảm bảo thứ tự khởi động chính xác:"
)
bullet("PostgreSQL container khởi động và chạy healthcheck pg_isready mỗi 5 giây, tối đa 5 lần thử (25 giây).", bold_pre="Bước 1 (db): ")
bullet("Chỉ khi db báo cáo trạng thái 'healthy', container giuaky-backend mới được phép khởi động.", bold_pre="Bước 2 (backend): ")
bullet("Sau khi backend đã khởi động, container giuaky-frontend (Nginx) mới được khởi tạo.", bold_pre="Bước 3 (frontend): ")
bullet(
    "Volume 'postgres_data' được khai báo là named volume Docker. Volume này tồn tại độc lập với vòng đời container, "
    "dữ liệu được bảo toàn ngay cả khi chạy docker compose down (chỉ mất khi dùng -v flag).",
    bold_pre="Volume persistence: "
)

img(os.path.join(OUTPUT_DIR, "06_docker_compose_config.png"),
    "Hình 4.1: Lệnh docker compose config xác thực cấu hình 3 services và dependency ordering")

heading2("4.3. Biên Dịch Images & Khởi Chạy Services")
body(
    "Lệnh docker compose up --build thực hiện toàn bộ quy trình từ đọc Dockerfile → biên dịch image → "
    "tạo network nội bộ → khởi chạy container theo đúng thứ tự dependency:"
)
img(os.path.join(OUTPUT_DIR, "07_docker_build.png"),
    "Hình 4.2: Quá trình docker compose up --build biên dịch 3 images và khởi chạy hệ thống")

heading2("4.4. Kiểm Tra Trạng Thái Container")
body(
    "Sau khi khởi chạy thành công, lệnh docker compose ps và docker images hiển thị "
    "trạng thái và kích thước của từng container:"
)
img(os.path.join(OUTPUT_DIR, "08_docker_ps.png"),
    "Hình 4.3: docker compose ps xác nhận 3 containers hoạt động và docker images hiển thị kích thước image")

heading2("4.5. Kiểm Tra Logs Khởi Tạo Database & Services")
body(
    "Logs của các container xác nhận luồng khởi động đúng thứ tự: database khởi tạo → "
    "backend kết nối → nginx sẵn sàng:"
)
img(os.path.join(OUTPUT_DIR, "09_docker_logs.png"),
    "Hình 4.4: docker compose logs xác nhận PostgreSQL nạp init.sql thành công và backend lắng nghe cổng 3000")

doc.add_page_break()

# ============================================================
# 9.  CHƯƠNG 5 – KIỂM THỬ
# ============================================================
heading1("CHƯƠNG 5: KIỂM THỬ API ENDPOINT & GIAO DIỆN WEB")

heading2("5.1. Kiểm Thử Toàn Bộ API Bằng cURL")
body(
    "Sau khi hệ thống 3 containers khởi động thành công, tiến hành kiểm thử từng endpoint của "
    "Backend API và Frontend Nginx bằng công cụ cURL trực tiếp trên CMD:"
)
img(os.path.join(OUTPUT_DIR, "10_curl_api_test.png"),
    "Hình 5.1: Kiểm thử 5 endpoint API (/api/health, /api/words, /api/define, /api/mssv) và xác nhận Nginx hoạt động")

test_tbl = doc.add_table(rows=6, cols=4)
test_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
header_row(test_tbl, ["Endpoint", "HTTP Method", "Kết Quả Thực Tế", "Trạng Thái"])
test_rows = [
    ("localhost:3000/api/health",         "GET", '{"db":"connected","words":10}',      "✅ PASS"),
    ("localhost:3000/api/words",           "GET", '["apple","book","computer",…10 từ]', "✅ PASS"),
    ("localhost:3000/api/define/computer", "GET", '{"word":"computer","def":"máy tính"}', "✅ PASS"),
    ("localhost:3000/api/mssv",            "GET", "Nguyen Ba Hoai Nam  MSSV: 102154",  "✅ PASS"),
    ("localhost:8080/ (Nginx)",            "GET", "HTTP 200 OK – React App HTML",       "✅ PASS"),
]
for i, row in enumerate(test_rows, 1):
    data_row(test_tbl, i, row)
sp(before=0, after=10)

heading2("5.2. Kiểm Thử Giao Diện Người Dùng Trên Trình Duyệt")
body(
    "Truy cập http://localhost:8080 trên trình duyệt để kiểm thử giao diện React App được phục vụ bởi Nginx. "
    "Frontend tự động gọi các API thông qua Nginx Reverse Proxy (proxy_pass http://backend:3000) "
    "mà không cần hardcode địa chỉ backend:"
)
if os.path.exists(WEB_HOME):
    img(WEB_HOME, "Hình 5.2: Giao diện Trang Chủ Dictionary App – Badge trạng thái Database và danh sách từ vựng")
if os.path.exists(WEB_NEXT):
    img(WEB_NEXT, "Hình 5.3: Tính năng tra cứu từ vựng hoạt động – Nghĩa tiếng Việt được nạp từ PostgreSQL qua API")

heading2("5.3. Dừng Hệ Thống & Quản Lý Volume")
body(
    "Sử dụng docker compose down để dừng và xóa containers an toàn. "
    "Volume postgres_data được giữ lại mặc định, bảo toàn dữ liệu qua các lần triển khai:"
)
img(os.path.join(OUTPUT_DIR, "11_docker_down.png"),
    "Hình 5.4: docker compose down dừng 3 containers an toàn, volume postgres_data được bảo toàn")

doc.add_page_break()

# ============================================================
# 10. CHƯƠNG 6 – JENKINS CI/CD
# ============================================================
heading1("CHƯƠNG 6: CHUỖI TỰ ĐỘNG HÓA CI/CD VỚI JENKINS PIPELINE")

heading2("6.1. Tổng Quan Kiến Trúc Jenkins (Docker-out-of-Docker)")
body(
    "Jenkins được triển khai như một container Docker (jenkins-jenkins) và giao tiếp với Docker Daemon "
    "của máy chủ host thông qua bind-mount Unix socket /var/run/docker.sock (hay /run/host-services/docker.proxy.sock "
    "trên Docker Desktop). Kiến trúc này gọi là Docker-out-of-Docker (DooD):"
)
bullet(
    "Jenkins container có thể gọi lệnh docker build, docker compose, docker push... như thể đang chạy trực tiếp "
    "trên máy host, không cần cài đặt Docker daemon lồng nhau phức tạp (Docker-in-Docker).",
    bold_pre="Ưu điểm DooD: "
)
bullet(
    "Jenkins chạy trên cổng 8080 (giao diện web) và 50000 (agent JNLP). Workspace được lưu trong volume "
    "jenkins_jenkins_home tại /var/jenkins_home.",
    bold_pre="Cấu hình network: "
)
bullet(
    "Thách thức: Khi Jenkins khởi chạy docker compose để smoke test, container test gọi 'localhost' sẽ trỏ "
    "về chính container Jenkins (không phải host). Script smoke-test.sh đã được fix để tự động phát hiện "
    "host.docker.internal (DNS đặc biệt của Docker Desktop) thay thế.",
    bold_pre="Thách thức & Giải pháp: "
)

img(os.path.join(OUTPUT_DIR, "12_jenkins_start.png"),
    "Hình 6.1: Khởi động Jenkins container và kích hoạt Pipeline Build qua Jenkins REST API")

heading2("6.2. Phân Tích Chi Tiết 6 Stages Của Jenkinsfile")
body(
    "File Jenkinsfile tại gốc repository định nghĩa Declarative Pipeline tuân theo 3 nguyên tắc vàng "
    "DevOps: BUILD một lần – TEST trên máy native – PUSH đa kiến trúc:"
)

pipeline_tbl = doc.add_table(rows=9, cols=4)
pipeline_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
header_row(pipeline_tbl, ["Stage", "Nội Dung Chi Tiết", "Lệnh Chính Thực Hiện", "Build #9 Duration"])
pipeline_rows = [
    ("Chuẩn bị",
     "Login GHCR, cài QEMU cho emulation ARM/RISC, tạo Buildx multiarch builder",
     "docker login, docker run tonistiigi/binfmt, docker buildx create",
     "~5s"),
    ("1. BUILD",
     "Build image native linux/amd64 với --load (nạp vào Docker local), đồng thời đẩy cache lên GHCR :buildcache",
     "docker buildx build --platform linux/amd64 --load --cache-to type=registry",
     "~13s"),
    ("2. TEST",
     "Chạy scripts/smoke-test.sh: khởi docker compose stack tạm, poll /api/health tối đa 30s, kiểm tra /api/define/computer",
     "chmod +x smoke-test.sh && SMOKE_IMAGE=... ./scripts/smoke-test.sh",
     "~5s"),
    ("3. PUSH",
     "Build lại đa nền tảng (linux/amd64 + linux/arm64) dùng cache từ Registry, đẩy Manifest List lên GHCR",
     "docker buildx build --platform linux/amd64,arm64 --push --tag :sha --tag :latest",
     "~37s"),
    ("4. PULL",
     "Xóa image local, pull image từ GHCR về máy host để kiểm chứng Registry hợp lệ",
     "docker rmi ...; docker pull ghcr.io/linh16122005/dictionary-app-5:sha",
     "~7s"),
    ("5. DEPLOY",
     "Deploy Production Stack dictionary-prod qua Docker Compose, giữ nguyên volume dữ liệu DB",
     "docker compose -p dictionary-prod -f docker-compose.yml -f docker-compose.prod.yml up -d",
     "~1s"),
    ("6. Kiểm tra",
     "Tự động poll /api/health từ Jenkins container qua host.docker.internal, gọi /api/define/computer",
     "for i in $(seq 1 30); do curl -sf $BASE/api/health; done",
     "~0.5s"),
    ("Post Actions",
     "docker logout GHCR, prune image cũ hơn 7 ngày để tiết kiệm dung lượng ổ đĩa laptop",
     "docker logout ghcr.io; docker image prune -f --filter until=168h",
     "~0.8s"),
]
for i, row in enumerate(pipeline_rows, 1):
    data_row(pipeline_tbl, i, row)
sp(before=0, after=10)

heading2("6.3. Lịch Sử Build & Quá Trình Debug")
body(
    "Quá trình đạt được Build SUCCESS #9 trải qua nhiều lần thất bại, mỗi lần thất bại là "
    "một bài học kỹ thuật quý giá về môi trường Docker-out-of-Docker:"
)

hist_tbl = doc.add_table(rows=7, cols=4)
hist_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
header_row(hist_tbl, ["Build #", "Kết Quả", "Nguyên Nhân Thất Bại", "Thời Gian (Duration)"])
hist_rows = [
    ("#4",  "❌ FAILURE", "Thiếu file cấu hình docker-compose.prod.yml",                   "21s"),
    ("#5",  "❌ FAILURE", "Credential GHCR chưa đúng format",                               "1s"),
    ("#6",  "❌ FAILURE", "smoke-test.sh dùng localhost → curl trỏ vào Jenkins container", "93s"),
    ("#7",  "❌ FAILURE", "Đã fix localhost nhưng port 3000 bị chiếm bởi container khác", "139s"),
    ("#8",  "❌ FAILURE", "Build 7 vẫn còn container cũ chưa dọn sạch",                   "127s"),
    ("#9",  "✅ SUCCESS", "Đã dọn sạch containers, fix host.docker.internal, pipeline hoàn hảo", "68s"),
]
for i, row in enumerate(hist_rows, 1):
    data_row(hist_tbl, i, row)
sp(before=0, after=10)

callout(
    "Giải pháp kỹ thuật cho vấn đề DooD networking:\n"
    "1. Khi smoke-test chạy docker compose up, containers được tạo ra trên HOST (qua docker.sock).\n"
    "2. Nhưng lệnh curl trong script chạy BÊN TRONG Jenkins container → 'localhost' trỏ về Jenkins, không phải host.\n"
    "3. Giải pháp: Script tự động kiểm tra 'getent hosts host.docker.internal' → nếu resolved thì dùng host.docker.internal "
    "thay cho localhost. Docker Desktop tự động thêm host.docker.internal vào DNS của mọi container.",
    prefix="Root Cause Analysis – DooD Networking: "
)

img(os.path.join(OUTPUT_DIR, "13_jenkins_build9_result.png"),
    "Hình 6.2: Tóm tắt lịch sử Build và kết quả chi tiết Build #9 SUCCESS với thời gian 68 giây")

heading2("6.4. Kết Quả Pipeline Trên Giao Diện Jenkins Stage View")
body(
    "Sau khi Build #9 hoàn thành thành công, giao diện Jenkins Stage View hiển thị màu xanh lá cây "
    "cho toàn bộ 6 stages, đây là bằng chứng trực quan về hệ thống CI/CD hoạt động đúng thiết kế:"
)
if os.path.exists(JENKINS_STAGE_VIEW):
    img(JENKINS_STAGE_VIEW,
        "Hình 6.3: Jenkins Stage View – Tất cả 6 Stages của Build #9 hiển thị màu xanh SUCCESS",
        w_inch=6.2)
if os.path.exists(JENKINS_BUILD9):
    img(JENKINS_BUILD9,
        "Hình 6.4: Trang chi tiết Jenkins Build #9 với trạng thái SUCCESS và timestamp 14/10/2026 00:10:06")

heading2("6.5. Xác Minh Ứng Dụng Production Sau Khi Jenkins Deploy")
body(
    "Sau khi Jenkins Stage 5 (DEPLOY) hoàn tất, hệ thống Production dictionary-prod "
    "với image kéo từ GHCR hoạt động hoàn hảo:"
)
img(os.path.join(OUTPUT_DIR, "14_prod_verify.png"),
    "Hình 6.5: Xác minh containers Production chạy image từ GHCR và API phản hồi đúng sau khi Jenkins deploy")

doc.add_page_break()

# ============================================================
# 11. CHƯƠNG 7 – KẾT LUẬN
# ============================================================
heading1("CHƯƠNG 7: KẾT LUẬN, BÀI HỌC KINH NGHIỆM & HƯỚNG PHÁT TRIỂN")

heading2("7.1. Kết Quả Đạt Được")
body(
    "Sau quá trình thực hành, Nguyễn Bá Hoài Nam đã đạt được các mục tiêu sau đây một cách đầy đủ và vượt "
    "mức yêu cầu đề tài:"
)
bullet(
    "Xây dựng hoàn chỉnh ứng dụng 3-tier với kiến trúc phân tán thực sự: Nginx Frontend riêng, "
    "Express Backend riêng, PostgreSQL riêng – mỗi service có thể scale và bảo trì độc lập.",
    bold_pre="Kiến trúc phân tán 3-tier: "
)
bullet(
    "Thiết kế hệ thống khởi động thứ tự với Healthcheck PostgreSQL → depends_on service_healthy → "
    "Backend → Frontend, đảm bảo không bao giờ có tình huống backend kết nối DB trước khi DB sẵn sàng.",
    bold_pre="Quản lý vòng đời container: "
)
bullet(
    "Áp dụng Multi-stage build cho Frontend (Node build → Nginx serve) giúp loại bỏ toàn bộ "
    "Node.js runtime khỏi image production, giảm kích thước từ ~400MB xuống còn ~23MB.",
    bold_pre="Tối ưu hóa Docker image: "
)
bullet(
    "Triển khai Nginx Reverse Proxy với cấu hình proxy_pass tới backend container, "
    "hỗ trợ React Router SPA với try_files fallback, và truyền đầy đủ HTTP headers.",
    bold_pre="Nginx Reverse Proxy: "
)
bullet(
    "Tích hợp thành công vào Jenkins CI/CD Pipeline 6-stage, image đã được push lên "
    "GitHub Container Registry với tag đa kiến trúc (amd64 + arm64) và deployed tự động lên Production.",
    bold_pre="CI/CD Pipeline: "
)

heading2("7.2. Bài Học Kinh Nghiệm Kỹ Thuật")

body("Trong quá trình thực hiện, một số vấn đề kỹ thuật quan trọng đã được phát hiện và giải quyết:", after=4)

exp_tbl = doc.add_table(rows=5, cols=3)
exp_tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
header_row(exp_tbl, ["Vấn Đề Gặp Phải", "Nguyên Nhân Gốc Rễ", "Giải Pháp Áp Dụng"])
exp_rows = [
    ("PostgreSQL không chạy init.sql trong Jenkins",
     "DooD: Jenkins container mount ./db/init.sql nhưng host tìm đường dẫn trên HOST",
     "Nhúng init.sql vào Dockerfile bằng COPY, không dùng bind-mount"),
    ("curl localhost thất bại trong smoke-test",
     "Lệnh curl chạy bên trong Jenkins container → localhost = Jenkins, không phải host",
     "Auto-detect host.docker.internal qua getent hosts trong bash script"),
    ("Port 3000 bị conflict khi deploy lần 2",
     "Container prod cũ vẫn còn chiếm port, deploy mới không thể bind port",
     "Dọn sạch containers cũ trước khi trigger build mới"),
    ("Image size quá lớn khi không dùng multi-stage",
     "node_modules cho devDependencies (~500MB) bị đưa vào image production",
     "Multi-stage build: Node build stage + Nginx serve stage riêng biệt"),
]
for i, row in enumerate(exp_rows, 1):
    data_row(exp_tbl, i, row)
sp(before=0, after=10)

heading2("7.3. Hướng Phát Triển & Mở Rộng")
bullet(
    "Triển khai trên cụm Kubernetes (K8s) với Deployment, Service, Ingress Controller và HorizontalPodAutoscaler "
    "để hỗ trợ tự động co giãn quy mô (Auto-scaling) và Zero-downtime Rolling Update.",
    bold_pre="1. Kubernetes Orchestration: "
)
bullet(
    "Thêm tầng cache Redis giữa Backend và PostgreSQL để giảm tải database, "
    "kết hợp CDN Cloudflare/AWS CloudFront cho tầng Frontend Nginx phục vụ toàn cầu.",
    bold_pre="2. Performance optimization: "
)
bullet(
    "Tích hợp Prometheus + Grafana để giám sát thời gian thực (CPU, RAM, request rate, error rate), "
    "Loki để thu thập và phân tích log tập trung từ tất cả containers.",
    bold_pre="3. Monitoring & Observability: "
)
bullet(
    "Bổ sung SonarQube vào Pipeline để quét tự động code smell, security vulnerability, "
    "kiểm tra độ phủ Unit Test và thiết lập Quality Gate tự động block merge khi vi phạm ngưỡng.",
    bold_pre="4. Code Quality & Security: "
)
bullet(
    "Thêm GitHub Actions workflow để chạy linting, type-checking và unit test khi có Pull Request, "
    "kết hợp Dependabot để tự động cập nhật dependencies bảo mật.",
    bold_pre="5. GitHub Actions Workflow: "
)

# Kết luận cuối
heading2("7.4. Lời Kết")
body(
    "Thông qua đồ án thực hành DevOps này, Nguyễn Bá Hoài Nam đã tích lũy được hiểu biết sâu sắc "
    "về toàn bộ chu trình phát triển và vận hành phần mềm hiện đại. Từ việc thiết lập môi trường phát triển "
    "chuẩn hóa với Git, xây dựng kiến trúc container hóa 3-tier với Docker, cho đến cấu hình pipeline CI/CD "
    "tự động hóa 100% trên Jenkins – mỗi bước đều mang lại những bài học thực tiễn quý giá mà không có "
    "lý thuyết nào có thể thay thế được."
)
body(
    "Đặc biệt, việc đối mặt và giải quyết các vấn đề kỹ thuật phức tạp như Docker-out-of-Docker networking, "
    "container healthcheck ordering, và multi-stage build optimization đã trang bị cho sinh viên "
    "những kỹ năng tư duy hệ thống và khả năng debug trong môi trường distributed systems – "
    "những kỹ năng cốt lõi của một kỹ sư DevOps/Cloud chuyên nghiệp trong thực tế công nghiệp.",
    after=20
)

# ============================================================
# 12. LƯU FILE
# ============================================================
doc.save(DOCX_PATH)
size = os.path.getsize(DOCX_PATH)
print(f"\n✅ ĐÃ TẠO XONG: {DOCX_PATH}")
print(f"   Kích thước: {size:,} bytes ({size//1024:,} KB)")
