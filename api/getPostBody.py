from django.http import HttpResponse
from steem import Steem

def index(request):
    try:
        s = Steem(nodes=["https://api.steemit.com"])
        author, permlink = request.GET['p'].split("/")
        post = s.get_content(author, permlink)
        return HttpResponse(post["body"], content_type='text/plain')
    except:
        return HttpResponse("To use this API call, please supply param p=account/post, substituting account/post with the account and permlink of the post.\n\n"
                            'Example: https://api.steem.place/getPostBody/?p=moisesmcardona/preparing-dinner-2-chicken-thights\n\n'
                            'Returns: Post Body', content_type='text/plain')