from django.http import HttpResponse
from steem import Steem

def index(request):
    if request.method == 'POST':
        try:
            pk = [request.POST['pk']]
            steem = Steem(keys=pk[0], nodes=["https://api.steemit.com"])
            tagsarray = request.POST['tags'].split(',')
            steem.post(request.POST['title'], request.POST['body'], author=request.POST['author'], permlink=request.POST['permlink'], json_metadata={"app": "steemplace/0.1", "tags": tagsarray}, reply_identifier=None, category=None)
            return HttpResponse('ok', content_type='text/plain')
        except:
            return HttpResponse('An error has occurred while posting the reply', content_type='text/plain')
    else:
        return HttpResponse('This is a POST request. To post to the Steem Blockchain, send the following parameters:\n'
                            'pk = private key\n'
                            'title = post title\n'
                            'body = post body\n'
                            'author = post author\n'
                            'permlink = post permlink\n'
                            'tags = tags, comma-separated (tag1,tag2,tag3,tag4,tag5)', content_type='text/plain')