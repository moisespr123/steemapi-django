from django.http import HttpResponse
from steem import Steem
import json

def index(request):
    try:
        s = Steem(nodes=["https://api.steemit.com"])
        author, permlink = request.GET['p'].split("/")
        post = s.get_content(author, permlink)
        postdata = post["active_votes"]
        counter = len(postdata)
        return HttpResponse(counter, content_type='text/plain')
    except:
        return HttpResponse("To use this API call, please supply param p=account/post, substituting account/post with the account and permlink of the post.\n\n"
            'Example: https://api.steem.place/getPostVotesCount/?p=moisesmcardona/preparing-dinner-2-chicken-thights\n\n'
            'Returns: Total number of votes in the post', content_type='text/plain')