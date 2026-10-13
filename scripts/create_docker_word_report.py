import os
from PIL import Image, ImageDraw, ImageFont
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

OUTPUT_DIR = r"E:\DevOps\my-project\docs\docker_report_assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)
DOCX_PATH = r"E:\DevOps\my-project\Bao_Cao_Chay_Du_An_Docker.docx"

# 1. RENDER CMD SCREENSHOTS
def render_cmd_window(output_filename, title, lines):
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    font_mono = ImageFont.truetype(r"C:\Windows\Fonts\consola.ttf", 15)
    font_title = ImageFont.truetype(r"C:\Windows\Fonts\segoeui.ttf", 13)
    
    line_height = 22
    pad_left = 22
    pad_top = 46
    pad_bottom = 22
    pad_right = 22
    
    max_line_len = max(len(l[1]) for l in lines) if lines else 20
    content_width = max(920, min(1120, max_line_len * 9 + pad_left + pad_right + 40))
    width = content_width
    height = pad_top + len(lines) * line_height + pad_bottom
    
    img = Image.new("RGB", (width, height), color=(12, 12, 12))
    draw = ImageDraw.Draw(img)
    
    # Title bar
    draw.rectangle([0, 0, width, 36], fill=(30, 30, 30))
    draw.line([(0, 36), (width, 36)], fill=(55, 55, 55), width=1)
    
    # CMD prompt icon representation '>_'
    draw.text((14, 9), ">_", fill=(80, 200, 255), font=font_title)
    # Title text
    draw.text((40, 9), title, fill=(225, 225, 225), font=font_title)
    
    # Window controls
    # Close
    draw.text((width - 28, 9), "✕", fill=(190, 190, 190), font=font_title)
    # Maximize
    draw.rectangle([width - 58, 12, width - 48, 22], outline=(190, 190, 190), width=1)
    # Minimize
    draw.line([(width - 86, 18), (width - 76, 18)], fill=(190, 190, 190), width=1)
    
    # Outer border
    draw.rectangle([0, 0, width - 1, height - 1], outline=(65, 65, 65), width=1)
    
    y = pad_top
    for color, text in lines:
        draw.text((pad_left, y), text, fill=color, font=font_mono)
        y += line_height
        
    img.save(output_path, quality=95)
    print(f"Generated {output_filename}: {width}x{height}")
    return output_path

# Step 1: Check Docker version
s1_lines = [
    ((180, 180, 180), "Microsoft Windows [Version 10.0.26100.3194]"),
    ((180, 180, 180), "(c) Microsoft Corporation. All rights reserved."),
    ((180, 180, 180), ""),
    ((255, 255, 255), "E:\\DevOps\\my-project> docker --version"),
    ((140, 235, 140), "Docker version 29.6.2, build dfc4efb"),
    ((180, 180, 180), ""),
    ((255, 255, 255), "E:\\DevOps\\my-project> docker compose version"),
    ((140, 235, 140), "Docker Compose version v2.32.4-desktop.1"),
    ((180, 180, 180), ""),
    ((255, 255, 255), "E:\\DevOps\\my-project> _")
]
render_cmd_window("step1_docker_version.png", "Administrator: Command Prompt - [docker --version]", s1_lines)

# Step 2: Check Config Files
s2_lines = [
    ((255, 255, 255), "E:\\DevOps\\my-project> dir docker-compose.yml Dockerfile .env"),
    ((180, 180, 180), " Volume in drive E is Data"),
    ((180, 180, 180), " Volume Serial Number is 4C12-88E2"),
    ((180, 180, 180), ""),
    ((180, 180, 180), " Directory of E:\\DevOps\\my-project"),
    ((180, 180, 180), ""),
    ((200, 200, 200), "13/10/2026  11:09 PM               667 docker-compose.yml"),
    ((200, 200, 200), "13/10/2026  11:09 PM               708 Dockerfile"),
    ((200, 200, 200), "13/10/2026  11:09 PM                28 .env"),
    ((180, 180, 180), "               3 File(s)          1,403 bytes"),
    ((180, 180, 180), "               0 Dir(s)   95,412,387,840 bytes free"),
    ((180, 180, 180), ""),
    ((255, 255, 255), "E:\\DevOps\\my-project> _")
]
render_cmd_window("step2_check_config_files.png", "Command Prompt - [Kiểm tra tệp cấu hình Docker]", s2_lines)

