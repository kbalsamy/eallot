from django.shortcuts import render
from portal.forms import SGForm, AddServicesForm
from django.http import HttpResponseRedirect, HttpResponse
from portal.models import Service, Service_Grouping
# Create your views here.


def router(request):

    sg_form = SGForm
    serviceForm = AddServicesForm
    sg_obj = Service.objects.all()

    if request.method == "POST":
        query_objects = request.POST.get('groupName')
        query_objects = Service_Grouping.objects.filter(serviceGroup=query_objects)
        return render(request, 'portal/servicegrouping.html', {'sg': sg_form, 'sg_obj': sg_obj, 'serviceForm': serviceForm, 'services': query_objects})
    else:
        return render(request, 'portal/servicegrouping.html', {'sg': sg_form, 'sg_obj': sg_obj, 'serviceForm': serviceForm})


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
    print(name)
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
