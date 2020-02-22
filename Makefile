DEPLOY_DIR = deployment/development

.PHONY: run run_docker stop_docker cleanup_docker

run:
	gunicorn app.manage:app -c app/config/gunicorn_setting.py

run_docker:
	docker-compose -f $(DEPLOY_DIR)/docker-compose.yml up

stop_docker:
	docker-compose -f $(DEPLOY_DIR)/docker-compose.yml stop

cleanup_docker:
	docker-compose -f $(DEPLOY_DIR)/docker-compose.yml down --rmi all -v

test:
	pytest -vv --cov=app --cov-report=term-missing
