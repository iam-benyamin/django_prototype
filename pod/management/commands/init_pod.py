from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from pod.models import *

class Command(BaseCommand):
    def handle(self, *args, **options):
        username = 'admin'
        password = 'admin'
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username=username, password=password)

        # Create Partner
        partner,_ = Partner.objects.update_or_create(
            name='ebay', defaults={'name': 'ebay', 'origin':'127.0.0.1:3000'})

        # Create Company
        Company.objects.update_or_create(name='dell', description='best computer store. last sales $152.23.', partner=partner,partner_company_id=1)
        Company.objects.update_or_create(
            name='dyson', description='great vaccum. last sales $988.77.', partner=partner, partner_company_id=2)
