# Create the docker container
docker build -t my-telebot . && docker run -d --name my-telebot-container my-telebot && docker stop my-telebot-container && docker rmi my-telebot