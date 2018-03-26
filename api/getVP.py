from django.http import HttpResponse
from steem import Steem
import json

def index(request):
    try:
        s = Steem(nodes=["https://api.steemit.com"])
        try:
            VP = s.get_account(request.GET['a'])['voting_power'] / 100
        except:
            VP = 0
        return HttpResponse(VP, content_type='text/plain')
    except:
        return HttpResponse("To use this API call, please supply param a=accountname, substituting accountname with the account to see the account Voting Power.\n\n"
                            'Example: https://api.steem.place/getVP/?a=moisesmcardona\n\n'
                            'Returns: account Voting Power', content_type='text/plain')