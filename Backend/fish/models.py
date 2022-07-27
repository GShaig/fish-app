from django.db import models
from django.core.validators import FileExtensionValidator

def upload_to(instance, filename):
    return 'files/{filename}'.format(filename=filename)

class Data(models.Model):
    upload = models.FileField(validators=[FileExtensionValidator(allowed_extensions=['csv'])], upload_to=upload_to, null=True, blank=True)
