from django.db import models

class LifecycleStage(models.Model):
    start = models.DateField()
    end = models.DateField()
    rawmaterial = models.ManyToManyField('RawMaterial')
    productpassport = models.ManyToManyField('ProductPassport')

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

class RawMaterial(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)

class ProductPassport(models.Model):
    code = models.CharField(max_length=255)
    product_name = models.IntegerField()
    brand = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)

class Reparation(models.Model):
    date_set = models.DateField()
    description = models.CharField(max_length=255)
    use = models.ForeignKey('Use', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)





