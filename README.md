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
Install dependancies:

```console
$ pip install -r requirements.txt
```

```cd``` into the directory and launch the app via uvicorn:
 
```console
$ FLASK_APP=application/main.py
```

```console
$ flask run --port=8080
```

## Check it
Please go to [API](http://127.0.0.1:8080) and obtain a table with summaries for your entered text.

You will obtain something like:

<img src="Screenshot.png" width="400" />

 
```JSON
{
"document_id":0,
"summary":"Brief description of a newspage"
}
```

## Tests

If you wanna run the test, run following command:

```
$python -m unittest discover -s tests -p '*_test.py'
```


