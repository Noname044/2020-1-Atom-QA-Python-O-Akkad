FROM python:3.8

ADD /requirements.txt requirements.txt
RUN pip3.8 install -r /requirements.txt

ADD /mock mock

WORKDIR /mock

CMD ["python3","mock.py"]