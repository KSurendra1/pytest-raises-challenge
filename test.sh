#!/bin/bash
set -e

export PYTHONPATH=/app/pytest/src:$PYTHONPATH

case "$1" in
  base)
    pytest tests/base
    ;;
  new)
    pytest tests/new
    ;;
  *)
    echo "Usage: ./test.sh {base|new}"
    exit 1
    ;;
esac
