from django.http import HttpResponse
from steem import Steem
import json

def index(request):
    try:
        s = Steem(nodes=["https://api.steemit.com"])
        author, permlink = request.GET['p'].split("/")
        post = s.get_content(author, permlink)
        postdata = post["active_votes"]
        users = ""
        for voters in postdata:
            users += voters["voter"] + ","
        return HttpResponse(users, content_type='text/plain')
    except:
        return HttpResponse("To use this API call, please supply param p=account/post, substituting account/post with the account and permlink of the post.\n\n"
            'Example: https://api.steem.place/getPostVotes/?p=moisesmcardona/preparing-dinner-2-chicken-thights\n\n'
            'Returns: Users who voted the post, separated by comma (,)', content_type='text/plain')