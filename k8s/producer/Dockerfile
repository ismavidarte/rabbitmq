FROM python:3
ADD producer.py /
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD [ "python", "./producer.py" ]