from django.http import HttpResponse
from steem import Steem

def index(request):
    try:
        s = Steem(nodes=["https://api.steemit.com"])
        try:
            follow_count = s.get_follow_count(request.GET['a'])['follower_count']
        except:
            follow_count = 0
        return HttpResponse(follow_count, content_type='text/plain')
    except:
        return HttpResponse("To use this API call, please supply param a=accountname, substituting accountname with the account to see the account's follower number.\n\n"
                            'Example: https://api.steem.place/getFollowersCount/?a=moisesmcardona\n\n'
                            'Returns: Total followers number', content_type='text/plain')