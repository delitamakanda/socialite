# socialite
![logo](https://codeship.com/projects/fda370c0-da6c-0134-0795-3a4993b56c58/status?branch=master)

work in progress

## Resources
* [book](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world/page/5)


## commands
* python manage.py db init
* python manage.py db migrate -m <migration example>
* python manage.py db upgrade

## generate fake data with forgerypy
* python manage.py shell
* User.generate_fake(100)
* Post.generate_fake(100)

## testing webservices httpie
* http --json --auth <email>:<password> POST http://127.0.0.1:5000/api/v1.0/posts/ "body=test post"
* http --json --auth : GET http://127.0.0.1:5000/api/v1.0/users/34/timeline/
* http --auth <email>:<password> --json GET http://127.0.0.1:5000/api/v1.0/token

## flask flat pages
[flat pages](https://pythonhosted.org/Flask-FlatPages/)
