up:
	docker compose up -d

down:
	docker compose down

migrate:
	alembic upgrade head

migrate-create:
	alembic revision --autogenerate -m "$(name)"

run:
	uvicorn app.main:app --reload
