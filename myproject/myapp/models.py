from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class News(models.Model):
    tittle = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    content = RichTextUploadingField(blank=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.tittle

