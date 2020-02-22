DEPLOY_DIR = deployment/docker

.PHONY: run stop cleanup

run:
	docker-compose -f $(DEPLOY_DIR)/docker-compose.yml up

stop:
	docker-compose -f $(DEPLOY_DIR)/docker-compose.yml stop

cleanup:
	docker-compose -f $(DEPLOY_DIR)/docker-compose.yml down --rmi all -v

test:
	pytest -vv --cov=app --cov-report=term-missing
