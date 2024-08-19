#! /bin/sh

# Uncomment RELOAD or WORKERS in .docker-env-local to run as a reloadable uvicorn app, or an app with only uvicorn workers
if [ -n "$RELOAD" ] || [ -n "$WORKERS" ]; then
    # WORKERS flag is ignored if RELOAD is set
    exec uvicorn fastapi1.app:app --host 0.0.0.0 --port 8000 $RELOAD $WORKERS --use-colors
else
    # Comment out both RELOAD and WORKERS to run with gunicorn (deployed-like state)
    exec gunicorn fastapi1.app:app -b 0.0.0.0:8000 -k uvicorn_worker.UvicornWorker -w $WORKER_COUNT
fi