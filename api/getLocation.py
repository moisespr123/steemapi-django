from django.http import HttpResponse
from steem import Steem
import json

def index(request):
    try:
        s = Steem(nodes=["https://api.steemit.com"])
        try:
            location = json.loads(s.get_account(request.GET['a'])['json_metadata'])["profile"]["location"]
        except:
            location = 'N/A'
        return HttpResponse(location, content_type='text/plain')
    except:
        return HttpResponse("To use this API call, please supply param a=accountname, substituting accountname with the account to see the account location based on what's typed in the profile.\n\n"
                            'Example: https://api.steem.place/getLocation/?a=moisesmcardona\n\n'
                            'Returns: account location information', content_type='text/plain')