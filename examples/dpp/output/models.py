from django.db import models

class RawMaterial(models.Model):
    name = models.CharField(max_length=255)
    composition = models.ManyToManyField('LifecycleStage', blank=True, null=True)

    def __str__(self):
        return str(self.id)

class ProductPassport(models.Model):
    code = models.CharField(max_length=255)
    product_name = models.IntegerField()
    brand = models.CharField(max_length=255)
    stage = models.ManyToManyField('LifecycleStage')

    def __str__(self):
        return str(self.id)

class Reparation(models.Model):
    description = models.CharField(max_length=255)
    date_set = models.DateField()
    reparations = models.ForeignKey('Use', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class LifecycleStage(models.Model):
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return str(self.id)

class Design(LifecycleStage):

    def __str__(self):
        return str(self.id)

class Use(LifecycleStage):

    def __str__(self):
        return str(self.id)

class Manufacture(LifecycleStage):

    def __str__(self):
        return str(self.id)

class Distribution(LifecycleStage):

    def __str__(self):
        return str(self.id)





