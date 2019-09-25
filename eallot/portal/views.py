from django.shortcuts import render
from portal.forms import SGForm, AddServicesForm, EDC
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from portal.models import Service, Service_Grouping, GeneratorReadings
from django.shortcuts import get_object_or_404
from django.core import serializers
from portal.api import main
from django.db import IntegrityError
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
    # lookup the service grouping table with received group
    services = Service_Grouping.objects.filter(serviceGroup__name=group)
    consumerList = services.values('serviceNumber', 'serviceZone__code')
    data = main(month, year, consumerList)
    print(data)

    for i in data:
        try:
            cursor = GeneratorReadings.objects.create(genstatementID=i[0], consumerID=i[1], statementMonth=i[2], statementYear=i[3], companyName=i[4], impUnitsC1=i[5], impUnitsC2=i[6], impUnitsC3=i[7], impUnitsC4=i[8], impUnitsC5=i[9], expUnitsC1=i[10], expUnitsC2=i[11], expUnitsC3=i[12], expUnitsC4=i[13], expUnitsC5=i[14], netUnitsC1=i[15], netUnitsC2=i[16], netUnitsC3=i[17], netUnitsC4=i[18], netUnitsC5=i[19], bankingC1=i[20], bankingC2=i[21], bankingC3=i[22], bankingC4=i[23], bankingC5=i[24], chargesC002=i[25], chargesC003=i[26], chargesC004=i[27], chargesC005=i[28], chargesC006=i[29], chargesC007=i[30], chargesC001=i[31])
            cursor.save()
            print('saved value for {}'.format(i[1]))

        except IntegrityError as e:
            print('already exists')

    return HttpResponse(status=204)

    # # query the model using multiple params
    # query_set = GeneratorReadings.objects.filter(statementMonth=month, statementYear=year)
    # readings = serializers.serialize("json", list(query_set), fields=(''))
    # return HttpResponse(readings)


def statementView(request):

    # passing group objects
    sg_obj = Service.objects.all()
    return render(request, 'portal/statement.html', {'sg_obj': sg_obj})
