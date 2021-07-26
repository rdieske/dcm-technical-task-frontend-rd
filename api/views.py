from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiResponse
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import TestRunRequest
from api.serializers import TestRunRequestSerializer, TestRunRequestItemSerializer
from api.tasks import execute_test_run_request
from api.usecases import get_assets


@extend_schema(description='Create a test run job to queue for Celery', methods=["POST"])
class TestRunRequestAPIView(ListCreateAPIView):
    """
        Returns a list of all test runs and their corresponding status information
    """
    serializer_class = TestRunRequestSerializer
    queryset = TestRunRequest.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        instance = serializer.save()
        execute_test_run_request.delay(instance.id)


class TestRunRequestItemAPIView(RetrieveAPIView):
    """
        Returns a test run object including all logs for the run
    """
    serializer_class = TestRunRequestItemSerializer
    queryset = TestRunRequest.objects.all()
    lookup_field = 'pk'


class AssetsAPIView(APIView):
    """
    Returns an object with 2 lists, one for all the available test paths and one for all the available environments
    """
    example = {
        "available_paths": [
            {
                "id": 5,
                "path": "api/tests/test_models.py"
            },
            {
                "id": 6,
                "path": "api/tests/test_tasks.py"
            },
        ],
        "test_envs": [
            {
                "id": 1,
                "name": "env1"
            },
            {
                "id": 10,
                "name": "env10"
            },
            {
                "id": 100,
                "name": "env100"
            },
        ]
    }

    @extend_schema(
        responses={200: OpenApiResponse(
            response=200,
            examples=[OpenApiExample(
                name='Simple Example',
                value=example
            )]
        )}
    )
    def get(self, request):
        return Response(status=status.HTTP_200_OK, data=get_assets())
