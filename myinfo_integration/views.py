from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from myinfo_integration.myinfo.client import MyInfoClient
from myinfo_integration.myinfo.security import get_decoded_access_token, get_decrypted_person_data

client = MyInfoClient()


def homepage_view(request):
    return render(request, 'homepage.html')


def myinfo_auth_view(request):
    authorise_url = client.get_authorise_url(state="testing")
    if not authorise_url:
        raise ValueError("authorise url is not available.")
    return HttpResponseRedirect(authorise_url)


def myinfo_callback(request):
    # Getting access token with code
    code = request.GET.get('code')
    if not code:
        raise ValueError("code is not available.")
    resp = client.get_access_token(code)
    access_token = resp.get("access_token")
    if not access_token:
        raise ValueError("access token is not available.")
    # Decoding access token
    decoded_access_token = get_decoded_access_token(access_token)
    uinfin = decoded_access_token["sub"]

    # Getting person data
    resp = client.get_person(uinfin=uinfin, access_token=access_token)
    decrypted = get_decrypted_person_data(resp)

    return render(request, 'homepage.html', context={'retrieved_info': decrypted})