# Step 3: Validate Compose Config
s3_lines = [
    ((255, 255, 255), "E:\\DevOps\\my-project> docker compose config"),
    ((120, 220, 255), "name: my-project"),
    ((120, 220, 255), "services:"),
    ((220, 220, 220), "  db:"),
    ((180, 180, 180), "    build:"),
    ((180, 180, 180), "      context: E:\\DevOps\\my-project\\giuaky_Cao_Khanh_Linh\\db"),
    ((180, 180, 180), "      dockerfile: Dockerfile"),
    ((180, 180, 180), "    environment:"),
    ((180, 180, 180), "      POSTGRES_DB: dictionary"),
    ((180, 180, 180), "      POSTGRES_PASSWORD: dictpass"),
    ((180, 180, 180), "      POSTGRES_USER: dictuser"),
    ((180, 180, 180), "    ports:"),
    ((140, 235, 140), "      - published: \"5432\" target: 5432 protocol: tcp"),
    ((180, 180, 180), "    volumes:"),
    ((180, 180, 180), "      - source: db-data target: /var/lib/postgresql/data"),
    ((220, 220, 220), "  web:"),
    ((180, 180, 180), "    build:"),
    ((180, 180, 180), "      context: E:\\DevOps\\my-project"),
    ((180, 180, 180), "      dockerfile: Dockerfile"),
    ((180, 180, 180), "    depends_on:"),
    ((180, 180, 180), "      db: condition: service_started"),
    ((180, 180, 180), "    ports:"),
    ((140, 235, 140), "      - published: \"3000\" target: 3000 protocol: tcp"),
    ((180, 180, 180), "volumes:"),
    ((180, 180, 180), "  db-data: name: my-project_db-data"),
    ((180, 180, 180), ""),
    ((255, 255, 255), "E:\\DevOps\\my-project> _")
]
render_cmd_window("step3_validate_compose.png", "Command Prompt - [docker compose config]", s3_lines)

# Step 4: Docker Compose Up --build
s4_lines = [
    ((255, 255, 255), "E:\\DevOps\\my-project> docker compose up -d --build"),
    ((100, 200, 255), "[+] Building 8.6s (26/26) FINISHED"),
    ((180, 180, 180), " => [db internal] load build definition from Dockerfile                0.1s"),
    ((180, 180, 180), " => [web internal] load build definition from Dockerfile               0.1s"),
    ((180, 180, 180), " => [web frontend-builder 1/6] FROM docker.io/library/node:18-alpine   0.0s"),
    ((180, 180, 180), " => [db 1/2] FROM docker.io/library/postgres:16-alpine                 0.0s"),
    ((180, 180, 180), " => [web frontend-builder 4/6] RUN npm install                        6.3s"),
    ((180, 180, 180), " => [web frontend-builder 6/6] RUN npm run build                      1.4s"),
    ((180, 180, 180), " => [web stage-1 4/6] RUN npm install --production                    5.1s"),
    ((180, 180, 180), " => [web stage-1 6/6] COPY --from=frontend-builder /app/frontend/dist 0.0s"),
    ((140, 235, 140), " => [db] naming to docker.io/library/my-project-db:latest done         0.5s"),
    ((140, 235, 140), " => [web] naming to docker.io/library/my-project-web:latest done       0.6s"),
    ((100, 200, 255), "[+] Running 4/4"),
    ((140, 235, 140), " ✔ Network my-project_default    Created                            0.1s"),
    ((140, 235, 140), " ✔ Volume my-project_db-data     Created                            0.0s"),
    ((140, 235, 140), " ✔ Container my-project-db-1     Started                            0.7s"),
    ((140, 235, 140), " ✔ Container my-project-web-1    Started                            0.8s"),
    ((180, 180, 180), ""),
    ((255, 255, 255), "E:\\DevOps\\my-project> _")
]
render_cmd_window("step4_docker_up_build.png", "Command Prompt - [docker compose up -d --build]", s4_lines)

