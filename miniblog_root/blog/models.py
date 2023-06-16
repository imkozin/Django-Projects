from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField('Post\'s title', max_length=100)
    description = models.TextField('Full text')
    author = models.CharField('Author\'s name', max_length=100)
    date = models.DateField('Publication date')
    image = models.ImageField('Image', upload_to='image/%Y')

    def __str__(self):
        return f'{self.author}, {self.title}'

class Comment(models.Model):
    email = models.EmailField()
    name = models.CharField('Username', max_length=50)
    text_comment = models.TextField('Comment\'s text', max_length=2000)
    time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f'{self.name}, {self.post}'

class Like(models.Model):
    ip = models.CharField('IP-Address', max_length=50)
    pos = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')


