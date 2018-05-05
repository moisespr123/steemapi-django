"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import index
from . import checkApprovedAccounts
from . import getCreatedDate
from . import getFollowersCount
from . import getFollowingCount
from . import getLocation
from . import getPostBody
from . import getPostCount
from . import getPostDate
from . import getPostTags
from . import getPostTitle
from . import getPostVotes
from . import getPostVotesJSON
from . import getPostVotesCount
from . import getSBDBalance
from . import getSTEEMBalance
from . import getVP
from . import getWitnessVotes
from . import postReply
from . import postResteem
from . import postToSteem
from . import vote

urlpatterns = [
    path('', index.index, name='index'),
    path('checkApprovedAccounts/', checkApprovedAccounts.index, name='index'),
    path('getCreatedDate/', getCreatedDate.index, name='index'),
    path('getFollowersCount/', getFollowersCount.index, name='index'),
    path('getFollowingCount/', getFollowingCount.index, name='index'),
    path('getLocation/', getLocation.index, name='index'),
    path('getPostBody/', getPostBody.index, name='index'),
    path('getPostCount/', getPostCount.index, name='index'),
    path('getPostDate/', getPostDate.index, name='index'),
    path('getPostTags/', getPostTags.index, name='index'),
    path('getPostTitle/', getPostTitle.index, name='index'),
    path('getPostVotes/', getPostVotes.index, name='index'),
    path('getPostVotesJSON/', getPostVotesJSON.index, name='index'),
    path('getPostVotesCount/', getPostVotesCount.index, name='index'),
    path('getSBDBalance/', getSBDBalance.index, name='index'),
    path('getSTEEMBalance/', getSTEEMBalance.index, name='index'),
    path('getVP/', getVP.index, name='index'),
    path('getWitnessVotes/', getWitnessVotes.index, name='index'),
    path('postReply/', postReply.index, name='index'),
    path('postResteem/', postResteem.index, name='index'),
    path('postToSteem/', postToSteem.index, name='index'),
    path('vote/', vote.index, name='index'),
]
