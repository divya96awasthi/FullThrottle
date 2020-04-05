# from django.core import serializers
from .Serializers import UserSerializer
from .models import User, ActivityPeriods
from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
import json


# Create your views here.


def home(request):
    # this function is for rendering home page
    return render(request, "home.html")


def json_generator(request):
    # this function will generate json format of the data
    user = User.objects.all()
    if user:
        temp_user = UserSerializer(user, many=True)
        for users in temp_user.data:
            activity_period = ActivityPeriods.objects.filter(user_id_id=users['id']).values('start_time', 'end_time')
            query_set = json.dumps(list(activity_period), cls=DjangoJSONEncoder)
            users['activity_periods'] = query_set

            response_dict = {"ok": True,
                             "members": temp_user.data,
                             }
        json_data = json.dumps(response_dict)
        #json_data1 = json_data.replace("\\", '')
        response = HttpResponse(json_data, content_type='application/json')
        response['Content-Disposition'] = 'attachment; {}' % response  # this syntax is to download the json file if
        # data is available.
        return response

    else:
        return render(request, "base.html")
