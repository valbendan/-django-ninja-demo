from django.urls import path
from ninja import NinjaAPI

# Create your views here.


api = NinjaAPI(urls_namespace="api:demo")


@api.get("hello")
def hello(request):
    return {"hello": "bug"}


urls = (
    [
        path("api/", api.urls, name="demo")
    ],
    "demo"
)
