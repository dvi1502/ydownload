FROM python:3.12-slim-bookworm
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000
CMD ["python", "-m", "ydownload"]
