from django.db import models

class ManualType(models.TextChoices):
    Installation = 'Installation', 'Installation'
    Recycle = 'Recycle', 'Recycle'
    Disassembly = 'Disassembly', 'Disassembly'
    Safety = 'Safety', 'Safety'
    Other = 'Other', 'Other'
    Use = 'Use', 'Use'

class Source(models.TextChoices):
    Biological = 'Biological', 'Biological'
    Other = 'Other', 'Other'
    Mined = 'Mined', 'Mined'
    Plant = 'Plant', 'Plant'
    Animal = 'Animal', 'Animal'
    Synthetic = 'Synthetic', 'Synthetic'
    Recycled = 'Recycled', 'Recycled'

class Carrier(models.TextChoices):
    NFC = 'NFC', 'NFC'
    QRCode = 'QRCode', 'QRCode'
    Barcode = 'Barcode', 'Barcode'

class MaterialUse(models.Model):
    quantity = models.IntegerField()
    unit = models.IntegerField()
    is_direct = models.BooleanField()
    reparation = models.ForeignKey('Reparation', on_delete=models.SET_NULL, blank=True, null=True)
    stage = models.ForeignKey('LifecycleStage', on_delete=models.PROTECT)
    material = models.ForeignKey('Material', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)

class Company(models.Model):
    postal_code = models.IntegerField()
    GLN = models.IntegerField()
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    stage = models.ManyToManyField('LifecycleStage', blank=True, null=True)

    def __str__(self):
        return str(self.id)

class Material(models.Model):
    toxic = models.CharField(max_length=255)
    source = models.CharField(max_length=255, choices=Source.choices)
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)

class DataCarrier(models.Model):
    code = models.CharField(max_length=255)
    technology = models.CharField(max_length=255, choices=Carrier.choices)
    product = models.ForeignKey('ProductPassport', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)

class Parameter(models.Model):
    value = models.IntegerField()
    metric = models.ForeignKey('Metric', on_delete=models.PROTECT)
    stage = models.ForeignKey('LifecycleStage', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Metric(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)

class LifecycleStage(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    issuer = models.ForeignKey('Person', on_delete=models.PROTECT)
    product = models.ForeignKey('ProductPassport', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Person(models.Model):
    function = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    telephone = models.IntegerField()
    company = models.ForeignKey('Company', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)

class Design(LifecycleStage):

    def __str__(self):
        return str(self.id)

class ProductPassport(models.Model):
    product_code = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    GTIN = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    hazard = models.ForeignKey('Hazard', on_delete=models.PROTECT)
    recycled_material = models.ForeignKey('RecycledMaterial', on_delete=models.PROTECT)
    chemical = models.ForeignKey('Chemical', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)

class Chemical(models.Model):
    disclosure = models.CharField(max_length=255)
    threshold = models.CharField(max_length=255)
    composition = models.BooleanField()

    def __str__(self):
        return str(self.id)

class Manufacture(LifecycleStage):
    production_site = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)

class Hazard(models.Model):
    exeed_limit = models.BooleanField()
    very_high = models.BooleanField()
    crm = models.BooleanField()

    def __str__(self):
        return str(self.id)

class Distribution(LifecycleStage):
    source = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)

class Use(LifecycleStage):

    def __str__(self):
        return str(self.id)

class Collect(LifecycleStage):

    def __str__(self):
        return str(self.id)

class RecycledMaterial(models.Model):
    posconsumer = models.CharField(max_length=255)
    renewable = models.CharField(max_length=255)
    preconsumer = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)

class Recycle(LifecycleStage):

    def __str__(self):
        return str(self.id)

class Reparation(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    use_stage = models.ForeignKey('Use', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)

class Guideline(models.Model):
    type = models.CharField(max_length=255, choices=ManualType.choices)
    name = models.CharField(max_length=255)
    doc = models.CharField(max_length=255)
    description = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)
















