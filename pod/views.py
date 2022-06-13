from rest_framework.decorators import api_view
from .models import *
from django.core import serializers
from rest_framework.response import Response
import datetime
import requests

@api_view(['GET', ])
def description(request):
    # TODO: 
    # Add authentication, so that only authenticated user can view their own company description
    # Authentication should be tied to Company model
    company = serializers.serialize("json", Company.objects.all())
    return Response(company)


@api_view(['GET', ])
def update(request):
    # TODO:
    # Below is an example of a background task that involves both getting information from database, and updating database. The task usually takes long processing time.
    # The goal is to run such task in a celery worker which is deployed in digitial ocean.
    company = Company.objects.first()
    company_name = company.name
    company.web_content_size = len(requests.get(
        'http://www.{company}.com'.format(company=company_name)).text)
    company.last_processed_date = datetime.datetime.now()
    company.save()
    return Response(200)
