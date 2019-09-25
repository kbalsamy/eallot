from django.shortcuts import render
from .api import main
from django.http import HttpResponse
from .models import ServiceGroup, Readings
from django.db import IntegrityError

# Create your views here.


def mainView(request):

    return render(request, 'dashboard/index.html')


def downloadView(request):

    month = request.GET.get('month')
    year = request.GET.get('year')
    consumer = request.GET.get('customer')
    consumerList = []

    consumer_query = ServiceGroup.objects.filter(customer__customer_name=consumer)
    print(consumer_query)
    for consumer in consumer_query:
        consumerList.append({'EDC': consumer.edc.code, 'id': consumer.serviceNumber})

    data = main(month, year, consumerList)

    try:
        for i in data:
            print(len(i))
            cursor = Readings.objects.create(consumerID=i[0], statementMonth=i[1], statementYear=i[2], impUnitsC1=i[3], impUnitsC2=i[4], impUnitsC3=i[5], impUnitsC4=i[6], impUnitsC5=i[7], expUnitsC1=i[8], expUnitsC2=i[9], expUnitsC3=i[10], expUnitsC4=i[11], expUnitsC5=i[12], netUnitsC1=i[13], netUnitsC2=i[14], netUnitsC3=i[15], netUnitsC4=i[16], netUnitsC5=i[17], bankingC1=i[18], bankingC2=i[19], bankingC3=i[20], bankingC4=i[21], bankingC5=i[22], chargesC002=i[23], chargesC003=i[24], chargesC004=i[25], chargesC005=i[26], chargesC006=i[27], chargesC007=i[28], chargesC001=i[29])
            cursor.save()

    except:
        pass

    return HttpResponse('success')


def readingView(request):

    month = request.POST.get('month')
    year = request.POST.get('year')
    customer = request.POST.get('customer')

    reading = Readings.objects.filter(statementMonth=month)
    timeperiod = {'month': month, 'year': year}
    return render(request, 'dashboard/readings.html', {'readings': reading, 'time': timeperiod})
