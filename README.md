# AI Feature Store Agent

A feature-discovery API that exposes freshness, quality, and lineage metadata so an agent can reason about feature readiness.

## Run
```bash
pip install -e '.[dev]'
uvicorn app.main:app --reload
```

## Production extensions
Connect Feast or a managed feature store, feature registry metadata, lineage APIs, online/offline stores, freshness SLAs, and model-serving checks.
