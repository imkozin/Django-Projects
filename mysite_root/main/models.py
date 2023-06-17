from django.db import models

# Create your models here.

class TodoList(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Item(models.Model):
    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE, related_name='items')
    text = models.TextField()
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.text