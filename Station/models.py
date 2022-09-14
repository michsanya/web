from django.db import models


class Ganre(models.Model):
    ganre = models.CharField(max_length=50)

    def __str__(self):
        return self.ganre


class Station(models.Model):
    name = models.CharField(max_length=50)
    freq = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=87)
    location = models.CharField(max_length=50)
    ganre = models.ForeignKey(Ganre, on_delete=models.SET_NULL, null=True)
    icon = models.ImageField(upload_to='icons', default='none')
    url_address = models.URLField(default='none')

    def __str__(self):
        return self.name + ' - ' + str(self.freq) + ' MHz'
