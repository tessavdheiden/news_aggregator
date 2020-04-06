# News aggregator

A request would look like:

```
  POST / HTTP/1.1
  Accept: application/json
  Content-Type: application/x-www-form-urlencoded
 
  text=This+is+a+long+text
```

This endpoint returns an id of a document, which can be used to request a summary.

A second endpoint returns a summary, which looks like:


```
  HTTP/1.1 200 OK
  Content-Type: application/json
   
  {
    "document_id": "example_id",
    "summary": "This is the summary"
  }
```
 
## Steps

