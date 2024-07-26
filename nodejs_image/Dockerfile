From ubuntu:20.04
MAINTAINER Docker sheep1221<kmkevin332907@gmail.com>
RUN apt-get update && apt-get install -y python && apt-get install -y curl
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash

RUN export NVM_DIR="$HOME/.nvm" && \
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" && \
    nvm install --lts && \
    nvm alias default node\
    npm install -g express-generator

# Expose the port your app runs on
EXPOSE 3000

RUN echo "Hello, Docker image" > message.txt

CMD ["cat", "message.txt"]
