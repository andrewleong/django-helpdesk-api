from django.db import models
import uuid
from django.contrib.auth.models import User

def create_ticket_id():
    return str(uuid.uuid4()).split("-")[-1]

class Ticket(models.Model):
    ticket_id = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)

    # Magic method to return format
    def __str__(self):
        return "{} = {}".format(self.title, self.ticket_id)

    def save(self, *args, **kwargs):
        if len(self.ticket_id.strip(" "))==0:
            self.ticket_id = create_ticket_id()

        super(Ticket, self).save(*args, **kwargs)

    class Meta:
        ordering = ["-created_date"]

class Category(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
