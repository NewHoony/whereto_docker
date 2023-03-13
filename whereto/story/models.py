from django.db import models

class Book(models.Model):
    site_name = models.CharField(max_length=100, null=True, blank=True)
    site_url = models.TextField()
    site_con = models.TextField(max_length=200)
    site_cover = models.ImageField(upload_to='story/bookcovers/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.site_name