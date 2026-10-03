#!/usr/bin/env bash
set -euo pipefail

# ===================================================================
# Smoke Test Script cho Pipeline Jenkins (Stage 2. TEST)
# ===================================================================

BUILD_NUM="${BUILD_NUMBER:-local}"
PROJECT_NAME="smoke-test-${BUILD_NUM}"
PORT="${SMOKE_WEB_PORT:-3999}"
DB_PORT="${SMOKE_DB_PORT:-55999}"
TARGET_IMAGE="${SMOKE_IMAGE:-ghcr.io/linh16122005/dictionary-app-5:latest}"

echo "====================================================="
echo "Bắt đầu Smoke Test"
echo "Project Name : ${PROJECT_NAME}"
echo "Test Image   : ${TARGET_IMAGE}"
echo "Web Port     : ${PORT}"
echo "====================================================="

cleanup() {
  echo "--- Dọn dẹp container smoke test ---"
  docker compose -p "${PROJECT_NAME}" down -v --remove-orphans || true
}
trap cleanup EXIT

echo "--- Đang khởi chạy stack smoke test ---"
IMAGE_TAG="${TARGET_IMAGE}" \
WEB_PORT="${PORT}" \
DB_PORT="${DB_PORT}" \
POSTGRES_USER=dictuser \
POSTGRES_PASSWORD=dictpass \
POSTGRES_DB=dictionary \
docker compose -p "${PROJECT_NAME}" \
  -f docker-compose.yml \
  -f docker-compose.prod.yml \
  up -d --remove-orphans

echo "--- Đang kiểm tra phản hồi từ ứng dụng (tối đa 30 giây) ---"
HEALTH_URL="http://localhost:${PORT}/api/health"
PASSED=false

for i in $(seq 1 30); do
  if curl -sf "${HEALTH_URL}" >/dev/null 2>&1; then
    echo "SUCCESS: App phản hồi sau ${i}s tại ${HEALTH_URL}"
    PASSED=true
    break
  fi
  sleep 1
done

if [ "${PASSED}" = true ]; then
  echo "--- Testing endpoint /api/define/computer ---"
  curl -s "http://localhost:${PORT}/api/define/computer" || true
  echo ""
  echo "====================================================="
  echo "SMOKE TEST THÀNH CÔNG!"
  echo "====================================================="
  exit 0
else
  echo "====================================================="
  echo "SMOKE TEST THẤT BẠI - App không phản hồi sau 30s!"
  echo "====================================================="
  docker compose -p "${PROJECT_NAME}" logs
  exit 1
fi
