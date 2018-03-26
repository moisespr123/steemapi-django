from django.http import HttpResponse
from steem import Steem

def index(request):
    if request.method == 'POST':
        try:
            pk = [request.POST['pk']]
            steem = Steem(keys=pk[0], nodes=["https://api.steemit.com"])
            steem.resteem(request.POST['i'], account=request.POST['a'])
            return HttpResponse('ok', content_type='text/plain')
        except:
            return HttpResponse('An error has occurred while resteeming the post', content_type='text/plain')
    else:
        return HttpResponse('This is a POST request. To resteem a post, send the following parameters:\n'
                                'pk = private key\n'
                                'i = post identifier\n'
                                'a = account', content_type='text/plain')