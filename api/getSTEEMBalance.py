from django.http import HttpResponse
from steem import Steem
import json

def index(request):
    try:
        s = Steem(nodes=["https://api.steemit.com"])
        try:
            balance = s.get_account(request.GET['a'])['balance']
        except:
            balance = '0.000 STEEM'
        return HttpResponse(balance, content_type='text/plain')
    except:
        return HttpResponse("To use this API call, please supply param a=accountname, substituting accountname with the account to see the account STEEM Balance.\n\n"
                            'Example: https://api.steem.place/getSTEEMBalance/?a=moisesmcardona\n\n'
                            'Returns: account STEEM balance', content_type='text/plain')