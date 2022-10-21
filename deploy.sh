#!/bin/bash 
docker stop monxun
docker rm monxun
docker build -t django-monxun .
docker run -d --name monxun -p 8300:8300 django-monxun