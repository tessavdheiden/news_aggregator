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
Please go to [Search](http://127.0.0.1:8000/search) and enter a search term to obtain newspages and their summaries.
 
```JSON
{
"document_id":0,
"summary":"Brief description of a newspage"
}
```


Alternatively, check your browser at for a table of news pages and summaries:

- [BBC News](http://127.0.0.1:8000/sources/bbc-news)
- [CNN](http://127.0.0.1:8000/sources/cnn)
- [Tech crunch](http://127.0.0.1:8000/sources/techcrunch)

Here you will see a table of summary and title of headlines for these source papers. 
You will see the JSON response as:

## Tests

If you wanna run the test, run following command:

```
$python -m unittest discover -s tests -p '*_test.py'
```


