#!/usr/bin/env bash
# One-time setup on macOS or Ubuntu: Python packages, mdb-tools and poppler, and a pgvector database in Docker.
set -euo pipefail
cd "$(dirname "$0")"
python3 -m pip install -r requirements.txt pytest
if command -v brew >/dev/null; then brew install mdbtools poppler
elif command -v apt-get >/dev/null; then sudo apt-get install -y mdbtools poppler-utils
else echo "install mdb-tools and poppler (pdftotext) with your package manager"; fi
if command -v docker >/dev/null; then docker compose up -d db && echo 'database: DB="postgresql://grounding:grounding@localhost:5433/taxground"'
else echo "no Docker: use any PostgreSQL 14+ with the pgvector extension (CREATE EXTENSION vector) and set DB to it"; fi
