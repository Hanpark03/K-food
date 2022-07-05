# pull official base image
FROM node:16-alpine3.15

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
#ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
# add app
COPY . ./
RUN yarn install

RUN yarn install
# start app
CMD ["yarn", "start"]