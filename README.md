# django-ninja bug demo

This repo is for reproduce the bug in the [issue](https://github.com/vitalik/django-ninja/pull/57)

## step to produce:

* run `poetry update` # install dep
* run `make run` # run the django server
* use browser to visit: [url](http://127.0.0.1:8000/api/api/docs)

the browser will display:

```text
NoReverseMatch at /api/api/docs

'api' is not a registered namespace inside 'api'
```

After apply the fix, it will properly render the doc
