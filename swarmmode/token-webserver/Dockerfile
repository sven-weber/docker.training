FROM python:alpine
RUN 	apk update && \
        apk upgrade
RUN pip install Flask
COPY server.py /
CMD ["python", "server.py"]
EXPOSE 80