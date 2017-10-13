FROM python:3.6-alpine
ADD . /code
WORKDIR /code
RUN apk add --no-cache bash
RUN pip install -r requirements.txt
CMD ["python", "app.py"]