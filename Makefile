install:
	pip3 install -r requirements.txt

# Linters
format: black isort

black:
	black --line-length 120 .

isort:
	isort .
