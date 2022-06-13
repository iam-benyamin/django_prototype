from django.db import models

class Partner(models.Model):
    name = models.CharField(max_length=100,unique=True)
    origin = models.CharField(max_length=100) # partner domain to login company

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    web_content_size = models.IntegerField(blank=True, null=True)
    last_processed_date = models.DateTimeField(blank=True, null=True)

    partner = models.ForeignKey(Partner, on_delete=models.CASCADE)
    partner_company_id = models.CharField(max_length=255)
    def __str__(self):
        return self.name