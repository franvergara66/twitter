from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render
from .models import Tweet

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h1>Hello World</h1>")   

def tweet_detail_view(request, tweed_id, *args, **kwargs):
    """
    REST API VIEW 
        Consume by javascript, or Swift/Java/iOS/Android
        return json.data
    """
    data = {
        "id": tweed_id,
        #"image_path": obj.img.url
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweed_id)
        data['content'] = obj.content,
    except:
         data['message'] = 'Not Found',
         status = 404
        

    return JsonResponse(data, status=status)  #json.dumps content_type='application/json'