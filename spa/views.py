import operator

from django.shortcuts import render
from api.models import TestRunRequest

def index(request):
    TestRunRequests = TestRunRequest.objects.all().order_by('-created_at')
    contextData = {'TestRunRequests' :  TestRunRequests }
    return render(request, 'spa/index.html', context = contextData)