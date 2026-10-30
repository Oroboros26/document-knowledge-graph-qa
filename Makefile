run:  ## Neo4j only for now (the Airflow DAG and the UI are not built yet)
	docker compose up --build

test:
	ruff check src tests && pytest -q
