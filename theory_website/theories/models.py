from django.db import models

class Theory(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='theories_images/')

    def __str__(self):
        return self.name



# class TheoryImage(models.Model):
#     theory = models.ForeignKey(Theory, related_name='theories_images', on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='C:\Users\Owner\Desktop\Theories\theory_websitemedia')
