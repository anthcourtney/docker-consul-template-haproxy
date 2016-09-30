FROM alpine:3.4

RUN apk --update add python py-pip && \
    pip install pytest requests
ADD test_http.py /tmp

CMD ["pytest", "/tmp"]
