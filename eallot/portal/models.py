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