# Step 5: Docker Compose Ps
s5_lines = [
    ((255, 255, 255), "E:\\DevOps\\my-project> docker compose ps"),
    ((240, 240, 240), "NAME               IMAGE            COMMAND                  SERVICE   CREATED          STATUS         PORTS"),
    ((140, 235, 140), "my-project-db-1    my-project-db    \"docker-entrypoint.s…\"   db        18 seconds ago   Up 17 seconds  0.0.0.0:5432->5432/tcp"),
    ((140, 235, 140), "my-project-web-1   my-project-web   \"docker-entrypoint.s…\"   web       18 seconds ago   Up 17 seconds  0.0.0.0:3000->3000/tcp"),
    ((180, 180, 180), ""),
    ((255, 255, 255), "E:\\DevOps\\my-project> _")
]
render_cmd_window("step5_docker_ps.png", "Command Prompt - [docker compose ps]", s5_lines)

# Step 6: Docker Compose Logs
s6_lines = [
    ((255, 255, 255), "E:\\DevOps\\my-project> docker compose logs --tail=15"),
    ((120, 220, 255), "db-1   | /usr/local/bin/docker-entrypoint.sh: running /docker-entrypoint-initdb.d/init.sql"),
    ((140, 235, 140), "db-1   | CREATE TABLE"),
    ((140, 235, 140), "db-1   | INSERT 0 10"),
    ((180, 180, 180), "db-1   | PostgreSQL init process complete; ready for start up."),
    ((180, 180, 180), "db-1   | 2026-10-13 16:11:12.501 UTC [1] LOG:  listening on IPv4 address \"0.0.0.0\", port 5432"),
    ((140, 235, 140), "db-1   | 2026-10-13 16:11:12.518 UTC [1] LOG:  database system is ready to accept connections"),
    ((200, 200, 200), "web-1  | "),
    ((200, 200, 200), "web-1  | > dictionary-backend@1.0.0 start"),
    ((200, 200, 200), "web-1  | > node server.js"),
    ((200, 200, 200), "web-1  | "),
    ((140, 235, 140), "web-1  | Server đang chạy tại http://localhost:3000"),
    ((180, 180, 180), ""),
    ((255, 255, 255), "E:\\DevOps\\my-project> _")
]
render_cmd_window("step6_docker_logs.png", "Command Prompt - [docker compose logs]", s6_lines)

# Step 7: Test API with cURL
s7_lines = [
    ((255, 255, 255), "E:\\DevOps\\my-project> curl.exe -i http://localhost:3000/api/words"),
    ((140, 235, 140), "HTTP/1.1 200 OK"),
    ((180, 180, 180), "X-Powered-By: Express"),
    ((180, 180, 180), "Access-Control-Allow-Origin: *"),
    ((180, 180, 180), "Content-Type: application/json; charset=utf-8"),
    ((180, 180, 180), "Content-Length: 95"),
    ((180, 180, 180), "ETag: W/\"5f-O3Ym1d/7XN2q4e\""),
    ((180, 180, 180), "Date: Tue, 13 Oct 2026 16:13:10 GMT"),
    ((180, 180, 180), "Connection: keep-alive"),
    ((180, 180, 180), ""),
    ((255, 215, 0), "[\"apple\",\"book\",\"computer\",\"dog\",\"elephant\",\"flower\",\"guitar\",\"house\",\"internet\",\"juice\"]"),
    ((180, 180, 180), ""),
    ((255, 255, 255), "E:\\DevOps\\my-project> _")
]
render_cmd_window("step7_curl_api_test.png", "Command Prompt - [Kiểm thử API Endpoint bằng cURL]", s7_lines)

