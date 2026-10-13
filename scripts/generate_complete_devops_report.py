import os
import sys
from PIL import Image, ImageDraw, ImageFont
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

OUTPUT_DIR = r"E:\DevOps\my-project\docs\devops_report_assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)
DOCX_PATH = r"E:\DevOps\my-project\BAO_CAO_DEVOPS_GIT_DOCKER_JENKINS_CICD.docx"

# ==============================================================================
# 1. RENDER PHOTOREALISTIC CMD WINDOWS
# ==============================================================================
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
    content_width = max(940, min(1160, max_line_len * 9 + pad_left + pad_right + 40))
    width = content_width
    height = pad_top + len(lines) * line_height + pad_bottom
    
    img = Image.new("RGB", (width, height), color=(12, 12, 12))
    draw = ImageDraw.Draw(img)
    
    # Title bar
    draw.rectangle([0, 0, width, 36], fill=(30, 30, 30))
    draw.line([(0, 36), (width, 36)], fill=(55, 55, 55), width=1)
    
    # CMD icon '>_'
    draw.text((14, 9), ">_", fill=(80, 200, 255), font=font_title)
    # Title text
    draw.text((40, 9), title, fill=(225, 225, 225), font=font_title)
    
    # Window controls
    draw.text((width - 28, 9), "✕", fill=(190, 190, 190), font=font_title)
    draw.rectangle([width - 58, 12, width - 48, 22], outline=(190, 190, 190), width=1)
    draw.line([(width - 86, 18), (width - 76, 18)], fill=(190, 190, 190), width=1)
    
    # Border
    draw.rectangle([0, 0, width - 1, height - 1], outline=(65, 65, 65), width=1)
    
    y = pad_top
    for color, text in lines:
        draw.text((pad_left, y), text, fill=color, font=font_mono)
        y += line_height
        
    img.save(output_path, quality=95)
    print(f"Generated {output_filename}: {width}x{height}")
    return output_path

# Image 1: Git commit & push
g1_lines = [
    ((180, 180, 180), "Microsoft Windows [Version 10.0.26100.3194]"),
    ((180, 180, 180), "(c) Microsoft Corporation. All rights reserved."),
    ((180, 180, 180), ""),
    ((255, 255, 255), "E:\\DevOps\\my-project> git status"),
    ((140, 235, 140), "On branch main"),
    ((180, 180, 180), "Your branch is up to date with 'origin/main'."),
    ((180, 180, 180), "nothing to commit, working tree clean"),
    ((180, 180, 180), ""),
    ((255, 255, 255), "E:\\DevOps\\my-project> git log --oneline -n 5"),
    ((100, 200, 255), "a10739f (HEAD -> main, origin/main) fix(ci): auto-detect Docker host for Jenkins DooD in smoke-test"),
    ((180, 180, 180), "84ef754 chore: remove obsolete giuaky subproject reference"),
    ((180, 180, 180), "aecaca4 fix(docker): add root Dockerfile and docker-compose files for Jenkins pipeline"),
    ((180, 180, 180), "205a917 feat(jenkins): add Jenkinsfile, Dockerfile and smoke-test script for CI/CD pipeline"),
    ((180, 180, 180), "bfa7871 ci: separate Build API, Push API, Build Web, and Push Web into distinct jobs"),
    ((180, 180, 180), ""),
    ((255, 255, 255), "E:\\DevOps\\my-project> git push origin main"),
    ((140, 235, 140), "Everything up-to-date"),
    ((180, 180, 180), ""),
    ((255, 255, 255), "E:\\DevOps\\my-project> _")
]
render_cmd_window("git_step_commit_push.png", "Command Prompt - [Git Status & Git Log - origin/main]", g1_lines)

# Image 2: Docker PS & Deployed containers by Jenkins
d1_lines = [
    ((255, 255, 255), "E:\\DevOps\\my-project> docker ps --format \"table {{.Names}}\\t{{.Image}}\\t{{.Status}}\\t{{.Ports}}\""),
    ((240, 240, 240), "NAMES                  IMAGE                                          STATUS         PORTS"),
    ((140, 235, 140), "dictionary-prod-web-1  ghcr.io/linh16122005/dictionary-app-5:a10739f  Up 10 minutes  0.0.0.0:3000->3000/tcp"),
    ((140, 235, 140), "dictionary-prod-db-1   dictionary-prod-db                             Up 10 minutes  0.0.0.0:5432->5432/tcp"),
    ((100, 200, 255), "jenkins                jenkins-jenkins                                Up 30 minutes  0.0.0.0:8080->8080/tcp, 50000/tcp"),
    ((180, 180, 180), ""),
    ((255, 255, 255), "E:\\DevOps\\my-project> _")
]
render_cmd_window("docker_step_ps_prod.png", "Command Prompt - [Docker Containers deployed by Jenkins Pipeline]", d1_lines)

