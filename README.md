# socialite app [![Build Status](https://travis-ci.org/delitamakanda/socialite.svg?branch=master)](https://travis-ci.org/delitamakanda/socialite)

*work in progress*

## commands

```bash
 pip install -r requirements-dev.txt
```

```bash
python manage.py db init
python manage.py db migrate -m <migration example>
python manage.py db upgrade
```

## generate fake data with forgerypy
```bash
python manage.py shell
User.generate_fake(100)
Post.generate_fake(100)
```

## testing webservices httpie
```bash
http --json --auth <email>:<password> POST http://127.0.0.1:5000/api/v1.0/posts/ "body=test post"
http --json --auth : GET http://127.0.0.1:5000/api/v1.0/users/34/timeline/
http --auth <email>:<password> --json GET http://127.0.0.1:5000/api/v1.0/token
```
