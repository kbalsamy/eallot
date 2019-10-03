import requests
import json
import sqlite3
from datetime import datetime
import os

API_PASSWORD = "niSMJC6TMwZWk8qqMR6R9g=="
LOGIN_URL = "http://htoa.tnebnet.org/oa-auth-service//tokens/login"
GEN_STATEMENT_URL = "http://htoa.tnebnet.org/oa-service//api/gs/generationstatements?"
READINGS_URL = "http://htoa.tnebnet.org/oa-service//api/gs/generationstatement/{}"


def checkCharges(charges):

    results = []

    charges_dict = {}

    for charge in charges:

        charges_dict.update({charge['chargeCode']: charge['totalCharges']})

    results.append(charges_dict)
    return results


# data cleanup helper functions


def cleanup(data):

    slots_read = []

    slots_read.append(data['id'])
    slots_read.append(data['dispCompanyServiceNumber'])
    slots_read.append(data['statementMonth'])
    slots_read.append(data['statementYear'])
    slots_read.append(data['dispCompanyName'])
    charges = data['generationStatementCharges']
    slots = data['generationStatementSlots']

    read_req = ['impUnits', 'expUnits', 'netUnits', 'bankedBalance']

    for val in read_req:
        for s in slots:
            slots_read.append(s[val])

    final_charges = checkCharges(charges)
    slots_read += final_charges
    return slots_read


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
    try:
        token = get_auth['token']
    except:
        token = None

    while token == None:
        get_auth = make_request('post', LOGIN_URL, headers, payload=login_data)
        token = get_auth['token']
        print("getting access token")

    headers.update({'Authorization': token})
    get_genrep_id = make_request('get', GEN_STATEMENT_URL, headers, payload=gen_data)
    if get_genrep_id:
        report_id = get_genrep_id[0]['id']
        reading = make_request('get', READINGS_URL.format(report_id), headers)
        return reading


def build_login_payload(serviceNumber, password):

    data = {"userName": serviceNumber, "password": password, "appClientId": "OA"}

    return data


def build_gen_payload(edc, serviceNumber, month, year):

    payload = {'dummy': '1', 'edc-id': edc, 'service-number': serviceNumber, "statement-month": month,
               'statement-year': year}

    return payload


def main(month, year, consumerList):

    tablename = 'portal_generatorreadings'
    con = sqlite3.connect('db.sqlite3')
    cursor = con.cursor()
    # data_bin = []

    for consumer in consumerList:

        edc = consumer['serviceZone__code']
        n = consumer['serviceNumber']
        print('fetching for {}'.format(n))
        login_data = build_login_payload(n, API_PASSWORD)
        gen_data = build_gen_payload(edc, n, month, year)
        results = get_reading(login_data=login_data, gen_data=gen_data)
        if results:
            data = cleanup(results)
            try:
                insert_values = cursor.execute("""INSERT INTO portal_generatorreadings (genstatementID, consumerID, statementMonth, statementYear,companyName,impUnitsC1,impUnitsC2, impUnitsC3, impUnitsC4,impUnitsC5, expUnitsC1, expUnitsC2,expUnitsC3, expUnitsC4, expUnitsC5,netUnitsC1, netUnitsC2, netUnitsC3, netUnitsC4, netUnitsC5,bankingC1, bankingC2, bankingC3, bankingC4, bankingC5, chargesC002, chargesC003, chargesC004, chargesC005, chargesC006, chargesC007, chargesC008,chargesC001) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11], data[12], data[13], data[14], data[15], data[16], data[17], data[18], data[19], data[20], data[21], data[22], data[23], data[24], data[25].get('C002', 0.0), data[25].get('C003', 0.0), data[25].get('C004', 0.0), data[25].get('C005', 0.0), data[25].get('C006', 0.0), data[25].get('C007', 0.0), data[25].get('C008', 0.0), data[25].get('C001', 0.0)))

                con.commit()
                print('saved')

            except sqlite3.IntegrityError as e:
                print("Already exists")
            # data_bin.append(data)

        else:
            date = datetime.now()
            with open('summary.txt', 'a') as f:
                f.write('{}: reading are not updated for {} \n' .format(datetime.strftime(date, "%d/%m/%y- %H:%M:%S"), n))
                f.close()
            print("readings are not updated for {}".format(n))


def db(month, year, consumerList):

    data = main(month, year, consumerList)


data = json.loads(open('consumerList.json').read())
consumerList = json.loads(data, encoding='utf-8')
currentMonth = datetime.now().month
currentYear = str(datetime.now().year)
month = str(currentMonth)


schedule = db("09", currentYear, consumerList)
