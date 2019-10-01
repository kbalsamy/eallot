from django.db import models

# database model for service_grouping table


class Service(models.Model):

    name = models.CharField(max_length=20, unique=True)
    remarks = models.CharField(max_length=30, blank=True)

    def __str__(self):

        return self.name


class EDC(models.Model):

    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=20)

    def __str__(self):

        return self.name


# db model for mapping service into service group

class Service_Grouping(models.Model):

    serviceNumber = models.CharField(max_length=12, unique=True)
    servicePassword = models.CharField(max_length=20)
    serviceZone = models.ForeignKey(EDC, on_delete=models.CASCADE)
    serviceGroup = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):

        return self.serviceNumber

# db for generator monthly generator readings


class GeneratorReadings(models.Model):

    genstatementID = models.CharField(max_length=10, unique=True)
    consumerID = models.CharField(max_length=12, blank=True)
    statementMonth = models.CharField(max_length=2, blank=True)
    statementYear = models.CharField(max_length=4, blank=True)
    companyName = models.CharField(max_length=150, blank=True)
    impUnitsC1 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    impUnitsC2 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    impUnitsC3 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    impUnitsC4 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    impUnitsC5 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    expUnitsC1 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    expUnitsC2 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    expUnitsC3 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    expUnitsC4 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    expUnitsC5 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    netUnitsC1 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    netUnitsC2 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    netUnitsC3 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    netUnitsC4 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    netUnitsC5 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    bankingC1 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    bankingC2 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    bankingC3 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    bankingC4 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    bankingC5 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    chargesC002 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    chargesC003 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    chargesC004 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    chargesC005 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    chargesC006 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    chargesC007 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    chargesC008 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    chargesC001 = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)

    def __str__(self):

        return self.consumerID + '_' + self.statementMonth + self.statementYear


class meterReadings(models.Model):

    readingID = models.CharField(max_length=10, unique=True)
    serviceNumber = models.CharField(max_length=12, blank=True)
    month = models.CharField(max_length=2, blank=True)
    year = models.CharField(max_length=150, blank=True)
    netUnitsC1 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    netUnitsC2 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    netUnitsC3 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    netUnitsC4 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)
    netUnitsC5 = models.DecimalField(max_digits=12, decimal_places=2, blank=True)

    def __str__(self):

        return self.serviceNumber + '_' + self.month + self.year