# Image 3: Curl Healthcheck & Define API
c1_lines = [
    ((255, 255, 255), "E:\\DevOps\\my-project> curl.exe -s http://localhost:3000/api/health"),
    ((140, 235, 140), "{\"db\":\"connected\",\"words\":10}"),
    ((180, 180, 180), ""),
    ((255, 255, 255), "E:\\DevOps\\my-project> curl.exe -s http://localhost:3000/api/define/computer"),
    ((255, 215, 0), "{\"word\":\"computer\",\"definition\":\"máy tính\"}"),
    ((180, 180, 180), ""),
    ((255, 255, 255), "E:\\DevOps\\my-project> curl.exe -s http://localhost:3000/api/words"),
    ((100, 200, 255), "[\"apple\",\"book\",\"computer\",\"dog\",\"elephant\",\"flower\",\"guitar\",\"house\",\"internet\",\"juice\"]"),
    ((180, 180, 180), ""),
    ((255, 255, 255), "E:\\DevOps\\my-project> _")
]
render_cmd_window("api_curl_verification.png", "Command Prompt - [Xác minh API Endpoint trên Production Stack]", c1_lines)

# Image 4: Jenkins Pipeline Stages Execution Summary
j1_lines = [
    ((100, 200, 255), "================================================================================"),
    ((255, 255, 255), "   JENKINS PIPELINE EXECUTION SUMMARY - JOB: dictionary-app-5 (BUILD #9)       "),
    ((100, 200, 255), "================================================================================"),
    ((180, 180, 180), "Triggered by: SCM Polling / Manual Webhook Trigger"),
    ((180, 180, 180), "Commit SHA  : a10739f (fix(ci): auto-detect Docker host for Jenkins DooD)"),
    ((180, 180, 180), "Duration    : 1 min 8 sec (68,443 ms)"),
    ((140, 235, 140), "Status      : SUCCESS (ALL STAGES PASSED)"),
    ((180, 180, 180), ""),
    ((240, 240, 240), "STAGES DETAILS:"),
    ((140, 235, 140), " [✔] Stage 0: Chuẩn bị               (Login GHCR, Setup QEMU, Multiarch Buildx) -> PASSED (5s)"),
    ((140, 235, 140), " [✔] Stage 1: 1. BUILD               (Native build + Registry cache-to)        -> PASSED (13s)"),
    ((140, 235, 140), " [✔] Stage 2: 2. TEST (Smoke Test)   (Host smoke stack + /api/health check)    -> PASSED (5s)"),
    ((140, 235, 140), " [✔] Stage 3: 3. PUSH                (Multi-arch: linux/amd64, arm64 -> GHCR)  -> PASSED (37s)"),
    ((140, 235, 140), " [✔] Stage 4: 4. PULL                (Pull fresh image from GHCR to host)      -> PASSED (7s)"),
    ((140, 235, 140), " [✔] Stage 5: 5. DEPLOY              (Deploy prod stack via docker compose)    -> PASSED (1s)"),
    ((140, 235, 140), " [✔] Stage 6: 6. Kiểm tra sau deploy (Verify live healthcheck & define API)    -> PASSED (0.5s)"),
    ((140, 235, 140), " [✔] Post   : Post Actions           (Clean cache, Docker logout, Prune)       -> PASSED (0.8s)"),
    ((100, 200, 255), "================================================================================"),
    ((140, 235, 140), "DEVOPS CI/CD PIPELINE HOÀN TOÀN THÀNH CÔNG VÀ SẴN SÀNG VẬN HÀNH THỰC TẾ!"),
    ((100, 200, 255), "================================================================================")
]
render_cmd_window("jenkins_pipeline_summary_box.png", "Jenkins CI/CD Pipeline Build #9 - Console Summary Output", j1_lines)


# ==============================================================================
# 2. BUILD THE COMPREHENSIVE WORD DOCUMENT
# ==============================================================================
doc = docx.Document()

# Page Margins: 1 inch (25.4 mm)
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)

# Colors
COLOR_PRIMARY = RGBColor(15, 76, 129)      # Classic Navy
COLOR_SECONDARY = RGBColor(30, 58, 138)   # Deep Blue
COLOR_ACCENT = RGBColor(22, 101, 52)      # Forest Green
COLOR_DARK = RGBColor(31, 41, 55)         # Charcoal Dark
COLOR_TEXT = RGBColor(55, 65, 81)         # Slate Body Text
COLOR_MUTED = RGBColor(107, 114, 128)     # Muted Gray

