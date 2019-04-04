import sys
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.contrib.auth.models import User


class Outward(models.Model):
    """ The inward correspondence registry table"""
    date_received = models.DateField(auto_now_add=False)
    date_despatched = models.DateField(auto_now_add=False)
    subject = models.TextField()
    ref_no = models.CharField(max_length=255, blank=True)
    address = models.CharField(
        max_length=255, help_text="Address of the despatched file", blank=True)
    despatch_mode = models.CharField(
        max_length=255, help_text="Mode by which file was despatched", blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)

    def __str__(self):
        return self.subject


class OutwardPic(models.Model):
    name = models.CharField(max_length=255, help_text="Name of image file")
    imagefile = models.ImageField(
        upload_to="Uploads/outward", blank=False, null=False)
    created_on = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)

    def save(self, *args, **kwargs):
        if not self.id:
            self.imagefile = self.compressImage(self.imagefile)
        super(OutwardPic, self).save(*args, **kwargs)

    def compressImage(self, imagefile):
        imagefileTemporal = Image.open(imagefile)
        outpuIoStream = BytesIO()
        imagefileTemporalResized = imagefileTemporal.resize((1020, 573))
        imagefileTemporal.save(outpuIoStream, format='JPEG', quality=60)
        outpuIoStream.seek(0)
        imagefile = InMemoryUploadedFile(outpuIoStream, 'ImageField', "%s.jpg" % imagefile.name.split(
            '.')[0], 'image/jpeg', sys.getsizeof(outpuIoStream), None)
        return imagefile

    def __str__(self):
        return str(self.name)
