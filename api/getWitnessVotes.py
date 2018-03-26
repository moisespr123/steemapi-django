from django.http import HttpResponse
from steem import Steem

def index(request):
    try:
        s = Steem(nodes=["https://api.steemit.com"])
        try:
            account = s.get_account(request.GET['a'])
            votes = account["witness_votes"]
            votelist = ""
            for vote in votes:
                votelist += vote + ","
        except:
            votelist = ''
        return HttpResponse(votelist, content_type='text/plain')
    except:
        return HttpResponse("To use this API call, please supply param a=accountname, substituting accountname with the account to see its Witness Votes.\n\n"
            'Example: https://api.steem.place/getWitnessVotes/?a=moisesmcardona\n\n'
            'Returns: Witnesses voted by account, separated by comma (,)', content_type='text/plain')