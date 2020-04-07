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


```JSON
  {
    "document_id": "example_id",
    "summary": "This is the summary"
  }
```
 
## Steps

Load server:
```console
$ uvicorn main_send:app --reload
```

Run main_send.py:
```console
$ python main_send.py
```

Test if news is retrieved and summarized:
```console
$ python main_recieve.py
```


## Tests

If you wanna run the test, run following command:

```
$python -m unittest discover -s <directory/>tests -p '*_test.py'
```


