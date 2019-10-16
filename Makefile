.PHONY: dep lint build run clean

dep:
	@pip install -r requirements.txt -r requirements-dev.txt

lint:
	@pylama src/

build:
	@:

run: build
	@python src/main.py

clean:
	@:
