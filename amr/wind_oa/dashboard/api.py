import requests
import json
from django.conf import settings
# data cleanup helper functions


def cleanup(data):

    slots_read = []

    charges = data['generationStatementCharges']
    slots = data['generationStatementSlots']

    slots_read.append(data['dispCompanyServiceNumber'])
    slots_read.append(data['statementMonth'])
    slots_read.append(data['statementYear'])

    read_req = ['impUnits', 'expUnits', 'netUnits', 'bankedBalance']

    for val in read_req:

        for s in slots:

            slots_read.append(s[val])

    for c in charges:

        slots_read.append(c['totalCharges'])

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
    get_auth = make_request('post', settings.LOGIN_URL, headers, payload=login_data)
    token = get_auth['token']
    headers.update({'Authorization': token})
    get_genrep_id = make_request('get', settings.GEN_STATEMENT_URL, headers, payload=gen_data)
    report_id = get_genrep_id[0]['id']
    reading = make_request('get', settings.READINGS_URL.format(report_id), headers)
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
        edc = consumer['EDC']

        n = consumer['id']

        login_data = build_login_payload(n, settings.API_PASSWORD)

        gen_data = build_gen_payload(edc, n, month, year)

        results = get_reading(login_data=login_data, gen_data=gen_data)

        data = cleanup(results)

        data_bin.append(data)

    return data_bin
