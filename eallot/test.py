import requests
import json
import sqlite3

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

    if len(charges) == 7:
        for c in charges:
            slots_read.append(c['totalCharges'])
        return slots_read

    else:
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
    token = get_auth['token']
    headers.update({'Authorization': token})
    get_genrep_id = make_request('get', GEN_STATEMENT_URL, headers, payload=gen_data)
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

    data_bin = []

    for consumer in consumerList:
        edc = consumer['serviceZone__code']
        n = consumer['serviceNumber']
        print('fetchinf for {}'.format(n))
        login_data = build_login_payload(n, API_PASSWORD)
        gen_data = build_gen_payload(edc, n, month, year)
        results = get_reading(login_data=login_data, gen_data=gen_data)
        data = cleanup(results)
        data_bin.append(data)

    return data_bin


def db(month, year, consumerList):
    tablename = 'portal_generatorreadings'
    con = sqlite3.connect('db.sqlite3')
    cursor = con.cursor()
    data = main(month, year, consumerList)

    print(len(data[0]))
    if data:
        for i in data:
            print[i[25]]
            try:
                insert_values = cursor.execute("""INSERT INTO portal_generatorreadings (genstatementID, consumerID, statementMonth, statementYear,companyName,impUnitsC1,impUnitsC2, impUnitsC3, impUnitsC4,impUnitsC5, expUnitsC1, expUnitsC2,expUnitsC3, expUnitsC4, expUnitsC5,netUnitsC1, netUnitsC2, netUnitsC3, netUnitsC4, netUnitsC5,bankingC1, bankingC2, bankingC3, bankingC4, bankingC5, chargesC002, chargesC003, chargesC004, chargesC005, chargesC006, chargesC007, chargesC008,chargesC001) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25].get('C002', 0.0), i[25].get('C003', 0.0), i[25].get('C004', 0.0), i[25].get('C005', 0.0), i[25].get('C006', 0.0), i[25].get('C007', 0.0), i[25].get('C008', 0.0), i[25].get('C001', 0.0)))
                con.commit()
                print('saved')
            except sqlite3.IntegrityError as e:
                print(failed)


# check = db('09', '2019', consumerList)
