# How to use this boilerplate


1. Git clone https://github.com/vacchiano/django-launch.git
2. `docker compose up -d --build`
3. `docker compose exec web python manage.py migrate`
4. Code away


To add a new app - a personal blog for example, run 

`docker compose exec web python manage.py startapp blog`

Replace blog with whatever the name of the project you are starting. Also, to run any of the Django commands or pipenv install new packages you have to start with "docker compose exec web" - where exec stands for execute and web is the name of the service you defined in the docker-compose.yml file.