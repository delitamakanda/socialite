title: GraphQL API developer docs
date: 2018-05-11
tags: [dev, api, doc, graphql]

## Query all posts

```
/api/v2.0/posts
```

```
query {
  allPosts{
    edges{
      node{
        id,
        body,
        timestamp,
        authorId,
        bodyHtml
      }
    }
  }
}
```


## Query one post

```
{
  node(id: "UG9zdDox") {
    ... on Post {
      id,
      timestamp,
      authorId,
      body,
      bodyHtml
    }
  }
}
```
