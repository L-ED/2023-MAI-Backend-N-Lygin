#! /bin/bash

set -o errexit
# set -o pipefail
set -o nounset

readonly WORKERS_CNT=4

main() {
  if ! gunicorn --workers 4 backend.app:app ; then
    echo "Failed to run gunicorn..."
    return 1
  fi
}

main $@