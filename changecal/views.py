# Create your views here.

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from changecal.serializers import ChangeRequestSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from changecal.models import ChangeRequest



class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its contents into JSOn/
    """

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def change_list(request):
    """
    List all change requests, or create a new request.
    """

    if request.method == 'GET':
        changerequests = ChangeRequest.objects.all()
        serializer = ChangeRequestSerializer(changerequests, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ChangeRequestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)


@csrf_exempt
def change_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        changerequest = ChangeRequest.objects.get(pk=pk)
    except ChangeRequest.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ChangeRequestSerializer(changerequest)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ChangeRequestSerializer(changerequest, data=data)

        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        changerequest.delete()
        return HttpResponse(status=204)
