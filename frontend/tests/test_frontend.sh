#!/bin/bash
set -e
container=$(docker run -d -p 8080:80 frontend:latest)
sleep 2
curl -f http://localhost:8080 || { echo "Frontend not reachable"; exit 1; }
docker rm -f $container
