from django.db   import  models

# department models
class Department(models.Model):
    name=models.CharField(max_length=50)
    code=models.CharField(max_length=3)
    head=models.CharField(max_length=40)
    block=models.CharField(max_length=40)
    

    def __str__(self):
        return self.name


