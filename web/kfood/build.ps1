$var = ((docker container ls | sls -pattern "kfood-web") -split '\s')[0]
docker rm -f $var
docker rmi -f kfood-web
docker build -f ./Dockerfile -t kfood-web .
docker run --name kfood-web -p 3000:3000 kfood-web