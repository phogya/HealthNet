from django.db import models
from django.forms import ModelForm, Textarea, Select

# Create your models here.


class Message(models.Model):
    sender = models.CharField(max_length=30)
    receiver = models.CharField(max_length=30)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=2000)
    time = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=0)

class MessageForm(ModelForm):

    class Meta:
        model = Message
        widgets = {
            'message': Textarea(attrs={'cols': 30, 'rows': 10}),
            }
        fields = ['subject','message']