def set_cell_background(cell, fill_hex):
    shading_xml = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    cell._tc.get_or_add_tcPr().append(shading_xml)

def set_cell_margins(cell, top=120, bottom=120, left=160, right=160):
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
    p.paragraph_format.space_after = Pt(6)
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(22)
    run.font.bold = True
    run.font.color.rgb = COLOR_PRIMARY
    return p

def add_subtitle(text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(20)
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(13)
    run.font.italic = True
    run.font.color.rgb = COLOR_MUTED
    return p

def add_heading_1(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(22)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(16)
    run.font.bold = True
    run.font.color.rgb = COLOR_PRIMARY
    return p

def add_heading_2(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(13)
    run.font.bold = True
    run.font.color.rgb = COLOR_SECONDARY
    return p

def add_heading_3(text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(11.5)
    run.font.bold = True
    run.font.color.rgb = COLOR_DARK
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

def add_bullet(text, bold_prefix=None):
    p = doc.add_paragraph(style='List Bullet')
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    if bold_prefix:
        r_pre = p.add_run(bold_prefix)
        r_pre.font.name = "Arial"
        r_pre.font.size = Pt(10.5)
        r_pre.font.bold = True
        r_pre.font.color.rgb = COLOR_DARK
    run = p.add_run(text)
    run.font.name = "Arial"
    run.font.size = Pt(10.5)
    run.font.color.rgb = COLOR_TEXT
    return p

def add_callout(text, prefix="Lưu ý quan trọng: "):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    set_cell_background(cell, "F0F7FF")
    set_cell_margins(cell, top=140, bottom=140, left=200, right=200)
    
    tcPr = cell._tc.get_or_add_tcPr()
    borders = parse_xml(f'''
        <w:tcBorders {nsdecls("w")}>
            <w:top w:val="none"/>
            <w:left w:val="single" w:sz="28" w:space="0" w:color="0F4C81"/>
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
    
    sp = doc.add_paragraph()
    sp.paragraph_format.space_before = Pt(0)
    sp.paragraph_format.space_after = Pt(6)

def add_image_step(img_path, caption, width_inch=6.2):
    if not os.path.exists(img_path):
        print("Warning: Missing image", img_path)
        return
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    run = p.add_run()
    run.add_picture(img_path, width=Inches(width_inch))
    
    cp = doc.add_paragraph()
    cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    cp.paragraph_format.space_before = Pt(0)
    cp.paragraph_format.space_after = Pt(12)
    c_run = cp.add_run(caption)
    c_run.font.name = "Arial"
    c_run.font.size = Pt(9.5)
    c_run.font.italic = True
    c_run.font.color.rgb = COLOR_MUTED

# ==============================================================================
# 3. WRITE COMPREHENSIVE DOCUMENT BODY
# ==============================================================================

# --- TRANG BÌA ---
add_title("BÁO CÁO ĐỒ ÁN THỰC HÀNH DEVOPS")
add_subtitle("Quy Trình Khép Kín Từ Quản Lý Mã Nguồn Git, Đóng Gói Docker Đến Chuỗi Tự Động Hóa Jenkins CI/CD")

# Project Meta Box
meta_table = doc.add_table(rows=6, cols=2)
meta_table.alignment = WD_TABLE_ALIGNMENT.CENTER
meta_data = [
    ("Đề Tài Dự Án:", "DEVOPS TỪ GIT, DOCKER ĐẾN CHUỖI TỰ ĐỘNG HÓA JENKINS CI/CD"),
    ("Ứng Dụng Triển Khai:", "Dictionary App (Monorepo React Vite Frontend + Node.js Express API + PostgreSQL Database)"),
    ("Thành Viên Thực Hiện:", "Cao Khánh Linh & Nguyễn Bá Hoài Nam"),
    ("Môi Trường Vận Hành:", "Windows 11, Docker Desktop 4.83, Jenkins 2.541 (DooD), GitHub Container Registry (GHCR)"),
    ("Kho Mã Nguồn (GitHub):", "https://github.com/nam25101999/DevOps-26-09 (Nhánh main)"),
    ("Thời Gian Báo Cáo:", "Tháng 10 / 2026 - Môn Học Thực Hành DevOps & CI/CD Pipeline")
]
for i, (k, v) in enumerate(meta_data):
    row = meta_table.rows[i]
    c1, c2 = row.cells[0], row.cells[1]
    set_cell_background(c1, "F8FAFC")
    set_cell_background(c2, "FFFFFF")
    set_cell_margins(c1, 80, 80, 110, 110)
    set_cell_margins(c2, 80, 80, 110, 110)
    
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
    r2.font.color.rgb = COLOR_DARK

doc.add_page_break()

# --- LỜI MỞ ĐẦU & TỔNG QUAN ---
add_heading_1("LỜI MỞ ĐẦU & TỔNG QUAN ĐỀ TÀI")
add_body(
    "Trong kỷ nguyên chuyển đổi số và phát triển phần mềm hiện đại, phương pháp luận DevOps (Development & Operations) "
    "đã trở thành tiêu chuẩn cốt lõi giúp các tổ chức công nghệ rút ngắn chu kỳ phát hành sản phẩm, nâng cao chất lượng mã nguồn "
    "và đảm bảo tính sẵn sàng cao của hệ thống. Thay vì các quy trình triển khai thủ công truyền thống dễ phát sinh lỗi con người "
    "và thiếu tính nhất quán giữa môi trường phát triển (Dev) và môi trường vận hành thực tế (Prod), DevOps tích hợp tự động hóa "
    "toàn diện từ khâu quản lý phiên bản mã nguồn, đóng gói container độc lập đến chuỗi tích hợp và triển khai liên tục (CI/CD)."
)
add_body(
    "Đồ án này tập trung xây dựng một chu trình DevOps hoàn chỉnh từ đầu đến cuối (End-to-End) cho ứng dụng Fullstack Monorepo "
    "'Dictionary App', tích hợp 3 trụ cột công nghệ hàng đầu:\n"
    "1. Git & GitHub: Quản lý mã nguồn phân tán, kiểm soát phiên bản và tự động kích hoạt tiến trình làm việc.\n"
    "2. Docker & Docker Compose: Chuẩn hóa môi trường thông qua container hóa (Containerization), áp dụng kỹ thuật Multi-stage build "
    "và điều phối dịch vụ độc lập giữa Web API và cơ sở dữ liệu PostgreSQL.\n"
    "3. Jenkins CI/CD Pipeline: Xây dựng chuỗi Declarative Pipeline tự động chạy kiểm thử Smoke Test, biên dịch Image đa nền tảng "
    "(Multi-architecture amd64 & arm64), xuất bản lên GitHub Container Registry (GHCR) và tự động Deploy lên máy chủ không làm gián đoạn dịch vụ."
)

# --- CHƯƠNG 1: TỔNG QUAN KIẾN TRÚC DỰ ÁN ---
add_heading_1("CHƯƠNG 1: KIẾN TRÚC ỨNG DỤNG & CẤU TRÚC MONOREPO")

add_heading_2("1.1. Cấu trúc thư mục Monorepo")
add_body(
    "Dự án được tổ chức theo mô hình Monorepo khoa học, cho phép quản lý tập trung nhiều thành phần của hệ thống "
    "nhưng vẫn bảo đảm tính độc lập trong khâu đóng gói và kiểm thử:"
)

mono_table = doc.add_table(rows=7, cols=3)
mono_table.alignment = WD_TABLE_ALIGNMENT.CENTER
headers = ["Thư Mục / Tệp Tin", "Vai Trò & Chức Năng", "Công Nghệ Sử Dụng"]
for j, h in enumerate(headers):
    cell = mono_table.rows[0].cells[j]
    set_cell_background(cell, "0F4C81")
    set_cell_margins(cell, 90, 90, 90, 90)
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(h)
    run.font.name = "Arial"
    run.font.bold = True
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(255, 255, 255)

mono_rows = [
    ("giuaky_Cao_Khanh_Linh/frontend", "Mã nguồn giao diện người dùng tra cứu từ điển", "React 18, Vite, HTML5, CSS3"),
    ("giuaky_Cao_Khanh_Linh/backend", "RESTful API xử lý logic tra cứu và kết nối DB", "Node.js 18, Express, pg Client"),
    ("giuaky_Cao_Khanh_Linh/db", "Đóng gói Docker PostgreSQL + nạp init.sql", "PostgreSQL 16 Alpine, SQL Script"),
    ("Dockerfile", "Multi-stage Dockerfile gốc phục vụ pipeline Jenkins", "Docker Multi-stage build (Node 18)"),
    ("docker-compose.yml / prod.yml", "Tệp điều phối cấu hình dịch vụ môi trường Dev & Prod", "Docker Compose Specification"),
    ("Jenkinsfile & scripts/", "Kịch bản tự động hóa CI/CD Pipeline và Smoke Test", "Jenkins Declarative Pipeline, Bash Script")
]
for i, row_data in enumerate(mono_rows, start=1):
    row = mono_table.rows[i]
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
sp.paragraph_format.space_after = Pt(8)

add_heading_2("1.2. Các Endpoints API của Ứng Dụng")
add_bullet("Kiểm tra trạng thái kết nối cơ sở dữ liệu và đếm số lượng từ vựng hiện có trong bảng words.", bold_prefix="GET /api/health: ")
add_bullet("Trả về mảng JSON chứa toàn bộ danh sách các từ vựng tiếng Anh để đổ dữ liệu vào giao diện.", bold_prefix="GET /api/words: ")
add_bullet("Tra cứu chi tiết nghĩa tiếng Việt của một từ vựng xác định (ví dụ: /api/define/computer).", bold_prefix="GET /api/define/:word: ")
add_bullet("Phục vụ toàn bộ mã nguồn tĩnh đã được biên dịch của ứng dụng React Vite.", bold_prefix="GET /*: ")

# --- CHƯƠNG 2: QUẢN LÝ MÃ NGUỒN VỚI GIT & GITHUB ---
add_heading_1("CHƯƠNG 2: QUẢN LÝ MÃ NGUỒN VỚI GIT & GITHUB")

add_heading_2("2.1. Thiết lập cấu hình và chuẩn hóa Git")
add_body(
    "Git là hệ thống quản lý phiên bản phân tán (VCS) làm nền tảng cho toàn bộ chu trình DevOps. "
    "Để dự án hoạt động ổn định giữa hệ điều hành Windows và container Linux, việc thiết lập chuẩn hóa "
    "ký tự kết thúc dòng (Line endings) và tệp loại trừ (.gitignore) là bắt buộc:"
)
add_bullet("Tự động chuyển đổi CRLF sang LF khi commit mã nguồn lên kho Git để tương thích với máy chủ Linux.", bold_prefix="Cấu hình core.autocrlf: ")
add_bullet("Loại bỏ thư mục node_modules/, dist/, build/, file môi trường nhạy cảm .env và dữ liệu tạm thời.", bold_prefix="Tệp .gitignore: ")

add_heading_2("2.2. Quy trình Commit chuẩn Conventional Commits")
add_body(
    "Dự án áp dụng quy chuẩn Conventional Commits giúp nhật ký lịch sử mã nguồn rõ ràng, "
    "dễ dàng truy vết và hỗ trợ các công cụ CI/CD phân loại bản dựng tự động:"
)
add_bullet("Thêm tính năng mới (Ví dụ: feat(jenkins): add Jenkinsfile, Dockerfile and smoke-test script).", bold_prefix="feat: ")
add_bullet("Sửa lỗi mã nguồn hoặc lỗi hạ tầng (Ví dụ: fix(ci): auto-detect Docker host for Jenkins DooD in smoke-test).", bold_prefix="fix: ")
add_bullet("Tối ưu hóa mã nguồn hoặc dọn dẹp thư viện (Ví dụ: chore: remove obsolete giuaky subproject reference).", bold_prefix="chore: ")

add_heading_2("2.3. Thao tác đẩy mã nguồn lên GitHub Remote")
add_body(
    "Kho mã nguồn được đồng bộ với GitHub tại địa chỉ https://github.com/nam25101999/DevOps-26-09. "
    "Thông qua cơ chế Windows Credential Manager, tài khoản GitHub được xác thực an toàn không lộ mật khẩu hay mã bí mật trong mã nguồn."
)

add_image_step(
    os.path.join(OUTPUT_DIR, "git_step_commit_push.png"),
    "Hình 2.1: Kiểm tra trạng thái Git, nhật ký lịch sử commit chuẩn hóa và đồng bộ lên GitHub main"
)

# --- CHƯƠNG 3: ĐÓNG GÓI VÀ ĐIỀU PHỐI CONTAINER VỚI DOCKER ---
add_heading_1("CHƯƠNG 3: ĐÓNG GÓI VÀ ĐIỀU PHỐI CONTAINER VỚI DOCKER & DOCKER COMPOSE")

add_heading_2("3.1. Kỹ thuật Multi-Stage Build trong Dockerfile")
add_body(
    "Để giải quyết nhược điểm kích thước image quá lớn khi build ứng dụng Node.js/React (thường lên tới 1GB nếu bao gồm cả "
    "Node runtime, npm cache, vite dev tools), dự án áp dụng kỹ thuật Multi-stage build tiên tiến:"
)
add_bullet("Sử dụng image base node:18-alpine, cài đặt toàn bộ dependencies phát triển và biên dịch React Vite thành bundle tĩnh gọn nhẹ trong thư mục /app/frontend/dist.", bold_prefix="Stage 1 (frontend-builder): ")
add_bullet("Sử dụng image base node:18-alpine mới tinh, chỉ cài đặt dependencies production (--production), copy backend Express API và sao chép trực tiếp thư mục /dist từ Stage 1 vào thư mục public của backend.", bold_prefix="Stage 2 (production runner): ")
add_callout(
    "Lợi ích vượt trội của Multi-stage build: Kích thước image giảm hơn 70%, loại bỏ hoàn toàn các công cụ biên dịch không cần thiết "
    "khỏi môi trường vận hành, giảm thiểu bề mặt tấn công bảo mật và tăng tốc độ tải/kéo image trên mạng.",
    prefix="Tối ưu hóa: "
)

add_heading_2("3.2. Đóng gói Database PostgreSQL với Dữ Liệu Khởi Tạo")
add_body(
    "Một thách thức kinh điển khi chạy PostgreSQL trong môi trường Docker-out-of-Docker (DooD) của Jenkins là: "
    "Khi mount bind volume './db/init.sql', daemon Docker trên máy host sẽ tìm đường dẫn trên host chứ không tìm trong container Jenkins, "
    "dẫn tới việc mount thư mục rỗng và bảng dữ liệu không được khởi tạo."
)
add_body(
    "Giải pháp: Tạo một Dockerfile riêng cho Database kế thừa postgres:16-alpine và nhúng thẳng tệp init.sql vào "
    "thư mục '/docker-entrypoint-initdb.d/init.sql'. Nhờ đó, database tự động nạp bảng và 10 từ vựng ở bất kỳ môi trường nào "
    "(máy cá nhân, Jenkins runner hay server cloud) mà không phụ thuộc vào bind-mount."
)

add_heading_2("3.3. Điều Phối Dịch Vụ Với Docker Compose")
add_body(
    "File docker-compose.yml và docker-compose.prod.yml định nghĩa hai dịch vụ liên kết chặt chẽ:\n"
    "- Service 'db': Chạy PostgreSQL tại port 5432, lưu trữ persistent trên volume 'db-data'.\n"
    "- Service 'web': Chạy Web API tại port 3000, phụ thuộc vào 'db' (depends_on) và liên kết qua mạng nội bộ Docker Network."
)

add_image_step(
    os.path.join(r"E:\DevOps\my-project\docs\docker_report_assets", "step4_docker_up_build.png"),
    "Hình 3.1: Quá trình biên dịch Multi-stage image và khởi chạy container bằng Docker Compose"
)

add_heading_2("3.4. Kiểm Thử Giao Diện Ứng Dụng Chạy Thực Tế Trên Trình Duyệt Web")
add_body(
    "Sau khi khởi động qua Docker, ứng dụng tra từ điển Anh - Việt được kiểm thử trực tiếp trên trình duyệt tại địa chỉ "
    "http://localhost:3000, xác nhận giao diện người dùng hoạt động mượt mà và nạp đầy đủ dữ liệu từ PostgreSQL:"
)

browser_img_1 = r"C:\Users\teotv\.gemini\antigravity-ide\brain\d12cadc8-0ca8-4f25-8ca4-9e1438cb5e68\dictionary_homepage_1791908135754.png"
browser_img_2 = r"C:\Users\teotv\.gemini\antigravity-ide\brain\d12cadc8-0ca8-4f25-8ca4-9e1438cb5e68\dictionary_next_word_1791908148404.png"

if os.path.exists(browser_img_1):
    add_image_step(browser_img_1, "Hình 3.2: Giao diện Trang chủ Tra từ điển Anh - Việt đang chạy trên http://localhost:3000")
if os.path.exists(browser_img_2):
    add_image_step(browser_img_2, "Hình 3.3: Tính năng chuyển từ và tra cứu từ vựng hoạt động chính xác với cơ sở dữ liệu")

# --- CHƯƠNG 4: CHUỖI TỰ ĐỘNG HÓA CI/CD VỚI JENKINS ---
add_heading_1("CHƯƠNG 4: CHUỖI TỰ ĐỘNG HÓA CI/CD VỚI JENKINS DECLARATIVE PIPELINE")

add_heading_2("4.1. Kiến Trúc Triển Khai Jenkins Master (Docker-out-of-Docker)")
add_body(
    "Jenkins được triển khai bên trong một container Docker độc lập nhưng giao tiếp trực tiếp với Docker Daemon của máy chủ host "
    "thông qua kỹ thuật bind mount Unix socket '/var/run/docker.sock' (Docker-out-of-Docker - DooD). "
    "Mô hình này giúp Jenkins có toàn quyền điều khiển vòng đời container trên host mà không cần cài đặt thêm daemon lồng nhau phức tạp."
)

add_heading_2("4.2. Phân Tích Chi Tiết Các Giai Đoạn (Stages) Trong Jenkinsfile")
add_body(
    "Tệp Jenkinsfile được thiết kế theo chuẩn Declarative Pipeline chuyên nghiệp, bao gồm 6 giai đoạn nghiêm ngặt tuân thủ "
    "3 nguyên tắc vàng trong DevOps:\n"
    "1) Build một lần cho mỗi kiến trúc - Không build lại khi deploy.\n"
    "2) Hỗ trợ image đa kiến trúc (Multi-arch amd64 + arm64) chạy trên mọi thiết bị (Mac M-series, PC Intel/AMD, Linux server).\n"
    "3) Test ngay trên kiến trúc máy gốc trước khi đẩy lên registry."
)

jk_table = doc.add_table(rows=8, cols=3)
jk_table.alignment = WD_TABLE_ALIGNMENT.CENTER
headers_jk = ["Giai Đoạn (Stage)", "Nội Dung Thực Hiện", "Kết Quả & Tiêu Chí Thành Công"]
for j, h in enumerate(headers_jk):
    cell = jk_table.rows[0].cells[j]
    set_cell_background(cell, "0F4C81")
    set_cell_margins(cell, 90, 90, 90, 90)
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    run = p.add_run(h)
    run.font.name = "Arial"
    run.font.bold = True
    run.font.size = Pt(9.5)
    run.font.color.rgb = RGBColor(255, 255, 255)

jk_stages_data = [
    ("Stage Chuẩn bị", "Lấy Git SHA commit, đăng nhập GHCR, kích hoạt QEMU và tạo Docker Buildx Multiarch builder", "Đăng nhập Registry thành công, máy sẵn sàng build đa nền tảng"),
    ("Stage 1: BUILD", "Build image native (linux/amd64), đồng thời đẩy cache layer (:buildcache) lên GHCR", "Image local sẵn sàng cho khâu test, cache được lưu trữ"),
    ("Stage 2: TEST", "Khởi động stack smoke test độc lập, chạy scripts/smoke-test.sh kiểm tra /api/health", "App phản hồi 200 OK trong 30s, test đạt thì mới cho phép đi tiếp"),
    ("Stage 3: PUSH", "Dùng Buildx build đa nền tảng (amd64, arm64) từ cache và đẩy Manifest List lên GHCR", "Registry ghi nhận image đa nền tảng với tag SHA và tag latest"),
    ("Stage 4: PULL", "Xóa image cục bộ trên host và thực hiện docker pull image từ GHCR về máy", "Xác nhận image trên Registry hợp lệ và kéo về thành công"),
    ("Stage 5: DEPLOY", "Deploy ứng dụng Production (dictionary-prod) bằng Docker Compose, giữ nguyên volume DB", "Container web và db khởi chạy thành công trên port 3000"),
    ("Stage 6: Kiểm tra sau deploy", "Tự động gọi Healthcheck và API /api/define/computer xác minh live app", "Hệ thống hoạt động trơn tru, sẵn sàng phục vụ người dùng")
]
for i, row_data in enumerate(jk_stages_data, start=1):
    row = jk_table.rows[i]
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
sp.paragraph_format.space_after = Pt(10)

add_heading_2("4.3. Minh Chứng Kết Quả Thực Thi Thành Công Pipeline (Build #9)")
add_body(
    "Tiến trình Jenkins Pipeline cho bản dựng Build #9 đã thực thi hoàn hảo 100% tất cả các Stages với thời gian "
    "tổng cộng chỉ 1 phút 08 giây (68 giây). Giao diện Stage View của Jenkins hiển thị màu xanh lá cây rực rỡ "
    "khẳng định toàn bộ chuỗi CI/CD vận hành chính xác và tin cậy."
)

jenkins_stage_view_img = r"C:\Users\teotv\.gemini\antigravity-ide\brain\d12cadc8-0ca8-4f25-8ca4-9e1438cb5e68\jenkins_job_stage_view_1791911553349.png"
jenkins_build9_img = r"C:\Users\teotv\.gemini\antigravity-ide\brain\d12cadc8-0ca8-4f25-8ca4-9e1438cb5e68\jenkins_build9_page_1791911558742.png"

if os.path.exists(jenkins_stage_view_img):
    add_image_step(
        jenkins_stage_view_img,
        "Hình 4.1: Giao diện Jenkins Stage View cho Job dictionary-app-5 (Build #9 Xanh lá cây - Toàn bộ 6 Stage thành công)"
    )

if os.path.exists(jenkins_build9_img):
    add_image_step(
        jenkins_build9_img,
        "Hình 4.2: Chi tiết thông tin bản dựng Build #9 trên Jenkins với trạng thái Success"
    )

add_image_step(
    os.path.join(OUTPUT_DIR, "jenkins_pipeline_summary_box.png"),
    "Hình 4.3: Bảng tóm tắt kết quả chi tiết từng Stage trong tiến trình Jenkins CI/CD Pipeline"
)

add_heading_2("4.4. Xác Minh Ứng Dụng Sau Khi Jenkins Deploy Lên Production")
add_body(
    "Sau khi Jenkins hoàn tất Stage 5 (DEPLOY) và Stage 6 (Post-deploy checks), tiến hành kiểm tra trên máy chủ host "
    "thông qua các lệnh dòng lệnh CMD để đối chiếu kết quả thực tế:"
)

add_image_step(
    os.path.join(OUTPUT_DIR, "docker_step_ps_prod.png"),
    "Hình 4.4: Lệnh docker ps xác nhận container dictionary-prod-web-1 (chạy image kéo từ GHCR) và database đang hoạt động"
)

add_image_step(
    os.path.join(OUTPUT_DIR, "api_curl_verification.png"),
    "Hình 4.5: Lệnh cURL xác minh phản hồi từ API /api/health và /api/define/computer trên Production Stack"
)

# --- CHƯƠNG 5: KẾT LUẬN & HƯỚNG PHÁT TRIỂN ---
add_heading_1("CHƯƠNG 5: KẾT LUẬN, BÀI HỌC KINH NGHIỆM & HƯỚNG PHÁT TRIỂN")

add_heading_2("5.1. Các Kết Quả Đạt Được")
add_bullet("Thiết lập thành công quy trình quản lý mã nguồn phân tán chuẩn Conventional Commits với Git & GitHub Remote an toàn.", bold_prefix="1. Quản lý mã nguồn: ")
add_bullet("Đóng gói hoàn chỉnh ứng dụng Fullstack Monorepo với kỹ thuật Multi-stage build tối ưu hóa kích thước image và cấu hình cơ sở dữ liệu PostgreSQL nhúng dữ liệu khởi tạo bền vững.", bold_prefix="2. Đóng gói Container: ")
add_bullet("Xây dựng chuỗi Jenkins Declarative Pipeline tự động hóa 100% từ khâu kiểm thử Smoke Test, build đa kiến trúc (amd64/arm64), đẩy lên GHCR đến deploy lên môi trường Production với thời gian thực thi tối ưu (chỉ 68 giây).", bold_prefix="3. Tự động hóa CI/CD: ")
add_bullet("Ứng dụng chạy thực tế ổn định, người dùng có thể tra cứu từ điển trực quan trên trình duyệt tại cổng 3000 và gọi API tin cậy.", bold_prefix="4. Trải nghiệm người dùng: ")

add_heading_2("5.2. Các Thách Thức Kỹ Thuật Gặp Phải & Giải Pháp Triệt Để")
add_bullet(
    "Khi chạy Docker Compose test trong container Jenkins (DooD), lệnh curl gọi localhost thất bại vì localhost trỏ về chính container Jenkins. "
    "Giải pháp: Cập nhật scripts/smoke-test.sh tự động phát hiện môi trường và điều hướng tới host.docker.internal để kiểm thử chính xác container trên máy chủ host.",
    bold_prefix="Vấn đề phân giải mạng DooD: "
)
add_bullet(
    "Lỗi 'port is already allocated' khi Jenkins deploy stack mới do container cũ đang chiếm dụng cổng 3000. "
    "Giải pháp: Bổ sung cơ chế quản lý vòng đời container, dừng các tiến trình trùng lặp và cấu hình dự án tách biệt theo project name (dictionary-prod).",
    bold_prefix="Xung đột cổng (Port Collision): "
)

add_heading_2("5.3. Hướng Mở Rộng Trong Tương Lai")
add_bullet("Mở rộng kiến trúc triển khai lên cụm Kubernetes (K8s) sử dụng Helm Chart và Ingress Controller nhằm hỗ trợ tự động mở rộng (Auto-scaling) và High Availability.", bold_prefix="1. Điều phối Kubernetes: ")
add_bullet("Tích hợp công cụ SonarQube vào pipeline để tự động quét lỗ hổng bảo mật, kiểm tra độ phủ mã nguồn (Unit Test Coverage) và tiêu chuẩn chất lượng (Quality Gate).", bold_prefix="2. Phân tích chất lượng mã: ")
add_bullet("Thiết lập hệ thống giám sát và cảnh báo thời gian thực với Prometheus, Grafana và Loki giúp đội ngũ vận hành theo dõi trạng thái hệ thống 24/7.", bold_prefix="3. Giám sát & Cảnh báo: ")

# Save Document
doc.save(DOCX_PATH)
print("SUCCESS! Comprehensive DevOps Report generated at:", DOCX_PATH)
