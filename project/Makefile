compose-up:
	docker-compose -f docker-compose.yml up --remove-orphans -d

compose-down:
	docker-compose -f docker-compose.yml down

docker-build:
	docker build --platform linux/amd64 -t "astrviktor/translator-bot:0.0.4" \
		-f ./Dockerfile .

docker-push:
	docker push astrviktor/translator-bot:0.0.4

