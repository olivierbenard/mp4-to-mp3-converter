black:
	poetry run black mp4_to_mp3_converter/

mypy:
	poetry run mypy mp4_to_mp3_converter/

pylint:
	poetry run pylint mp4_to_mp3_converter/

test:
	poetry run pytest -vvs tests/

checks: black mypy pylint test
