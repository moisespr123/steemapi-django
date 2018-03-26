from django.http import HttpResponse
from steem import Steem
import json

def index(request):
    try:
        s = Steem(nodes=["https://api.steemit.com"])
        return HttpResponse(s.get_account(request.GET['a'])['post_count'], content_type='text/plain')
    except:
        return HttpResponse("To use this API call, please supply param a=accountname, substituting accountname with the account to see the account's total post and comments count\n\n"
                            'Example: https://api.steem.place/getPostCount/?a=moisesmcardona\n\n'
                            'Returns: account post count (posts and comments combined)', content_type='text/plain')