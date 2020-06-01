import random
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Tweet
from .forms import TweetForm

def tweetCreateView(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    print('post data is: ', request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        # do other form related logic
        obj.save()
        form = TweetForm()
    return render(request, 'components/form.html', context={"form": form})

def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW 
    Consume by javascript, or Swift/Java/iOS/Android
    return json.data
    """
    qs = Tweet.objects.all()
    tweet_list = [{"id": x.id, "content": x.content, "likes": random.randint(0,100)} for x in qs]
    data = {
    "isUser": False, 
        "response": tweet_list,
 
    }
    return JsonResponse(data)


def home_view(request, *args, **kwargs):
    print(args, kwargs)
    #return HttpResponse("<h1>Hello World</h1>") 
    return render(request, "pages/home.html", context={}, status=200)  

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