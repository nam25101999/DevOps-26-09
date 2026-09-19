#!/bin/bash
# ============================================================
# VIDEO DEMO SCRIPT - Linux Commands cho DevOps
# Dùng để record terminal với asciinema hoặc script
# ============================================================

# Cài asciinema nếu chưa có
# sudo apt install asciinema

OUTPUT_DIR="/tmp/devops-linux-demo"
rm -rf $OUTPUT_DIR
mkdir -p $OUTPUT_DIR
cd $OUTPUT_DIR

clear
echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                                                              ║"
echo "║     🐧 LINUX COMMANDS CHO DEVOPS - VIDEO DEMO 🐧            ║"
echo "║                  nam@KhanhLinh | Ubuntu WSL2                 ║"
echo "║                                                              ║"
echo "╚══════════════════════════════════════════════════════════════╝"
sleep 2

# ──────────────────────────────────────────
echo ""
echo "┌─────────────────────────────────────────────┐"
echo "│  📌 PHẦN 1: LỆNH CƠ BẢN                    │"
echo "└─────────────────────────────────────────────┘"
sleep 1

echo ""; echo "# Xem thư mục hiện tại"
sleep 0.5
echo "$ pwd"; pwd
sleep 1

echo ""; echo "# Xem user hiện tại"
sleep 0.5
echo "$ whoami"; whoami
sleep 1

echo ""; echo "# Xem tên máy"
sleep 0.5
echo "$ hostname"; hostname
sleep 1

echo ""; echo "# Xem ngày giờ"
sleep 0.5
echo "$ date"; date
sleep 1

echo ""; echo "# Thông tin hệ điều hành"
sleep 0.5
echo "$ uname -a"; uname -a
sleep 1

echo ""; echo "# In nội dung ra màn hình"
sleep 0.5
echo '$ echo "Hello DevOps! 🚀"'
echo "Hello DevOps! 🚀"
sleep 1

echo ""; echo "# Tìm vị trí bash"
sleep 0.5
echo "$ which bash"; which bash
sleep 1

echo ""; echo "# Tìm python3"
sleep 0.5
echo "$ whereis python3"; whereis python3
sleep 1

echo ""; echo "# Xem loại lệnh ls"
sleep 0.5
echo "$ type ls"; type ls
sleep 2

# ──────────────────────────────────────────
echo ""
echo "┌─────────────────────────────────────────────┐"
echo "│  📁 PHẦN 2: QUẢN LÝ THƯ MỤC               │"
echo "└─────────────────────────────────────────────┘"
sleep 1

echo ""; echo "# Tạo cấu trúc project DevOps"
sleep 0.5
echo "$ mkdir -p project/{backend,frontend,database,docs}"
mkdir -p $OUTPUT_DIR/project/{backend,frontend,database,docs}
sleep 0.5

echo "$ ls project/"
ls $OUTPUT_DIR/project/
sleep 1

echo ""; echo "# Di chuyển thư mục"
echo "$ cd project && pwd"
cd $OUTPUT_DIR/project && pwd
sleep 0.5
echo "$ cd .. && pwd"
cd .. && pwd
sleep 0.5
echo "$ cd ~ && pwd"
cd ~ && pwd
sleep 1

echo ""; echo "# Tạo thư mục nested"
echo "$ mkdir -p nested/level1/level2/level3"
mkdir -p $OUTPUT_DIR/nested/level1/level2/level3
find $OUTPUT_DIR/nested -type d
sleep 2

# ──────────────────────────────────────────
echo ""
echo "┌─────────────────────────────────────────────┐"
echo "│  📄 PHẦN 3: QUẢN LÝ FILE                   │"
echo "└─────────────────────────────────────────────┘"
sleep 1

cd $OUTPUT_DIR

echo ""; echo "# Tạo file"
echo "$ touch file.txt readme.txt config.yml"
touch file.txt readme.txt config.yml
ls -la *.txt *.yml
sleep 1

echo ""; echo "# Ghi nội dung vào file"
echo '$ echo "Hello DevOps!" > file.txt'
echo "Hello DevOps!" > file.txt
echo "Line 2: Học Linux cơ bản" >> file.txt
echo "Line 3: Thực hành lệnh" >> file.txt
echo "Line 4: WSL Ubuntu 22.04" >> file.txt
echo "Line 5: DevOps Journey 🚀" >> file.txt
echo "$ cat file.txt"
cat file.txt
sleep 1

echo ""; echo "# Copy file"
echo "$ cp file.txt backup.txt"
cp file.txt backup.txt
ls -la *.txt
sleep 0.5

echo ""; echo "# Copy folder"
echo "$ cp -r project project-backup"
cp -r project project-backup
ls -la | grep project
sleep 1

