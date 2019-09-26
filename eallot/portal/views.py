from django.shortcuts import render
from portal.forms import SGForm, AddServicesForm, EDC
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from portal.models import Service, Service_Grouping, GeneratorReadings
from django.shortcuts import get_object_or_404
from django.core import serializers
from portal.api import main
from django.db import IntegrityError
import json
# Create your views here.


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


def statementDownloadView(request):

    # get query params from request object
    # get all the service number in the selected group
    group = request.POST.get('group')
    month = request.POST.get('month')
    year = request.POST.get('year')
    # get service numbers from the group
    services = Service_Grouping.objects.filter(serviceGroup__name=group)
    consumerList = services.values('serviceNumber')
    readings = []
    # query the model using multiple params put in list
    for service in consumerList:
        query_set = GeneratorReadings.objects.filter(statementMonth=month, statementYear=year, consumerID=service['serviceNumber']).values('consumerID', 'netUnitsC1', 'netUnitsC2', 'netUnitsC3', 'netUnitsC4', 'netUnitsC5', 'bankingC1', 'bankingC2', 'bankingC3', 'bankingC4', 'bankingC5', 'chargesC002', 'chargesC003', 'chargesC004', 'chargesC005', 'chargesC006', 'chargesC007', 'chargesC001')
        values = list(query_set)
        readings.append(values)

    return JsonResponse(readings, safe=False)


def statementView(request):
    # passing group objects
    sg_obj = Service.objects.all()
    return render(request, 'portal/statement.html', {'sg_obj': sg_obj})


def statementFetchView(request):

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
