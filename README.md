# Scripting assignment - Coding

`docker build -t cisco .`
```
[+] Building 0.3s (9/9) FINISHED                                                          
 => [internal] load build definition from Dockerfile                                 0.0s
 => => transferring dockerfile: 37B                                                  0.0s
 => [internal] load .dockerignore                                                    0.0s
 => => transferring context: 2B                                                      0.0s
 => [internal] load metadata for docker.io/library/alpine:latest                     0.0s
 => [internal] load build context                                                    0.0s
 => => transferring context: 35B                                                     0.0s
 => [1/4] FROM docker.io/library/alpine:latest                                       0.0s
 => CACHED [2/4] RUN apk add bash python3 py3-pip                                    0.0s
 => CACHED [3/4] RUN pip install requests                                            0.0s
 => CACHED [4/4] COPY macaddress.py /                                                0.0s
 => exporting to image                                                               0.0s
 => => exporting layers                                                              0.0s
 => => writing image sha256:f1621d493ef914b299f1dd1fae9f76bafa40822ddc652a707d44441  0.0s
 => => naming to docker.io/library/cisco                                             0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
```
`docker run cisco`

```
macaddress.py <mac address>

Example:
  macaddress.py 14:7d:da:d9:4d:75
```
`docker run cisco 14:7d:da:d9:4d:75`
```
Apple, Inc
```