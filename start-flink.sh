#!/usr/bin/env bash
set -euo pipefail

# Start a local Flink standalone cluster (jobmanager + taskmanager)
BASE_DIR="$(cd "$(dirname "$0")" && pwd)"
FLINK_HOME="${FLINK_HOME:-$BASE_DIR/flink/apache-flink-1.18.1}"

if [[ ! -d "$FLINK_HOME" ]]; then
  echo "Flink not found in $FLINK_HOME"
  echo "Run ./setup.sh to download the Flink distribution or set FLINK_HOME environment variable."
  exit 1
fi

echo "Starting Flink (local standalone) using FLINK_HOME=$FLINK_HOME"
"$FLINK_HOME/bin/start-cluster.sh"
