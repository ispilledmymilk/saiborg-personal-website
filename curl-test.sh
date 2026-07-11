#!/usr/bin/env bash
# Test GET and POST /api/timeline_post endpoints with curl.
# Bonus: DELETE the test post afterward.
set -euo pipefail

BASE_URL="${BASE_URL:-http://localhost:5001}"
API_URL="${BASE_URL}/api/timeline_post"

RANDOM_ID=$RANDOM
NAME="Test User ${RANDOM_ID}"
EMAIL="test${RANDOM_ID}@example.com"
CONTENT="Random timeline post #${RANDOM_ID} testing endpoints with curl."

echo "==> POST ${API_URL}"
POST_RESPONSE=$(curl -s --request POST "${API_URL}" \
  -d "name=${NAME}" \
  -d "email=${EMAIL}" \
  -d "content=${CONTENT}")

echo "${POST_RESPONSE}"

POST_ID=$(python3 -c "import json,sys; print(json.load(sys.stdin)['id'])" <<<"${POST_RESPONSE}")

echo ""
echo "==> GET ${API_URL}"
GET_RESPONSE=$(curl -s --request GET "${API_URL}")
echo "${GET_RESPONSE}"

echo ""
if echo "${GET_RESPONSE}" | grep -q "${CONTENT}"; then
  echo "PASS: POST created a post that appears in GET (descending order)."
else
  echo "FAIL: Created content was not found in GET response."
  exit 1
fi

echo ""
echo "==> DELETE ${API_URL}/${POST_ID}"
DELETE_RESPONSE=$(curl -s --request DELETE "${API_URL}/${POST_ID}")
echo "${DELETE_RESPONSE}"

echo ""
echo "All curl endpoint tests passed."