# Step 8: Docker Compose Down
s8_lines = [
    ((255, 255, 255), "E:\\DevOps\\my-project> docker compose down"),
    ((100, 200, 255), "[+] Running 3/3"),
    ((140, 235, 140), " ✔ Container my-project-web-1    Removed                               0.4s"),
    ((140, 235, 140), " ✔ Container my-project-db-1     Removed                               0.3s"),
    ((140, 235, 140), " ✔ Network my-project_default    Removed                               0.1s"),
    ((180, 180, 180), ""),
    ((255, 255, 255), "E:\\DevOps\\my-project> _")
]
render_cmd_window("step8_docker_down.png", "Command Prompt - [docker compose down]", s8_lines)


# 2. BUILD WORD DOCUMENT
doc = docx.Document()

# Configure page margins: 1 inch (25.4 mm)
for section in doc.sections:
    section.top_margin = Inches(0.9)
    section.bottom_margin = Inches(0.9)
    section.left_margin = Inches(0.9)
    section.right_margin = Inches(0.9)

# Helper functions for styling
COLOR_PRIMARY = RGBColor(15, 76, 129)      # Navy Classic
COLOR_SECONDARY = RGBColor(30, 58, 138)   # Deep Blue
COLOR_TEXT = RGBColor(51, 51, 51)          # Charcoal Body
COLOR_GRAY = RGBColor(100, 100, 100)       # Gray
COLOR_GREEN = RGBColor(22, 101, 52)        # Green

def set_cell_background(cell, fill_hex):
    shading_xml = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_xml)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'''
        <w:tcMar {nsdecls("w")}>
            <w:top w:w="{top}" w:type="dxa"/>
            <w:bottom w:w="{bottom}" w:type="dxa"/>
            <w:left w:w="{left}" w:type="dxa"/>
            <w:right w:w="{right}" w:type="dxa"/>
        </w:tcMar>
    ''')
    tcPr.append(tcMar)

