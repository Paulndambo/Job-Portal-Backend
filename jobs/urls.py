from django.urls import path
from .views import JobListCreateAPIView, JobDetailAPIView, JobsWriterAPIView

urlpatterns = [
    path('search/', JobListCreateAPIView.as_view(), name='search'),
    path('job-details/<int:pk>/', JobDetailAPIView.as_view(), name='job-details'),
    path('upload-data/', JobsWriterAPIView.as_view(), name='upload-data')
]