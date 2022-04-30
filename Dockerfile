FROM alpine:latest
RUN apk update
RUN apk add bash python3 py3-pip
RUN pip install requests
COPY macaddress.py /
ENTRYPOINT ["python3", "macaddress.py"]