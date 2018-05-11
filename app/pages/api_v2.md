title: GraphQL API developer docs
date: 2018-05-11
tags: [dev, api, doc, graphql]

## Posts

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
