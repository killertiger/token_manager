from django.db import models

# Create your models here.


class CodeGenerated(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    used_at = models.DateTimeField(null=True)
    code = models.CharField(max_length=10)
    metadata = models.TextField(max_length=1000)

    def __str__(self):
        return self.code
