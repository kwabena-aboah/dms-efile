import sys
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.contrib.auth.models import User


class Inward(models.Model):
    """ The inward correspondence registry table"""
    date_of_letter = models.DateField(auto_now_add=False)
    date_received = models.DateField(auto_now_add=False)
    received_from = models.CharField(max_length=200)
    ref_no = models.CharField(max_length=255, blank=True)
    subject = models.TextField()
    officer_to = models.CharField(
        max_length=255, help_text="Officer to whom file is passed")
    date_filed = models.DateField(auto_now_add=False, help_text="Date added")
    file_number = models.CharField(
        max_length=255, help_text="Complaint, purpose or issue")
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)

    def __str__(self):
        return self.received_from


class InwardPic(models.Model):
    name = models.CharField(max_length=255, help_text="Name of image file")
    imagefile = models.ImageField(
        upload_to="Uploads/inward", blank=False, null=False)
    created_on = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,)

    def save(self, *args, **kwargs):
        if not self.id:
            self.imagefile = self.compressImage(self.imagefile)
        super(InwardPic, self).save(*args, **kwargs)

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


class DocumentUpload(models.Model):
    name = models.FileField(upload_to="Uploads/documents")
    uploaded_on = models.DateField(auto_now_add=True)
