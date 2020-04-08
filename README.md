# News aggregator

A request would look like:

```
  POST / HTTP/1.1
  Accept: application/json
  Content-Type: application/x-www-form-urlencoded
 
  text=This+is+a+long+text
```

This endpoint returns an id of a document, which can be used to request a summary and second endpoint returns a summary.

 
## Steps
Install dependancies:

```console
$ pip install -r requirements.txt
```

Run the app via python
```console
$ python run.py
```

## Check it
Open your browser at <a href="http://127.0.0.1:8000/pages/0" class="external-link" target="_blank">http://127.0.0.1:8000/pages/0</a>

You will see the JSON response as:

```JSON
  {
    "document_id": "example_id",
    "summary": "This is the summary"
  }
```

## Tests

If you wanna run the test, run following command:

```
$python -m unittest discover -s tests -p '*_test.py'
```


