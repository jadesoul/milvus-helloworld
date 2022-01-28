HOST_IP=$(ifconfig en0 | grep netmask | cut -d ' ' -f 2)
docker run -p 8000:3000 -e HOST_URL=http://${HOST_IP}:8000 -e MILVUS_URL=${HOST_IP}:19530 -it zilliz/attu:latest
open http://${HOST_IP}:8000
