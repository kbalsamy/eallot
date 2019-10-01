import requests
import json
import sqlite3
from datetime import datetime
import os

API_PASSWORD = os.environ.get('password')
LOGIN_URL = "http://htoa.tnebnet.org/oa-auth-service//tokens/login"
GEN_STATEMENT_URL = "http://htoa.tnebnet.org/oa-service//api/gs/generationstatements?"
READINGS_URL = "http://htoa.tnebnet.org/oa-service//api/meterreading/{}"
METER_READING_URL = "http://htoa.tnebnet.org/oa-service//transaction/meterreadings?"


def cleanup(results):

    data_bin = []

    reading_id = results['id']
    serviceNumber = results['companyServiceNumber']
    month = results['readingMonthCode']
    year = results['readingYear']

    for i in [reading_id, serviceNumber, month, year]:
        data_bin.append(i)

    monthly_reading = results['meterReadingSlot']

    for reading in monthly_reading:

        impUnits = int(reading['impUnits'])
        expUnits = int(reading['expUnits'])
        netUnits = expUnits - impUnits

        data_bin.append(netUnits)

    return data_bin


def make_request(method, url, headers, payload=None):

    if method == 'get' and payload is None:
        resp = requests.get(url, headers=headers)
        return resp.json()

    elif method == 'get' and payload:
        resp = requests.get(url, params=payload, headers=headers)

        return resp.json()

    else:
        resp = requests.post(url, data=json.dumps(payload), headers=headers)
        return resp.json()


def get_reading(login_data=None, gen_data=None):

    headers = {"Accept": "application/json", "Content-Type": "application/json",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0"}
    get_auth = make_request('post', LOGIN_URL, headers, payload=login_data)
    token = get_auth['token']
    headers.update({'Authorization': token})
    meter_readings = make_request('get', METER_READING_URL, headers, payload=gen_data)
    if meter_readings:
        reading_id = meter_readings[0]['id']
        get_reading = make_request('get', READINGS_URL.format(reading_id), headers)
        return get_reading


def build_login_payload(serviceNumber, password):

    data = {"userName": serviceNumber, "password": password, "appClientId": "OA"}

    return data


def build_gen_payload(edc, serviceNumber, month, year):

    payload = {'dummy': '1', 'company-service-number': serviceNumber, 'org-id': edc, "month": month,
               'year': year}

    return payload


def main(month, year, consumerList):

    data_bin = []

    for consumer in consumerList:
        edc = consumer['serviceZone__code']
        n = consumer['serviceNumber']
        print('fetching for {}'.format(n))
        login_data = build_login_payload(n, API_PASSWORD)
        gen_data = build_gen_payload(edc, n, month, year)
        results = get_reading(login_data=login_data, gen_data=gen_data)
        if results:
            data = cleanup(results)
            data_bin.append(data)

    return data_bin


def db(month, year, consumerList):
    tablename = 'portal_meterreadings'
    con = sqlite3.connect('db.sqlite3')
    cursor = con.cursor()
    data = main(month, year, consumerList)
    if data:
        for i in data:
            print(i)
            try:
                insert_values = cursor.execute("""INSERT INTO portal_meterreadings (readingID, serviceNumber, month, year,netUnitsC1, netUnitsC2, netUnitsC3, netUnitsC4, netUnitsC5) values (?,?,?,?,?,?,?,?,?)""", (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]))
                con.commit()
                print('saved')
            except sqlite3.IntegrityError as e:
                print("Already exists")
    else:
        print('statement not uploaded')


data = json.loads(open('consumerList.json').read())
consumerList = json.loads(data, encoding='utf-8')
currentMonth = datetime.now().month
currentYear = str(datetime.now().year)
month = "0" + str(currentMonth)


schedule = db('07', currentYear, consumerList)
