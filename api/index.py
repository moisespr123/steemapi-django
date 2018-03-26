from django.http import HttpResponse

def index(request):
    return HttpResponse('<head> \
                        <title>STEEM Web API Documentation</title> \
                        </header> \
                        <h1>STEEM Web API Documentation</h1> \
                        <a href=https://steemit.com/technology/@moisesmcardona/steemplace-api>Post #1</a><br> \
                        \
                        <h2>MORE TO COME!!!</h2>\
                        Follow me on Steemit: <a href=https://steemit.com/@moisesmcardona>https://steemit.com/@moisesmcardona</a> \
                        \
                        <h3>Also, vote me for Witness!</h3> \
                        <a href=https://v2.steemconnect.com/sign/account-witness-vote?witness=moisesmcardona&approve=1>Click here to vote me by using SteemConnect 🙂</a>')