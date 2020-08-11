# News aggregator

A request would look like:

```
  POST / HTTP/1.1
  Accept: application/json
  Content-Type: application/x-www-form-urlencoded
 
  text=This+is+a+long+text
```

This endpoint returns an id of a document, which can be used to request a summary and second endpoint returns a summary.


The response of this endpoint should be something like:

```
  HTTP/1.1 200 OK

  Content-Type: application/json
  {
    "document_id": "example_id",
    "summary": "This is the summary"
  }
```
 
## Steps
Install dependencies:

```console
$ pip install -r requirements.txt
```

```cd``` into the directory and launch the app via:
 
```console
$ FLASK_APP=app
```

```console
$ flask run --port=8080
```

```console
$ curl -H "Content-Type: application/json" -X POST -d '{"text": "This is a large text. It should be summarized."}' 
http://localhost:5000/api/documents/
```


## Tests

If you wanna run the test, run following command:

```
$python -m unittest discover -s tests -p '*_test.py'
```


