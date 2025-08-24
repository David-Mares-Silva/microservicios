install:
	pip install --upgrade pip && \
		pip install -r requirements.txt 

install-gpc:
	pip install --upgrade pip && \
		pip install -r requirements-gpc.txt && \
		pip install git+

install-aws:
	pip install --upgrade pip && \
		pip install -r requirements-aws.txt && \
		pip install git+

install-azure:
	pip install --upgrade pip && \
		pip install -r requirements-azure.txt && \
		pip install git+

lint:
	pylint --disable=R,C --exit-zero $$(find . -type f -name "*.py")
#$$(find . -type f -name "*.py") || true --exit-zero
# pylint --disable=R,C 020_api/flask_intro.py  || true

format:
	black *.py

