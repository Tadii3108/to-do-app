from django.db import models

# creates a special type of class called todoitem which represent each todo item in our database.
# able to interact with the data in the db using this class
# content is an attribute, which represents content of each item which is text; (textfield)
class TodoItem(models.Model):
    content = models.TextField()