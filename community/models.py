from django.db import models
from accounts.models import MyUser
from django.utils.timezone import datetime

class Post(models.Model):
    title = models.CharField(max_length=50)
    community_type = models.CharField(max_length=50, choices=(('Open Community','Open Community'),
                                                            ('Quarantine Community','Quarantine Community'),
                                                            ('Lockdown Stuck Community','Lockdown Stuck Community')
                                                            ),default='Open Community')
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    content = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/',blank=True)
    time = models.DateTimeField(default=datetime.now)
    likes_count = models.IntegerField(default=0)
    dislikes_count = models.IntegerField(default=0)
    comment_count = models.IntegerField(default=0)
    tags = models.CharField(max_length=250, null=True)
    def __str__(self):
        return self.title
    

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    writter = models.CharField(max_length=50)
    text = models.CharField(max_length=250)
    posting_time = models.DateTimeField(default=datetime.now)
