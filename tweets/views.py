from django.http import HttpResponse, Http404, JsonResponse, HttpRequest
from django.shortcuts import render

from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
    # print(args, kwargs)
    return HttpResponse("<h1>Hello world</h1>")

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    # print(args, kwargs)
    """
    REST API ViEW
    Consume by Javascript or Swift or Java or Ios/Android
    retrun json data
    """

    data = {
        "id": tweet_id,
        #"content": obj.content,
        # "image_path": obj.image.url
    }
    status = 200

    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        # raise Http404
        data['massage'] = "Not Found"
        status = 404

    return JsonResponse(data, status = status)

