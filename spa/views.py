import operator

from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import JsonResponse

from api.models import TestRunRequest

def index(request):
    TestRunRequests = TestRunRequest.objects.all().order_by('-created_at')
    contextData = {'TestRunRequests' :  TestRunRequests }

    if request.is_ajax():
        data = dict()
        data['html_table'] = render_to_string('spa/runRequestsTable.html',
            contextData,
            request = request)
        return JsonResponse(data)

    return render(request, 'spa/index.html', context = contextData)