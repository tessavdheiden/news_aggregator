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

```cd``` into the directory and launch the app via uvicorn:
 
```console
$ uvicorn application:app --reload
```

## Check it
Open your browser at <a href="http://127.0.0.1:8000/pages/bbc-news/0" class="external-link" target="_blank">http://127.0.0.1:8000/pages/bbc-news/0</a>

You will see the JSON response as:

```JSON
{
"document_id":0,
"summary":"Brief description of a newspage"
}
```

Feel free to select a different page: "cnn" or "fox-news" together with some id: 0..10.

## Tests

If you wanna run the test, run following command:

```
$python -m unittest discover -s tests -p '*_test.py'
```


