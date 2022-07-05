$var = ((docker container ls | sls -pattern "kfood-api") -split '\s')[0]
docker rm -f $var
docker rmi -f kfood-api
docker build -f ./Dockerfile -t kfood-api .
docker run --name kfood-api -p 8080:8080 kfood-api