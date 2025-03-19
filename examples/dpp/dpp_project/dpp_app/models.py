from django.db import models

class Reparation(models.Model):
    description = models.CharField(max_length=255)
    date_set = models.DateField()
    Use = models.ForeignKey('Use', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)

class RawMaterial(models.Model):
    name = models.CharField(max_length=255)
    LifecycleStage = models.ManyToManyField('LifecycleStage', blank=True)

    def __str__(self):
        return str(self.id)

class LifecycleStage(models.Model):
    start = models.DateField()
    end = models.DateField()
    ProductPassport = models.ManyToManyField('ProductPassport', blank=True)

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

class ProductPassport(models.Model):
    code = models.CharField(max_length=255)
    product_name = models.IntegerField()
    brand = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)





