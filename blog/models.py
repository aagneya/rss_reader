from django.db import models

# Create your models here.
class rssreader(models.Model):

      url_input = models.CharField(max_length=100,blank=True, null=True)
      
      def __str__(self):
		return self.url_input
