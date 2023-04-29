from django.db import models

class Profile(models.Model):
  name = models.CharField(max_length=255)
  pfp = models.ImageField(null=True, blank=True, upload_to='profile/')
  
  @property
  def pfpURL(self):
    try:
      return self.pfp.url
    except:
      return ''
      