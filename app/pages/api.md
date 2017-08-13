title: API developer docs
date: 2017-07-11
tags: [dev, api, doc]

For future projects i prepare some api endpoint for Socialite app.

Please feel free to contact us for more documentation.

##### Posts

GET all posts
```
http://127.0.0.1:5000/api/v1.0/posts/
```

GET one post
```
http://127.0.0.1:5000/api/v1.0/posts/<id>
```

POST one post
```
http://127.0.0.1:5000/api/v1.0/posts/
```

PUT one post
```
http://127.0.0.1:5000/api/v1.0/posts/<id>
```

##### Comments

GET all comments
```
http://127.0.0.1:5000/api/v1.0/comments/
```

GET one comment
```
http://127.0.0.1:5000/api/v1.0/comments/<id>
```

GET comment(s) by post
```
http://127.0.0.1:5000/api/v1.0/posts/<id>/comments/
```

POST comment by post
```
http://127.0.0.1:5000/api/v1.0/posts/<id>/comments/
```


##### Users
GET one user
```
http://127.0.0.1:5000/api/v1.0/users/2
```

GET posts by user
```
http://127.0.0.1:5000/api/v1.0/users/<id>/posts/
```

GET user by followed posts
```
http://127.0.0.1:5000/api/v1.0/users/<id>/timeline/
```
