from django.db import models
from django.utils.text import slugify
from embed_video.fields import EmbedVideoField
# Create your models here.



class Project(models.Model):
  title =  models.CharField(max_length=200, unique=True)
  client_name =  models.CharField(max_length=200, unique=True)
  description = models.TextField(max_length=500)
  role = models.TextField(max_length=200)
  slug =   models.SlugField(max_length=200, unique=True)
  status = models.TextField(max_length=200)
  created_on = models.DateTimeField(auto_now_add=True)
  updated_on = models.DateTimeField(auto_now=True)
  video = EmbedVideoField()  # same like models.URLField()
  video_1 = EmbedVideoField()
  video_2 = EmbedVideoField()

  def save(self, *args, **kwargs):
        if not self.slug and self.title :
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)

  class Meta:
        verbose_name = 'project'


  def __str__(self):
        return self.title
