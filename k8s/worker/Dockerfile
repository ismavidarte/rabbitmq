FROM python:3
ADD worker.py /
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
CMD [ "python", "./worker.py" ]