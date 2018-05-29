from django.db import models

def upload(instance, filename):
    instance.upload_path = 'images/'+str(instance.memberType)+'/'+str(instance.member)+'/'+filename
    return instance.upload_path


class ImageUploads(models.Model):
    member = models.CharField(max_length=255, blank=True)
    memberType = models.CharField(max_length=1, blank=True)
    # upload_path=''
    document = models.ImageField(upload_to=upload)
    uploaded_at = models.DateTimeField(auto_now_add=True)
