import json
from datetime import datetime
from django.shortcuts import render
from portal.forms import SGForm, AddServicesForm, EDC
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from portal.models import Service, Service_Grouping, GeneratorReadings, meterReadings
from django.shortcuts import get_object_or_404
from django.core import serializers
from portal import api
from django.db import IntegrityError
from django.db.models import Sum
from django.core.serializers import serialize

# Create your views here.

currentMonth = "0" + str(datetime.now().month - 1)
currentYear = str(datetime.now().year)


def homeView(request):

    C1 = GeneratorReadings.objects.filter(statementMonth=currentMonth, statementYear=currentYear).aggregate(Sum('netUnitsC1'))["netUnitsC1__sum"]
    C2 = GeneratorReadings.objects.filter(statementMonth=currentMonth, statementYear=currentYear).aggregate(Sum('netUnitsC2'))["netUnitsC2__sum"]
    C3 = GeneratorReadings.objects.filter(statementMonth=currentMonth, statementYear=currentYear).aggregate(Sum('netUnitsC3'))["netUnitsC3__sum"]
    C4 = GeneratorReadings.objects.filter(statementMonth=currentMonth, statementYear=currentYear).aggregate(Sum('netUnitsC4'))["netUnitsC4__sum"]
    C5 = GeneratorReadings.objects.filter(statementMonth=currentMonth, statementYear=currentYear).aggregate(Sum('netUnitsC5'))["netUnitsC5__sum"]

    return render(request, 'portal/index.html', {'c1': C1, 'c2': C2, 'c3': C3, 'c4': C4, 'c5': C5})


def router(request):

    sg_form = SGForm
    edc_groups = EDC.objects.all()
    serviceForm = AddServicesForm
    sg_obj = Service.objects.all()

    return render(request, 'portal/servicegrouping.html', {'sg': sg_form, 'sg_obj': sg_obj, 'serviceForm': serviceForm, 'edc_groups': edc_groups})


def addService(request):

    if request.method == "POST":
        form = SGForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Successfully added')
        else:
            return HttpResponse('Name already exists')


def deleteService(request):

    name = request.GET.get('name')
    query_obj = Service.objects.get(name=name)
    query_obj.delete()
    return HttpResponse('{} is deleted'.format(name))


def servicesMapping(request):

    if request.method == "POST":
        form = AddServicesForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Successfully added')
        else:

            return HttpResponse('Service Mapping Failed. Try Again!')

# for testing


def displayServiceView(request):

    groupName = request.GET.get("groupName")
    edc_groups = EDC.objects.all()
    sg_obj = Service.objects.all()
    sg_form = SGForm
    serviceForm = AddServicesForm
    query_objects = Service_Grouping.objects.filter(serviceGroup=groupName)
    return render(request, "portal/servicelist.html", {'sg': sg_form, 'sg_obj': sg_obj, 'serviceForm': serviceForm, 'services': query_objects, 'edc_groups': edc_groups})


def serviceUpdateView(request):

    if request.method == "POST":
        s_id = request.POST.get("id")
        obj = Service_Grouping.objects.get(pk=s_id)
        form = AddServicesForm(request.POST, instance=obj)
        form.save()
        return HttpResponse('service updated')
    else:

        return HttpResponse('Service update Failed. Try Again!')


def serviceDeleteView(request):

    number = request.GET.get('number')
    obj = Service_Grouping.objects.get(serviceNumber=number)
    obj.delete()
    return HttpResponse('Service is deleted ')


def statementView(request):
    # passing group objects
    sg_obj = Service.objects.all()
    return render(request, 'portal/statement.html', {'sg_obj': sg_obj})


def statementDownloadView(request):

    # get query params from request object

    month = request.GET.get('month')
    year = request.GET.get('year')
    sg_obj = Service.objects.all()
    if month and year:
        # get service numbers from the group
        reading_querySets = GeneratorReadings.objects.filter(statementMonth=month, statementYear=year)
        return render(request, 'portal/showreadings.html', {'readings': reading_querySets, 'sg_obj': sg_obj, 'month': month, 'year': year})

    else:
        return render(request, 'portal/showreadings.html', {'sg_obj': sg_obj})


def statementFetchView(request):
    """ this function view handles serach services by service group """

    sg_obj = Service.objects.all()
    group = request.POST.get('group')
    month = request.POST.get('month')
    year = request.POST.get('year')
    # get service numbers from the group
    services = Service_Grouping.objects.filter(serviceGroup__name=group)
    consumerList = services.values('serviceNumber')
    readings = []
    # query the model using multiple params put in list
    for service in consumerList:
        query_set = GeneratorReadings.objects.filter(statementMonth=month, statementYear=year, consumerID=service['serviceNumber'])
        readings.append(query_set)

    return render(request, 'portal/statementreports.html', {'sg_obj': sg_obj, 'readings': readings})


def showSingleReadings(request):

    month = request.GET.get('month')
    year = request.GET.get('year')
    consumerID = request.GET.get('consumerID')

    query_set = GeneratorReadings.objects.filter(statementMonth=month, statementYear=year, consumerID=consumerID)

    return render(request, 'portal/showSingleReadings.html', {'readings': query_set})


def meterReadingView(request):

    return render(request, 'portal/meterreadings.html')


def meterReadingShowView(request):

    month = request.GET.get('month')
    year = request.GET.get('year')

    query_set = meterReadings.objects.filter(month=month, year=year)

    return render(request, 'portal/showmeterreadings.html', {'readings': query_set, 'month': month, 'year': year})
