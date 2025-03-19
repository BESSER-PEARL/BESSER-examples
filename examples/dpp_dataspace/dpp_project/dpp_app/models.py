from django.db import models

class Carrier(models.TextChoices):
    BARCODE = 'Barcode', 'Barcode'
    QRCODE = 'QRCode', 'QRCode'
    NFC = 'NFC', 'NFC'

class Source(models.TextChoices):
    BIOLOGICAL = 'Biological', 'Biological'
    SYNTHETIC = 'Synthetic', 'Synthetic'
    MINED = 'Mined', 'Mined'
    OTHER = 'Other', 'Other'
    PLANT = 'Plant', 'Plant'
    RECYCLED = 'Recycled', 'Recycled'
    ANIMAL = 'Animal', 'Animal'

class ManualType(models.TextChoices):
    SAFETY = 'Safety', 'Safety'
    INSTALLATION = 'Installation', 'Installation'
    DISASSEMBLY = 'Disassembly', 'Disassembly'
    RECYCLE = 'Recycle', 'Recycle'
    OTHER = 'Other', 'Other'
    USE = 'Use', 'Use'

class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.IntegerField()
    GLN = models.IntegerField()
    stage = models.ManyToManyField('LifecycleStage', blank=True)

    def __str__(self):
        return str(self.id)

class Reparation(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date = models.DateTimeField()
    use_stage = models.ForeignKey('Use', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)

class Person(models.Model):
    name = models.CharField(max_length=255)
    function = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    telephone = models.IntegerField()
    company = models.ForeignKey('Company', on_delete=models.PROTECT)

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

class Manufacture(LifecycleStage):
    production_site = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)

class Collect(LifecycleStage):

    def __str__(self):
        return str(self.id)

class Use(LifecycleStage):

    def __str__(self):
        return str(self.id)

class Design(LifecycleStage):

    def __str__(self):
        return str(self.id)

class DiStringTypeibution(LifecycleStage):
    source = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)

class Recycle(LifecycleStage):

    def __str__(self):
        return str(self.id)

class Metric(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)

class Parameter(models.Model):
    value = models.IntegerField()
    stage = models.ForeignKey('LifecycleStage', on_delete=models.CASCADE)
    metric = models.ForeignKey('Metric', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)

class DataCarrier(models.Model):
    code = models.CharField(max_length=255)
    technology = models.CharField(max_length=255, choices=Carrier.choices)
    product = models.ForeignKey('ProductPassport', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)

class Material(models.Model):
    name = models.CharField(max_length=255)
    toxic = models.CharField(max_length=255)
    source = models.CharField(max_length=255, choices=Source.choices)

    def __str__(self):
        return str(self.id)

class MaterialUse(models.Model):
    quantity = models.IntegerField()
    unit = models.IntegerField()
    is_direct = models.BooleanField()
    material = models.ForeignKey('Material', on_delete=models.PROTECT)
    stage = models.ForeignKey('LifecycleStage', on_delete=models.PROTECT)
    reparation = models.ForeignKey('Reparation', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return str(self.id)

class Guideline(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    type = models.CharField(max_length=255, choices=ManualType.choices)
    doc = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)

class RecycledMaterial(models.Model):
    preconsumer = models.CharField(max_length=255)
    posconsumer = models.CharField(max_length=255)
    renewable = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)

class Hazard(models.Model):
    very_high = models.BooleanField()
    crm = models.BooleanField()
    exeed_limit = models.BooleanField()

    def __str__(self):
        return str(self.id)

class Chemical(models.Model):
    threshold = models.CharField(max_length=255)
    disclosure = models.CharField(max_length=255)
    composition = models.BooleanField()

    def __str__(self):
        return str(self.id)

class ProductPassport(models.Model):
    code = models.CharField(max_length=255)
    GTIN = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_code = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    chemical = models.ForeignKey('Chemical', on_delete=models.PROTECT)
    recycled_material = models.ForeignKey('RecycledMaterial', on_delete=models.PROTECT)
    hazard = models.ForeignKey('Hazard', on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)
















