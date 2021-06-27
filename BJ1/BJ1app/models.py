from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255, default='Robert')
    last_name = models.CharField(max_length=255, default='Johnson')
    email_address = models.EmailField(default='robert@gmail.com')
    age = models.IntegerField(default=25)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"