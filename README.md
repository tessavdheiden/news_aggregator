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
Please go to [Text](http://127.0.0.1:8000/summarize/corona) and obtain a table with summaries.

Please go to [Search](http://127.0.0.1:8000/search) and enter a search term to obtain newspages and their summaries.
 
```JSON
{
"document_id":0,
"summary":"Brief description of a newspage"
}
```

Here you will see a table of summary and title of headlines for these source papers. 
You will see the JSON response as:

## Tests

If you wanna run the test, run following command:

```
$python -m unittest discover -s tests -p '*_test.py'
```


