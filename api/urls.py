from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from .views import TestRunRequestAPIView, TestRunRequestItemAPIView, AssetsAPIView

urlpatterns = [
    path('assets', AssetsAPIView.as_view(), name='assets'),
    path('test-run', TestRunRequestAPIView.as_view(), name='test_run_req'),
    path('test-run/<pk>', TestRunRequestItemAPIView.as_view(), name='test_run_req_item'),
    #API Documentation
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
