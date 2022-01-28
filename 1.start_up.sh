test -f docker-compose.yml || wget https://github.com/milvus-io/milvus/releases/download/v2.0.0/milvus-standalone-docker-compose.yml -O docker-compose.yml

docker-compose up -d
docker-compose ps