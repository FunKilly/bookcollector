CONTAINER ?= "panel-api"

# run
run:
	docker-compose up

# build
build:
	docker-compose build

# lint
lint:
	black --line-length=90 . && isort . && flake8 --max-line-length=120

# Enter the container
bash:
	docker exec -it ${CONTAINER} bash
