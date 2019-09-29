codes = ['C002', 'C003', 'C004', 'C005', 'C006', 'C007', 'C008' 'C001']

results = [{u'unitCharge': None, u'chargeTypeCode': u'FORMULA', u'chargeTypeName': u'Formula Based Charge', u'generationStatementId': u'376317', u'chargeDesc': u'Transmission Charges', u'remarks': None, u'chargeCode': u'C003', u'id': u'2328242', u'totalCharges': u'63784'}, {u'unitCharge': None, u'chargeTypeCode': u'FORMULA', u'chargeTypeName': u'Formula Based Charge', u'generationStatementId': u'376317', u'chargeDesc': u'System Operation Charges', u'remarks': None, u'chargeCode': u'C004', u'id': u'2328243', u'totalCharges': u'709'}, {u'unitCharge': None, u'chargeTypeCode': u'FORMULA', u'chargeTypeName': u'Formula Based Charge', u'generationStatementId': u'376317', u'chargeDesc': u'RKvah Penalty', u'remarks': None, u'chargeCode': u'C005', u'id': u'2328244', u'totalCharges': u'247'}, {u'unitCharge': None, u'chargeTypeCode': u'FORMULA', u'chargeTypeName': u'Formula Based Charge', u'generationStatementId': u'376317', u'chargeDesc': u'Negative Energy Charges', u'remarks': None, u'chargeCode': u'C006', u'id': u'2328245', u'totalCharges': u'0'}, {u'unitCharge': None, u'chargeTypeCode': u'FORMULA', u'chargeTypeName': u'Formula Based Charge', u'generationStatementId': u'376317', u'chargeDesc': u'Scheduling Charges', u'remarks': None, u'chargeCode': u'C007', u'id': u'2328246', u'totalCharges': u'2240'}, {u'unitCharge': u'300', u'chargeTypeCode': u'LUMP_SUM', u'chargeTypeName': u'Lump Sum Charge', u'generationStatementId': u'376317', u'chargeDesc': u'Meter Reading Charges', u'remarks': None, u'chargeCode': u'C001', u'id': u'2328241', u'totalCharges': u'300'}]

final = []

charges_dict = {}

for r in results:

    charges_dict.update({r['chargeCode']: r['totalCharges']})


final.append(charges_dict)

print (final)

# for r in results:

#     charges_dict.append({r['chargeCode']: r['totalCharges']})

# vals = []

# for charge in charges_dict:

#     inner_list = []

#     for code in codes:

#         vals.append(charge.get(code, 0))

# print(vals)

# if type(vals[0]) != unicode:
#     final = vals[1::8]
#     final.insert(0, 0)
#     print(final)


# if type(vals[1]) != unicode:
#     final = [vals[0], vals[9], vals[9 + 8], vals[9 + 8 + 8], vals[9 + 8 + 8 + 8], vals[9 + 8 + 8 + 8 + 8]]
#     final.insert(1, 0)
#     print(final)

# if type(vals[2]) != unicode:
#     final = vals[1::8]
#     final.insert(0, 0)
#     print(final)
