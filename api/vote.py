from django.http import HttpResponse
from steem import Steem

def index(request):
    if request.method == 'POST':
        try:
            pk = [request.POST['pk']]
            steem = Steem(keys=pk[0], nodes=["https://api.steemit.com"])
            percent = float(request.POST['w'])
            steem.vote(request.POST['i'], percent, account=request.POST['v'])
            return HttpResponse('ok', content_type='text/plain')
        except:
            return HttpResponse('An error has occurred while posting the reply', content_type='text/plain')
    else:
        return HttpResponse('This is a POST request. To vote a post, send the following parameters:\n'
                            'pk = private key\n'
                            'i = post identifier\n'
                            'w = voting weight\n'
                            'v = voter (account to use to vote post)\n', content_type='text/plain')