title: API developer docs
date: 2017-07-11
tags: [dev, api, doc]

For future projects I prepared some api endpoints for Socialite app.

Please feel free to contact us for more documentation.

##### Posts

GET all posts
```
https://the-socialite-app.herokuapp.com/api/v1.0/posts/
```

GET one post
```
https://the-socialite-app.herokuapp.com/api/v1.0/posts/<id>
```

POST one post
```
https://the-socialite-app.herokuapp.com/api/v1.0/posts/
```

PUT one post
```
https://the-socialite-app.herokuapp.com/api/v1.0/posts/<id>
```

##### Comments

GET all comments
```
https://the-socialite-app.herokuapp.com/api/v1.0/comments/
```

GET one comment
```
https://the-socialite-app.herokuapp.com/api/v1.0/comments/<id>
```

GET comment(s) by post
```
https://the-socialite-app.herokuapp.com/api/v1.0/posts/<id>/comments/
```

POST comment by post
```
https://the-socialite-app.herokuapp.com/api/v1.0/posts/<id>/comments/
```


##### Users
GET one user
```
https://the-socialite-app.herokuapp.com/api/v1.0/users/2
```

GET posts by user
```
https://the-socialite-app.herokuapp.com/api/v1.0/users/<id>/posts/
```

GET user by followed posts
```
https://the-socialite-app.herokuapp.com/api/v1.0/users/<id>/timeline/
```
