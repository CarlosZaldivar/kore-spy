FROM python:3.9-slim-buster

RUN apt-get update
RUN apt-get install tcpdump python3-dev -y

COPY requirements.txt /usr/src/app/
RUN pip3 install --no-cache-dir -r /usr/src/app/requirements.txt

COPY main.py /usr/src/app

CMD ["-u", "/usr/src/app/main.py"]
ENTRYPOINT ["python3"]