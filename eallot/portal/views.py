from django.shortcuts import render
from portal.forms import SGForm, AddServicesForm, EDC
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from portal.models import Service, Service_Grouping, GeneratorReadings
from django.shortcuts import get_object_or_404
from django.core import serializers
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
    # query the model using multiple params
    query_set = GeneratorReadings.objects.filter(statementMonth=month, statementYear=year)
    readings = serializers.serialize("json", list(query_set), fields=('name'))
    return HttpResponse(readings)


def statementView(request):

    # passing group objects
    sg_obj = Service.objects.all()

    return render(request, 'portal/statement.html', {'sg_obj': sg_obj})
