from django.shortcuts import render
import _json
from django.http import jsanresponse
from.models import 


def register(req):
    if req.method == "POST":
        data=_json.loads(req.body)
        nm=data.get('email')
        models.users.objects.create(
            name=nm
        )



        return jsanresponse({'message':'successfully registered'},status=200)
        return jsanresponse({'message':'failed'},status=500)