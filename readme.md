# danjgorestandtest

To Run
1. docker build -t danjgo:latest .
2. docker run --rm -d -p 127.0.0.1:\<openPort\>:8000 -v <full/path/to/project>:/usr/src/app danjgo:latest
3. In a web browser navigate to 127.0.0.1:\<openPort\>/admin
    - username: admin
    - password: password
Now you can use the REST API to add, update, delete and view users using the following urls:
    127.0.0.1:\<openPort\>/users
    127.0.0.1:\<openPort\>/users/<pk> - where pk is the id of the user

To Run Tests
1. docker ps - get container id
2. docker exec -it <container-id> bash
3. python manage.py test
4. coverage run --source='user' manage.py test
5. coverage report
6. coverage html
Now you can view the coverage report in htmlcov/index.html