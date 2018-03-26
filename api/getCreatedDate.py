from django.http import HttpResponse
from steem import Steem

def index(request):
    try:
        s = Steem(nodes=["https://api.steemit.com"])
        try:
            created = s.get_account(request.GET['a'])['created']
        except:
            created = None
        return HttpResponse(created, content_type='text/plain')
    except:
        return HttpResponse('To use this API call, please supply param a=accountname, substituting accountname with the account to see its creation date.\n\n'
                            'Example: https://api.steem.place/getCreatedDate/?a=moisesmcardona\n\n'
                            'Returns: Created date', content_type='text/plain')