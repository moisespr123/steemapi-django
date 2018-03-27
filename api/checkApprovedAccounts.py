from django.http import HttpResponse
from steem import Steem

def index(request):
    try:
        s = Steem(nodes=["https://api.steemit.com"])
        posting = s.get_account(request.GET['user'])
        gotAccount = False
        for account in posting['posting']['account_auths']:
            if account[0] == request.GET['account']:
                gotAccount = True
                return HttpResponse(True, content_type='text/plain')
        if not gotAccount:
            return HttpResponse(False, content_type='text/plain')
    except:
        return HttpResponse('To use this API call, please supply param user=account username and account=account to check if authorized.\n\n'
                            'Example: http://api.steem.place/checkApprovedAccounts/?user=moisesmcardona&account=steem.place\n\n'
                            'Returns: True if user @moisesmcardona has authorized @steem.place', content_type='text/plain')