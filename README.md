# docker-consule-template-haproxy

This repository contains a basic docker-compose based environment which tests the interaction of consul, regstirator, haproxy, consul-template and a simple web-based backend service.

The simple test case queries haproxy and expects a '200 OK' response back from a back-end which haprox proxies the request to.

The haproxy configuration is generated using consul-template.

# Basic Usage

```
$ docker-compose up --build -d && docker logs test-client
```

If successful, this should result in output similar to the following:

```
============================= test session starts ==============================
platform linux2 -- Python 2.7.12, pytest-3.0.3, py-1.4.31, pluggy-0.4.0
rootdir: /tmp, inifile: 
collected 2 items

tmp/test_http.py ..

=========================== 2 passed in 0.06 seconds ===========================
```
