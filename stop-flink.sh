#!/usr/bin/env bash
set -euo pipefail

BASE_DIR="$(cd "$(dirname "$0")" && pwd)"
FLINK_HOME="${FLINK_HOME:-$BASE_DIR/flink/apache-flink-1.18.1}"

if [[ ! -d "$FLINK_HOME" ]]; then
  echo "Flink not found in $FLINK_HOME"
  exit 1
fi

echo "Stopping Flink (local standalone) using FLINK_HOME=$FLINK_HOME"
"$FLINK_HOME/bin/stop-cluster.sh"
