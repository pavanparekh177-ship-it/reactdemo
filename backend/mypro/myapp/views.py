from django.shortcuts import render
import _json
from django.http import jsanresponse
from.models import


def register(req):
    if req.method == "POST":
        data=_json.loads(req.body)
        nm=data.get('email')
        Users.Objects.create(
            name=nm
        )



        return jsanresponse({'message':'successfully registered'},status=200)
        return jsanresponse({'message':'failed'},status=500)
    

    def login (req):
    if req.method == "POST":
        data=_json.loads(req.body)
        email=data.get('email')
        pwd=data.get('pwd')
        print(email,pwd)
        users.Objects.get(
            name=eamail,password=pwd
        )



        return jsanresponse({'message':'successfully login'},status=200)
        return jsanresponse({'message':'login failed'},status=20)
    
    def Data(req):
        D=users.objects_by().values('id','name','password')[:1]
        return jsanresponse(list(D),safe=False)