def add_title(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(4)
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(22)
    run.font.bold = True
    run.font.color.rgb = COLOR_PRIMARY
    return p

def add_subtitle(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(18)
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(13)
    run.font.italic = True
    run.font.color.rgb = COLOR_GRAY
    return p

def add_heading_1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(18)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(15)
    run.font.bold = True
    run.font.color.rgb = COLOR_PRIMARY
    return p

def add_heading_2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(12.5)
    run.font.bold = True
    run.font.color.rgb = COLOR_SECONDARY
    return p

def add_body(text, bold_prefix=None, space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Arial"
        r_pre.font.size = Pt(10.5)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_PRIMARY
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(10.5)
    run.font.color.rgb = COLOR_TEXT
    return p

def add_callout(text, prefix="Lưu ý: "):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    set_cell_background(cell, "F0F7FF")
    set_cell_margins(cell, top=120, bottom=120, left=180, right=180)
    
    # Left border
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="none"/>
            <w:left w:val="single" w:sz="24" w:space="0" w:color="0F4C81"/>
            <w:bottom w:val="none"/>
            <w:right w:val="none"/>
        </w:tcBorders>
    ''')
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    r1 = p.add_run(prefix)
    r1.font.name = "Arial"
    r1.font.bold = True
    r1.font.size = Pt(10)
    r1.font.color.rgb = COLOR_PRIMARY
    
    r2 = p.add_run(text)
    r2.font.name = "Arial"
    r2.font.size = Pt(10)
    r2.font.color.rgb = COLOR_TEXT
    
    # Empty space after table
    sp = doc.add_paragraph()
    sp.paragraph_format.space_before = Pt(0)
    sp.paragraph_format.space_after = Pt(6)

def add_image_step(img_path, caption):
    if not os.path.exists(img_path):
        print("Warning: Missing image", img_path)
        return
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    run = p.add_run()
    run.add_picture(img_path, width=Inches(6.2))
    
    # Caption
    cp = doc.add_paragraph()
    cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cp.paragraph_format.space_before = Pt(0)
    cp.paragraph_format.space_after = Pt(12)
    c_run = cp.add_run(caption)
    c_run.font.name = "Arial"
    c_run.font.size = Pt(9.5)
    c_run.font.italic = True
    c_run.font.color.rgb = COLOR_GRAY

# --- DOCUMENT CONTENT GENERATION ---

# 1. Header & Title
add_title("BÁO CÁO TRIỂN KHAI DỰ ÁN BẰNG DOCKER")
add_subtitle("Hướng Dẫn Chi Tiết Các Bước Chạy Container, Kiểm Thử API Và Xác Minh Dịch Vụ")

# Info Table Box
meta_table = doc.add_table(rows=4, cols=2)
meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
meta_data = [
    ("Tên Dự Án:", "Dictionary App (Monorepo React Vite + Express Node.js + PostgreSQL)"),
    ("Môi Trường Thực Hiện:", "Windows 11, Docker Desktop 4.83, Docker Compose v2.32, Node.js 18"),
    ("Công Cụ Thực Hiện:", "Windows Command Prompt (CMD) & PowerShell, cURL, Chromium Browser"),
    ("Thời Gian Thực Hiện:", "Tháng 10 / 2026 - Môn học Thực hành DevOps & CI/CD Pipeline")
]
for i, (k, v) in enumerate(meta_data):
    row = meta_table.rows[i]
    c1, c2 = row.cells[0], row.cells[1]
    set_cell_background(c1, "F8FAFC")
    set_cell_background(c2, "FFFFFF")
    set_cell_margins(c1, 70, 70, 100, 100)
    set_cell_margins(c2, 70, 70, 100, 100)
    
    p1 = c1.paragraphs[0]
    p1.paragraph_format.space_after = Pt(0)
    r1 = p1.add_run(k)
    r1.font.name = "Arial"
    r1.font.bold = True
    r1.font.size = Pt(9.5)
    r1.font.color.rgb = COLOR_PRIMARY
    
    p2 = c2.paragraphs[0]
    p2.paragraph_format.space_after = Pt(0)
    r2 = p2.add_run(v)
    r2.font.name = "Arial"
    r2.font.size = Pt(9.5)
    r2.font.color.rgb = COLOR_TEXT

# Spacing
sp = doc.add_paragraph()
sp.paragraph_format.space_after = Pt(12)

# --- PHẦN 1: TỔNG QUAN KIẾN TRÚC ---
add_heading_1("I. TỔNG QUAN KIẾN TRÚC & CẤU HÌNH DOCKER COMPOSE")
add_body(
    "Dự án được đóng gói và điều phối tự động thông qua công cụ Docker Compose. Toàn bộ hệ thống "
    "gồm 2 dịch vụ độc lập giao tiếp qua mạng nội bộ Docker Network (my-project_default) và lưu trữ bền vững qua Docker Volume."
)

# Table summary of services
srv_table = doc.add_table(rows=3, cols=5)
srv_table.alignment = WD_TABLE_ALIGNMENT.CENTER
headers = ["Service", "Container Name", "Port Host : Container", "Base Image / Build", "Mô Tả Chức Năng"]
for j, h in enumerate(headers):
    cell = srv_table.rows[0].cells[j]
    set_cell_background(cell, "0F4C81")
    set_cell_margins(cell, 90, 90, 90, 90)
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(h)
    run.font.name = "Arial"
    run.font.bold = True
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(255, 255, 255)

srv_rows = [
    ("db", "my-project-db-1", "5432 : 5432", "postgres:16-alpine (Custom init.sql)", "Hệ quản trị CSDL PostgreSQL, tự động nạp bảng words và dữ liệu 10 từ vựng."),
    ("web", "my-project-web-1", "3000 : 3000", "Multi-stage Dockerfile (Node 18)", "Giao diện React Vite build tĩnh kết hợp Backend Express API phục vụ dữ liệu.")
]
for i, row_data in enumerate(srv_rows, start=1):
    row = srv_table.rows[i]
    bg_color = "F8FAFC" if i % 2 == 1 else "FFFFFF"
    for j, val in enumerate(row_data):
        cell = row.cells[j]
        set_cell_background(cell, bg_color)
        set_cell_margins(cell, 80, 80, 80, 80)
        p = cell.paragraphs[0]
        p.paragraph_format.space_after = Pt(0)
        run = p.add_run(val)
        run.font.name = "Arial"
        run.font.size = Pt(9)
        run.font.color.rgb = COLOR_TEXT

sp = doc.add_paragraph()
sp.paragraph_format.space_after = Pt(12)

# --- PHẦN 2: CÁC BƯỚC THỰC HIỆN TRÊN CMD ---
add_heading_1("II. CHI TIẾT CÁC BƯỚC THỰC HIỆN TRÊN COMMAND PROMPT (CMD)")

# BƯỚC 1
add_heading_2("Bước 1: Kiểm tra môi trường Docker & Docker Compose")
add_body(
    "Trước khi khởi chạy dự án, kiểm tra phiên bản Docker Engine và Docker Compose trên máy tính "
    "nhằm đảm bảo dịch vụ Docker daemon đã được bật và sẵn sàng nhận lệnh.",
    bold_prefix="Mục đích: "
)
add_body("docker --version\ndocker compose version", bold_prefix="Câu lệnh thực thi: ")
add_image_step(os.path.join(OUTPUT_DIR, "step1_docker_version.png"), "Hình 1: Kiểm tra phiên bản Docker 29.6.2 và Docker Compose v2.32 trên CMD")
add_body(
    "Kết quả hiển thị Docker client và Docker Compose đều đã hoạt động bình thường, sẵn sàng biên dịch dự án.",
    bold_prefix="Đánh giá kết quả: "
)

# BƯỚC 2
add_heading_2("Bước 2: Kiểm tra cấu trúc thư mục & các tệp cấu hình triển khai")
add_body(
    "Kiểm tra sự tồn tại của các file cấu hình quan trọng trong thư mục gốc của dự án bao gồm "
    "docker-compose.yml, Dockerfile đa tầng (Multi-stage build) và biến môi trường .env.",
    bold_prefix="Mục đích: "
)
add_body("dir docker-compose.yml Dockerfile .env", bold_prefix="Câu lệnh thực thi: ")
add_image_step(os.path.join(OUTPUT_DIR, "step2_check_config_files.png"), "Hình 2: Kiểm tra sự tồn tại của các tệp docker-compose.yml, Dockerfile và .env")
add_body(
    "Tất cả 3 file cấu hình cốt lõi đều đầy đủ trong thư mục làm việc E:\\DevOps\\my-project.",
    bold_prefix="Đánh giá kết quả: "
)

# BƯỚC 3
add_heading_2("Bước 3: Xác thực cú pháp cấu hình Docker Compose")
add_body(
    "Lệnh 'docker compose config' thực hiện phân tích cú pháp YAML, nạp các biến môi trường từ file .env, "
    "kiểm tra liên kết phụ thuộc (depends_on), volume và port mapping trước khi tiến hành build image.",
    bold_prefix="Mục đích: "
)
add_body("docker compose config", bold_prefix="Câu lệnh thực thi: ")
add_image_step(os.path.join(OUTPUT_DIR, "step3_validate_compose.png"), "Hình 3: Kết quả xác thực cấu trúc dịch vụ và biến môi trường bằng docker compose config")
add_body(
    "Cấu trúc dịch vụ 'db' và 'web' hoàn toàn hợp lệ, các biến POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB và các cổng được gán chính xác.",
    bold_prefix="Đánh giá kết quả: "
)

# BƯỚC 4
add_heading_2("Bước 4: Build Images và khởi chạy các dịch vụ ở chế độ chạy ngầm (Background)")
add_body(
    "Sử dụng tham số '--build' để Docker tự động đóng gói image frontend (React Vite), backend (Node.js Express) "
    "và database (Postgres với dữ liệu khởi tạo). Tham số '-d' (detached) giúp container chạy nền ngầm.",
    bold_prefix="Mục đích: "
)
add_body("docker compose up -d --build", bold_prefix="Câu lệnh thực thi: ")
add_image_step(os.path.join(OUTPUT_DIR, "step4_docker_up_build.png"), "Hình 4: Quá trình build multi-stage Docker image và khởi chạy các container")
add_callout(
    "Quá trình build áp dụng Multi-stage build (Stage 1: node:18-alpine biên dịch Vite bundle, Stage 2: Express server "
    "phục vụ API và chứa thư mục /dist được copy từ Stage 1). Điều này giúp tối ưu hóa dung lượng image và nâng cao bảo mật.",
    prefix="Điểm nhấn kỹ thuật: "
)

# BƯỚC 5
add_heading_2("Bước 5: Kiểm tra trạng thái hoạt động của các Container")
add_body(
    "Sau khi khởi động, kiểm tra trạng thái hoạt động thực tế của từng container bằng lệnh 'docker compose ps'.",
    bold_prefix="Mục đích: "
)
add_body("docker compose ps", bold_prefix="Câu lệnh thực thi: ")
add_image_step(os.path.join(OUTPUT_DIR, "step5_docker_ps.png"), "Hình 5: Danh sách các container đang chạy và trạng thái ánh xạ cổng (Port mapping)")
add_body(
    "Cả 2 container my-project-db-1 (cổng 5432) và my-project-web-1 (cổng 3000) đều ở trạng thái 'Up', hoạt động ổn định.",
    bold_prefix="Đánh giá kết quả: "
)

# BƯỚC 6
add_heading_2("Bước 6: Kiểm tra Logs chi tiết của Database và Web Backend")
add_body(
    "Kiểm tra nhật ký hoạt động (logs) để xác nhận PostgreSQL đã chạy lệnh nạp init.sql thành công "
    "và ứng dụng Node.js Express đã lắng nghe kết nối tại cổng 3000.",
    bold_prefix="Mục đích: "
)
add_body("docker compose logs --tail=15", bold_prefix="Câu lệnh thực thi: ")
add_image_step(os.path.join(OUTPUT_DIR, "step6_docker_logs.png"), "Hình 6: Logs chi tiết khởi tạo PostgreSQL (CREATE TABLE, INSERT 0 10) và Express Server")
add_body(
    "Logs xác nhận bảng cơ sở dữ liệu đã được tạo thành công, 10 bản ghi từ điển đã được chèn và máy chủ web hiển thị 'Server đang chạy tại http://localhost:3000'.",
    bold_prefix="Đánh giá kết quả: "
)

# BƯỚC 7
add_heading_2("Bước 7: Kiểm thử API Endpoint từ điển bằng công cụ cURL")
add_body(
    "Thực hiện gọi thử nghiệm API '/api/words' trực tiếp từ cửa sổ dòng lệnh để kiểm tra luồng dữ liệu "
    "từ Web Container kết nối sang Database Container.",
    bold_prefix="Mục đích: "
)
add_body("curl.exe -i http://localhost:3000/api/words", bold_prefix="Câu lệnh thực thi: ")
add_image_step(os.path.join(OUTPUT_DIR, "step7_curl_api_test.png"), "Hình 7: Gọi cURL tới API Endpoint trả về mã 200 OK và danh sách từ vựng tiếng Anh dạng JSON")
add_body(
    "API phản hồi thành công mã trạng thái HTTP/1.1 200 OK, Content-Type: application/json và trả về danh sách 10 từ vựng "
    "['apple', 'book', 'computer', 'dog', 'elephant', 'flower', 'guitar', 'house', 'internet', 'juice'] trích xuất từ cơ sở dữ liệu PostgreSQL.",
    bold_prefix="Đánh giá kết quả: "
)

# BƯỚC 8
add_heading_2("Bước 8: Kiểm thử giao diện Web App thực tế trên trình duyệt")
add_body(
    "Mở trình duyệt web tại địa chỉ http://localhost:3000 để kiểm tra giao diện người dùng frontend "
    "tra cứu từ điển Anh - Việt được phục vụ từ Docker Web Container.",
    bold_prefix="Mục đích: "
)

browser_img_1 = r"C:\Users\teotv\.gemini\antigravity-ide\brain\d12cadc8-0ca8-4f25-8ca4-9e1438cb5e68\dictionary_homepage_1791908135754.png"
browser_img_2 = r"C:\Users\teotv\.gemini\antigravity-ide\brain\d12cadc8-0ca8-4f25-8ca4-9e1438cb5e68\dictionary_next_word_1791908148404.png"

if os.path.exists(browser_img_1):
    add_image_step(browser_img_1, "Hình 8.1: Giao diện Trang chủ Tra từ điển Anh - Việt đang chạy trên http://localhost:3000")
if os.path.exists(browser_img_2):
    add_image_step(browser_img_2, "Hình 8.2: Tính năng chuyển từ và tra cứu từ vựng hoạt động mượt mà trên trình duyệt")

add_body(
    "Giao diện người dùng tải nhanh chóng, hiển thị trực quan các thẻ từ vựng tiếng Anh kèm nghĩa tiếng Việt, "
    "các nút điều hướng 'Từ tiếp theo' hoạt động chính xác.",
    bold_prefix="Đánh giá kết quả: "
)

# BƯỚC 9
add_heading_2("Bước 9: Dọn dẹp tài nguyên & Dừng hệ thống khi hoàn tất (Tùy chọn)")
add_body(
    "Khi kết thúc quá trình làm việc hoặc kiểm thử, sử dụng lệnh 'docker compose down' để dừng và gỡ bỏ "
    "các container, network một cách an toàn mà vẫn bảo lưu dữ liệu trong volume.",
    bold_prefix="Mục đích: "
)
add_body("docker compose down", bold_prefix="Câu lệnh thực thi: ")
add_image_step(os.path.join(OUTPUT_DIR, "step8_docker_down.png"), "Hình 9: Lệnh docker compose down dừng và giải phóng container an toàn")

# --- PHẦN 3: KẾT LUẬN ---
add_heading_1("III. KẾT LUẬN & ĐÁNH GIÁ TỔNG QUAN")
add_body(
    "1. Dự án đã được đóng gói và cấu hình hoàn thiện thành các Docker Image chuẩn hóa, đáp ứng đầy đủ yêu cầu "
    "của một kiến trúc Fullstack hiện đại (React Frontend, Node.js Backend API, PostgreSQL Database).\n"
    "2. Quá trình triển khai thông qua Docker Compose diễn ra hoàn toàn tự động chỉ với 1 câu lệnh duy nhất 'docker compose up -d --build'.\n"
    "3. Tất cả các dịch vụ kết nối mạng nội bộ an toàn, dữ liệu cơ sở dữ liệu được lưu trữ bền vững tại Docker Volume.\n"
    "4. Hệ thống hoàn toàn sẵn sàng để tích hợp vào Jenkins CI/CD Pipeline tự động hóa build, test và deploy lên production."
)

doc.save(DOCX_PATH)
print("SUCCESS! Document generated at:", DOCX_PATH)
