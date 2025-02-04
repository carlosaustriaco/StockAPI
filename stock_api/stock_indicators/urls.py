from django.urls import path
from .views import IndicatorAPI

urlpatterns = [
    path('api/indicator/', IndicatorAPI.as_view(), name='indicator-api')
]