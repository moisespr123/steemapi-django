from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from steem import Steem
from steem.post import Post

@csrf_exempt
def index(request):
    if request.method == 'POST':
        try:
            pk = [request.POST['pk']]
            steem = Steem(keys=pk[0], nodes=["https://api.steemit.com"])
            postToComment = Post(request.POST['i'], steem)
            texto = request.POST['b']
            cuenta = request.POST['a']
            postToComment.reply(body=texto, author=cuenta)
            return HttpResponse('ok', content_type='text/plain')
        except:
            return HttpResponse('An error has occurred while posting the reply', content_type='text/plain')
    else:
        return HttpResponse('This is a POST request. To reply to a post, send the following parameters:\n'
                            'pk = private key\n'
                            'i = post identifier\n'
                            'b = reply body\n'
                            'a = account', content_type='text/plain')