echo ""; echo "# Đổi tên file"
echo "$ mv readme.txt readme-renamed.txt"
mv readme.txt readme-renamed.txt
ls -la *.txt
sleep 1

echo ""; echo "# Xóa file"
echo "$ rm backup.txt"
rm backup.txt
ls -la *.txt
sleep 2

# ──────────────────────────────────────────
echo ""
echo "┌─────────────────────────────────────────────┐"
echo "│  👀 PHẦN 4: ĐỌC FILE                       │"
echo "└─────────────────────────────────────────────┘"
sleep 1

# Tạo bigfile
for i in $(seq 1 25); do
    echo "Line $i: DevOps learning - Lệnh Linux số $i" >> bigfile.txt
done

echo ""; echo "# Xem toàn bộ file"
echo "$ cat file.txt"
cat file.txt
sleep 1

echo ""; echo "# Xem 5 dòng đầu"
echo "$ head -n 5 bigfile.txt"
head -n 5 bigfile.txt
sleep 1

echo ""; echo "# Xem 5 dòng cuối"
echo "$ tail -n 5 bigfile.txt"
tail -n 5 bigfile.txt
sleep 1

echo ""; echo "# Đếm số dòng"
echo "$ wc -l bigfile.txt"
wc -l bigfile.txt
sleep 2

# ──────────────────────────────────────────
echo ""
echo "┌─────────────────────────────────────────────┐"
echo "│  🔍 PHẦN 5: TÌM KIẾM FILE (find)           │"
echo "└─────────────────────────────────────────────┘"
sleep 1

# Tạo dữ liệu demo
mkdir -p project/backend
echo "spring.datasource.url=jdbc:postgresql://localhost:5432/devdb" > project/backend/application.yml
echo "server.port=8080" >> project/backend/application.yml
echo "DEBUG: Application started" > project/backend/app.log
echo "INFO: Server running on localhost:8080" >> project/backend/app.log
echo "ERROR: Connection refused to database" >> project/backend/app.log
echo "WARN: High memory usage detected" >> project/backend/app.log
touch project/frontend/index.html

echo ""; echo "$ find . -type f"
find $OUTPUT_DIR -maxdepth 3 -type f | head -10
sleep 1

echo ""; echo "$ find . -name '*.yml'"
find $OUTPUT_DIR -name "*.yml"
sleep 1

echo ""; echo "$ find . -name '*.log'"
find $OUTPUT_DIR -name "*.log"
sleep 2

# ──────────────────────────────────────────
echo ""
echo "┌─────────────────────────────────────────────┐"
echo "│  🔎 PHẦN 6: GREP - Tìm kiếm nội dung       │"
echo "└─────────────────────────────────────────────┘"
sleep 1

echo ""; echo "# Tìm ERROR trong log"
echo '$ grep "ERROR" project/backend/app.log'
grep "ERROR" project/backend/app.log
sleep 1

echo ""; echo "# Grep với số dòng"
echo '$ grep -n "localhost" project/backend/app.log'
grep -n "localhost" project/backend/app.log
sleep 1

echo ""; echo "# Grep không phân biệt hoa thường"
echo '$ grep -i "info" project/backend/app.log'
grep -i "info" project/backend/app.log
sleep 1

echo ""; echo "# Grep đệ quy"
echo '$ grep -r "localhost" project/'
grep -r "localhost" project/
sleep 1

echo ""; echo "# Kết hợp pipe với grep"
echo "$ cat app.log | grep ERROR"
cat project/backend/app.log | grep ERROR
sleep 2

# ──────────────────────────────────────────
echo ""
echo "┌─────────────────────────────────────────────┐"
echo "│  🏷️  PHẦN 7: ALIAS                          │"
echo "└─────────────────────────────────────────────┘"
sleep 1

echo ""; echo "# Tạo alias"
echo '$ alias ll="ls -la"'
alias ll="ls -la"
sleep 0.5
echo "$ ll"
ls -la | head -8
sleep 1

echo ""; echo "# Xem tất cả alias"
echo "$ alias"
alias | head -5
sleep 1

echo ""; echo "# Xóa alias"
echo "$ unalias ll"
unalias ll
sleep 2

echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║                                                              ║"
echo "║  ✅ HOÀN THÀNH! Tất cả Linux Commands đã được demo!        ║"
echo "║                                                              ║"
echo "║  📸 Screenshots: docs/linux-commands/screenshots/           ║"
echo "║  🎬 Video:       docs/linux-commands/videos/                ║"
echo "║  📖 README:      docs/linux-commands/README.md              ║"
echo "║                                                              ║"
echo "╚══════════════════════════════════════════════════════════════╝"
