FROM python:3-slim-buster
COPY . /python-flask
WORKDIR /python-flask
RUN pip install -r requirement.txt
ENTRYPOINT ["python","mcq.py"]
