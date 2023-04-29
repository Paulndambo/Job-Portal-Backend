from django.shortcuts import render
from .serializers import JobSerializer, JobWriterSerializer
from .models import Job
from rest_framework import status, generics
from rest_framework.response import Response
from .rapidapi import data_dismantler
import requests
# Create your views here.
class JobListCreateAPIView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    lookup6_field = "pk"


class JobsWriterAPIView(generics.GenericAPIView):
    serializer_class = JobWriterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            url = "https://jsearch.p.rapidapi.com/search"

            querystring = {"query": f"{request.data['upload']}","page":"5","num_pages":"3"}

            headers = {
                "content-type": "application/octet-stream",
                "X-RapidAPI-Key": "3eb9cc95b8msh9605b615e7f39c8p12bd91jsn4f29554abd4d",
                "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers, params=querystring)
            y = response.json()['data']
            for x in y:
                z = data_dismantler(x)
                try:
                    Job.objects.create(**z)
                except Exception as e:
                    raise e
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)