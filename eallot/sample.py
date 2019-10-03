# import os

# print(os.environ.get('password'))

 # if data:
    #     for i in data:
    #         try:
    #             insert_values = cursor.execute("""INSERT INTO portal_generatorreadings (genstatementID, consumerID, statementMonth, statementYear,companyName,impUnitsC1,impUnitsC2, impUnitsC3, impUnitsC4,impUnitsC5, expUnitsC1, expUnitsC2,expUnitsC3, expUnitsC4, expUnitsC5,netUnitsC1, netUnitsC2, netUnitsC3, netUnitsC4, netUnitsC5,bankingC1, bankingC2, bankingC3, bankingC4, bankingC5, chargesC002, chargesC003, chargesC004, chargesC005, chargesC006, chargesC007, chargesC008,chargesC001) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", (i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23], i[24], i[25].get('C002', 0.0), i[25].get('C003', 0.0), i[25].get('C004', 0.0), i[25].get('C005', 0.0), i[25].get('C006', 0.0), i[25].get('C007', 0.0), i[25].get('C008', 0.0), i[25].get('C001', 0.0)))
    #             con.commit()
    #             print('saved')

    #         except sqlite3.IntegrityError as e:
    #             print("Already exists")
    # else:
    #     print('statement not uploaded')
