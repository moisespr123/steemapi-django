from django.http import HttpResponse
from steem import Steem
import json

def index(request):
    try:
        s = Steem(nodes=["https://api.steemit.com"])
        try:
            balance = s.get_account(request.GET['a'])['sbd_balance']
        except:
            balance = '0.000 SBD'
        return HttpResponse(balance, content_type='text/plain')
    except:
        return HttpResponse("To use this API call, please supply param a=accountname, substituting accountname with the account to see the account SBD Balance.\n\n"
                            'Example: https://api.steem.place/getSBDBalance/?a=moisesmcardona\n\n'
                            'Returns: account SBD balance', content_type='text/plain')