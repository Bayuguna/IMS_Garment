# update database bank jika data toko ditambah, diupdate, dan di delete dan jika data bank ditambah, diupdate dan didelete
import pymysql
import time
import json

print('|---Integrasi Migrasi Sistem---|')
print('|--------------BY-------------|')
print('|   Eka Krisna   (1605552007) |')
print('|   Bayuguna     (1605552011) |')
print('|   Dode Aditya  (1605552024) |')
print('')
#koneksi
dbToko = pymysql.connect("localhost","root","","toko_kain")
dbGarmen = pymysql.connect("localhost","root","","garmen")

#cursor = db.cursor()
curToko = dbToko.cursor()
curGarmen = dbGarmen.cursor()

#input time sleep untuk waktu delay
delay = int(input("masukan waktu delay : "))

#function untuk file Report.json yang menyimpan data report dari Database Toko
def InsertJson(id, jenis_kain, kwalitas_kain, tekstur_kain, warna_kain, panjang_kain, harga):
    list_data = []
    with open('reportToko.json', 'r', encoding='utf-8') as report:
        try:
            data = json.load(report)
        except:
            data = []
    new_entry = {'id': str(id), 'jenis_kain': jenis_kain, 'kwalitas_kain': kwalitas_kain, 'tekstur_kain': str(tekstur_kain),
                 'warna_kain': warna_kain, 'panjang_kain': panjang_kain, 'harga': str(harga), 'action': 'insert', 'status': '0'}
    list_data.append(new_entry)
    with open('reportToko.json', 'w', encoding='utf-8') as report:
        json.dump(data + list_data, report, indent=4)

def UpdateJson(id, jenis_kain, kwalitas_kain, tekstur_kain, warna_kain, panjang_kain, harga):
    list_data = []
    with open('reportToko.json', 'r', encoding='utf-8') as report:
        try:
            data = json.load(report)
        except:
            data = []
    new_entry = {'id': str(id), 'jenis_kain': jenis_kain, 'kwalitas_kain': kwalitas_kain,'tekstur_kain': str(tekstur_kain),
                 'warna_kain': warna_kain, 'panjang_kain': panjang_kain, 'harga': str(harga), 'action': 'update','status': '0'}
    list_data.append(new_entry)
    with open('reportToko.json', 'w', encoding='utf-8') as report:
        json.dump(data + list_data, report, indent=4)

def DeleteJson(id, jenis_kain, kwalitas_kain, tekstur_kain, warna_kain, panjang_kain, harga):
    list_data = []
    with open('reportToko.json', 'r', encoding='utf-8') as report:
        try:
            data = json.load(report)
        except:
            data = []
    new_entry = {'id': str(id), 'jenis_kain': jenis_kain, 'kwalitas_kain': kwalitas_kain,'tekstur_kain': str(tekstur_kain),
                 'warna_kain': warna_kain, 'panjang_kain': panjang_kain, 'harga': str(harga), 'action': 'delete','status': '0'}
    list_data.append(new_entry)
    with open('reportToko.json', 'w', encoding='utf-8') as report:
        json.dump(data + list_data, report, indent=4)

#function untuk insert data report dari database Bank
def InsertJsonGarmen(id, jenis_kain, kwalitas_kain, tekstur_kain, warna_kain, panjang_kain, harga):
    list_data = []
    with open('reportGarmen.json', 'r', encoding='utf-8') as report:
        try:
            data = json.load(report)
        except:
            data = []
    new_entry = {'id': str(id), 'jenis_kain': jenis_kain, 'kwalitas_kain': kwalitas_kain,'tekstur_kain': str(tekstur_kain),
                 'warna_kain': warna_kain, 'panjang_kain': panjang_kain, 'harga': str(harga), 'action': 'insert','status': '0'}
    list_data.append(new_entry)
    with open('reportGarmen.json', 'w', encoding='utf-8') as report:
        json.dump(data + list_data, report, indent=4)

def UpdateJsonGarmen(id, jenis_kain, kwalitas_kain, tekstur_kain, warna_kain, panjang_kain, harga):
    list_data = []
    with open('reportGarmen.json', 'r', encoding='utf-8') as report:
        try:
            data = json.load(report)
        except:
            data = []
    new_entry = {'id': str(id), 'jenis_kain': jenis_kain, 'kwalitas_kain': kwalitas_kain,'tekstur_kain': str(tekstur_kain),
                 'warna_kain': warna_kain, 'panjang_kain': panjang_kain, 'harga': str(harga),'action': 'update', 'status': '0'}
    list_data.append(new_entry)
    with open('reportGarmen.json', 'w', encoding='utf-8') as report:
        json.dump(data + list_data, report, indent=4)

def DeleteJsonGarmen(id, jenis_kain, kwalitas_kain, tekstur_kain, warna_kain, panjang_kain, harga):
    list_data = []
    with open('reportGarmen.json', 'r', encoding='utf-8') as report:
        try:
            data = json.load(report)
        except:
            data = []
    new_entry = {'id': str(id), 'jenis_kain': jenis_kain, 'kwalitas_kain': kwalitas_kain,'tekstur_kain': str(tekstur_kain),
                 'warna_kain': warna_kain, 'panjang_kain': panjang_kain, 'harga': str(harga), 'action': 'delete','status': '0'}
    list_data.append(new_entry)
    with open('reportGarmen.json', 'w', encoding='utf-8') as report:
        json.dump(data + list_data, report, indent=4)

def Cek(Transaksi, cur1, db1):

    if  Transaksi == 'toko_kain':
        # koneksi
        dbToko = pymysql.connect("localhost", "root", "", "toko_kain")

        # cursor
        curToko = dbToko.cursor()

        # select semua data dari tb_transaksi pada Database Toko
        curToko.execute("SELECT * FROM tb_transaksi;")
        data = curToko.fetchall()

        # select semua data dari tb_transaksi_backup pada Database Toko
        curToko.execute("SELECT * FROM tb_transaksi_backup;")
        dataBackup = curToko.fetchall()

        # hitung banyak data
        jumlahData = len(data)
        jumlahDataBackup = len(dataBackup)

        dbToko.close()

    elif Transaksi == 'garmen':
        dbGarmen = pymysql.connect("localhost", "root", "", "garmen")

        curGarmen = dbGarmen.cursor()

        # select semua data dari tb_transaksi pada Database Bank
        curGarmen.execute("SELECT * FROM tb_transaksi;")
        data = curGarmen.fetchall()

        # select semua data dari tb_transaksi_backup pada Database Bank
        curGarmen.execute("SELECT * FROM tb_transaksi_backup;")
        dataBackup = curGarmen.fetchall()

        # hitung banyak data
        jumlahData = len(data)
        jumlahDataBackup = len(dataBackup)

        dbGarmen.close()

    else:
        print("Error")

    if jumlahData == jumlahDataBackup:
        # proses penyocokan data
        for i in range(0, jumlahData):
            # cek pembaruan no rekening
            if data[i][1] != dataBackup[i][1]:
                print(
                    "Update data pada Database %s pada data jenis_kain, data sebelumnya adalah %s diupdate menjadi %s pada id %s" % (
                    Transaksi, dataBackup[i][1], data[i][1], data[i][0]))

                # proses update pada tb transaksi backup pada Database Toko
                cur1.execute("UPDATE tb_transaksi_backup SET jenis_kain='%s' WHERE id=%s;" % (
                data[i][1], dataBackup[i][0]))
                db1.commit()

                if Transaksi == 'toko_kain':
                    UpdateJson(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4],
                               data[i][5], data[i][6])
                elif Transaksi == 'garmen':
                    UpdateJsonGarmen(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4],
                               data[i][5], data[i][6])


            # cek pembaruan atas nama
            elif data[i][2] != dataBackup[i][2]:
                print(
                    "Update data pada Database %s pada data kwalitas_kain, data sebelumnya adalah %s diupdate menjadi %s pada id %s" % (
                    Transaksi, dataBackup[i][2], data[i][2], data[i][0]))

                # update tb transaksi backup
                sql = "UPDATE tb_transaksi_backup SET kwalitas_kain='%s' WHERE id=%s;" % (
                data[i][2], dataBackup[i][0])
                cur1.execute(sql)
                db1.commit()

                if Transaksi == 'toko_kain':
                    UpdateJson(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4],
                           data[i][5], data[i][6])
                elif Transaksi == 'garmen':
                    UpdateJsonGarmen(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4],
                                   data[i][5], data[i][6])

            # cek pembaruan jumlah
            elif data[i][3] != dataBackup[i][3]:
                print(
                    "Update data pada Database %s pada data tekstur_kain, data sebelumnya adalah %s diupdate menjadi %s pada id %s" % (
                    Transaksi, dataBackup[i][3], data[i][3], data[i][0]))

                # update tb transaksi backup
                sql = "UPDATE tb_transaksi_backup SET tekstur_kain='%s' WHERE id=%s;" % (
                data[i][3], dataBackup[i][0])
                cur1.execute(sql)
                db1.commit()

                if Transaksi == 'toko_kain':
                    UpdateJson(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4],
                           data[i][5], data[i][6])
                elif Transaksi == 'garmen':
                    UpdateJsonGarmen(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4],
                                   data[i][5], data[i][6])

            # cek pembaruan kode unik
            elif data[i][4] != dataBackup[i][4]:
                print(
                    "Update data pada Database %s pada data warna_kain, data sebelumnya adalah %s diupdate menjadi %s pada id %s" % (
                    Transaksi, data[i][4], data[i][4], data[i][0]))

                # update tb transaksi backup
                sql = "UPDATE tb_transaksi_backup SET warna_kain='%s' WHERE id=%s;" % (
                data[i][4], dataBackup[i][0])
                cur1.execute(sql)
                db1.commit()

                if Transaksi == 'toko_kain':
                    UpdateJson(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4],
                           data[i][5], data[i][6])
                elif Transaksi == 'garmen':
                    UpdateJsonGarmen(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4],
                                   data[i][5], data[i][6])

            # cek pembaruan status
            elif data[i][5] != dataBackup[i][5]:
                print(
                    "Update data pada Database %s pada data panjang_kain, data sebelumnya adalah %s diupdate menjadi %s pada id %s" % (
                    Transaksi, dataBackup[i][5], data[i][5], data[i][0]))

                # update tb transaksi backup
                sql = "UPDATE tb_transaksi_backup SET panjang_kain=%s WHERE id=%s;" % (
                data[i][5], dataBackup[i][0])
                cur1.execute(sql)
                db1.commit()

                if Transaksi == 'toko_kain':
                    UpdateJson(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4],
                           data[i][5], data[i][6])
                elif Transaksi == 'garmen':
                    UpdateJsonGarmen(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4],
                                   data[i][5], data[i][6])

            # cek pembaruan tanggal
            elif data[i][6] != dataBackup[i][6]:
                print(
                    "Update data pada Database %s pada data harga, data sebelumnya adalah %s diupdate menjadi %s pada id %s" % (
                    Transaksi, dataBackup[i][6], data[i][6], data[i][0]))

                # update tb transaksi backup
                sql = "UPDATE tb_transaksi_backup SET harga=%s WHERE id=%s;" % (
                data[i][6], dataBackup[i][0])
                cur1.execute(sql)
                db1.commit()

                if Transaksi == 'toko_kain':
                    UpdateJson(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4],
                           data[i][5], data[i][6])
                elif Transaksi == 'garmen':
                    UpdateJsonGarmen(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4],
                                   data[i][5], data[i][6])

            else:
                print("Checking %s" % (Transaksi))

    # proses pengecekan jika terjadi insert data baru di tabel
    elif jumlahData > jumlahDataBackup:

        # proses insert data baru
        insertMin = jumlahDataBackup
        beforeMaxInsert = jumlahData

        for i in range(insertMin, beforeMaxInsert):
            # pemberitahuan
            print(
                "Insert data pada Database %s dengan index %s ,data yang di-insert adalah jenis_kain =%s, kwalitas_kain = %s, tekstur_kain = %s, warna_kain = %s, panjang_kain = %s , harga = %s" % (
                Transaksi, data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5],
                data[i][6]))

            # insert into tb_transaksi_backup
            sql = "INSERT INTO tb_transaksi_backup(jenis_kain, kwalitas_kain, tekstur_kain, warna_kain, panjang_kain, harga) " \
                  "VALUES('%s','%s','%s','%s','%s','%s');" % (
            data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6])
            cur1.execute(sql)
            db1.commit()

            if Transaksi == 'toko_kain':
                InsertJson(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5],data[i][6])
            elif Transaksi == 'garmen':
                InsertJsonGarmen(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5],data[i][6])

    # proses ketika terjadi delete di tabel toko
    elif jumlahData < jumlahDataBackup:

        # proses delete yang terjadi jika id yang di delete pada tabel toko adalah id terakhir
        for i in range(0, jumlahDataBackup):

            cur1.execute("SELECT * FROM tb_transaksi WHERE tb_transaksi.`id`=%s;" % dataBackup[i][0])

            if cur1.rowcount == 0:
                print(
                    "Delete data pada Database %s dengan index %s,data yang di-delete adalah jenis_kain =%s, kwalitas_kain = %s, tekstur_kain = %s, kode unik = %s, panjang_kain = %s , harga = %s" % (
                        Transaksi, dataBackup[i][0], dataBackup[i][1], dataBackup[i][2], dataBackup[i][3],
                        dataBackup[i][4], dataBackup[i][5],
                        dataBackup[i][6]))

                # delete di tabel transaksi database 1
                sql = "DELETE FROM tb_transaksi_backup WHERE id=%s;" % dataBackup[i][0]
                cur1.execute(sql)
                db1.commit()

                if Transaksi == 'toko_kain':
                    DeleteJson(dataBackup[i][0], dataBackup[i][1], dataBackup[i][2], dataBackup[i][3], dataBackup[i][4],
                                   dataBackup[i][5], dataBackup[i][6])
                elif Transaksi == 'garmen':
                    DeleteJsonGarmen(dataBackup[i][0], dataBackup[i][1], dataBackup[i][2], dataBackup[i][3], dataBackup[i][4],
                                   dataBackup[i][5], dataBackup[i][6])

                # temp = i
                # pemberitahuan
                print(
                    "Delete data pada Database %s dengan index %s,data yang di-delete adalah jenis_kain =%s, kwalitas_kain = %s, tekstur_kain = %s, kode unik = %s, panjang_kain = %s , harga = %s" % (
                    Transaksi, dataBackup[i][0], dataBackup[i][1], dataBackup[i][2], dataBackup[i][3],dataBackup[i][4], dataBackup[i][5], dataBackup[i][6]))

        else:
            print("Checking Eror")

    else:
        print("Checking %s" %(Transaksi))

    # akhir dari chek data
    # time.sleep(delay)

    if Transaksi == 'toko_kain':
        # Cek Pembahruan dalam JSON file database bank
        with open('reportGarmen.json', 'r', encoding='utf-8') as report:
            try:
                dataJson = json.load(report)
            except:
                dataJson = []
        jumlahData = len(dataJson)
    elif Transaksi == 'garmen':
        # Cek Pembahruan dalam JSON file database toko
        with open('reportToko.json', 'r', encoding='utf-8') as report:
            try:
                dataJson = json.load(report)
            except:
                dataJson = []
        jumlahData = len(dataJson)

    if (dataJson is None) == False:
        for i in range(jumlahData):
            # memasukkan status action dan status perintah apakah belum atau sudah dijalankan
            action = dataJson[i]['action']
            status = dataJson[i]['status']

            # memasukkan nilai pada json ke variabel
            id_json = int(dataJson[i]['id'])
            jenis_kain_json = dataJson[i]['jenis_kain']
            kwalitas_kain_json = dataJson[i]['kwalitas_kain']
            tekstur_kain_json = dataJson[i]['tekstur_kain']
            warna_kain_json = dataJson[i]['warna_kain']
            panjang_kain_json = dataJson[i]['panjang_kain']
            harga_json = dataJson[i]['harga']

            # print(action)
            if action == 'update' and status == '0':
                for a in range(jumlahDataBackup):
                    if id_json == dataBackup[a][0]:
                        if jenis_kain_json != dataBackup[a][1]:
                            # print notifikasi
                            print(
                                "Terjadi perubahan pada Json, data sebelumnya %s berubah menjadi %s pada id %s" % (
                                    dataBackup[a][1], jenis_kain_json, id_json))

                            # update pada tabel tb_transaksi di database
                            cur1.execute(
                                "UPDATE tb_transaksi SET jenis_kain = '%s' WHERE id = %s" % (
                                    jenis_kain_json, id_json))
                            db1.commit()

                            # update pada tabel tb_transaksi_temp di database
                            cur1.execute(
                                "UPDATE tb_transaksi_backup SET jenis_kain = '%s' WHERE id = %s" % (
                                    jenis_kain_json, id_json))
                            db1.commit()

                            # memasukkan perubahan pada status run_bank menjadi 1
                            dataJson[i]['status'] = '1'
                            if Transaksi == 'toko_kain':
                                with open('reportGarmen.json', 'w', encoding='utf-8') as report:
                                    json.dump(dataJson, report, indent=4)
                            elif Transaksi == 'garmen':
                                with open('reportToko.json', 'w', encoding='utf-8') as report:
                                    json.dump(dataJson, report, indent=4)

                        if kwalitas_kain_json != dataBackup[a][2]:
                            # pemberitahuan
                            print(
                                "Terjadi perubahan pada Json, data sebelumnya %s berubah menjadi %s pada id %s" % (
                                    dataBackup[a][2], kwalitas_kain_json, id_json))

                            # update pada tb_transaksi di database bank
                            cur1.execute(
                                "UPDATE tb_transaksi SET kwalitas_kain = '%s' WHERE id = %s" % (
                                    kwalitas_kain_json, id_json))
                            db1.commit()

                            # update pada tabel tb_transaksi_temp di database bank
                            cur1.execute(
                                "UPDATE tb_transaksi_backup SET kwalitas_kain = '%s' WHERE id = %s" % (
                                    kwalitas_kain_json, id_json))
                            db1.commit()
                            # memasukkan perubahan pada status run_bank menjadi 1
                            dataJson[i]['status'] = '1'
                            if Transaksi == 'toko_kain':
                                with open('reportGarmen.json', 'w', encoding='utf-8') as report:
                                    json.dump(dataJson, report, indent=4)
                            elif Transaksi == 'garmen':
                                with open('reportToko.json', 'w', encoding='utf-8') as report:
                                    json.dump(dataJson, report, indent=4)

                        if tekstur_kain_json != dataBackup[a][3]:
                            # print notifikasi
                            print(
                                "Terjadi perubahan pada Json, data sebelumnya %s berubah menjadi %s pada id %s" % (
                                    dataBackup[a][3], tekstur_kain_json, id_json))
                            # update pada tb_transaksi di database bank
                            cur1.execute(
                                "UPDATE tb_transaksi SET tekstur_kain = '%s' WHERE id = %s" % (
                                    tekstur_kain_json, id_json))
                            db1.commit()
                            # update pada tb_transaksi_temp di database bank
                            cur1.execute(
                                "UPDATE tb_transaksi_backup SET tekstur_kain = '%s' WHERE id = %s" % (
                                    tekstur_kain_json, id_json))
                            db1.commit()
                            # memasukkan perubahan pada status run_bank menjadi 1
                            dataJson[i]['status'] = '1'
                            if Transaksi == 'toko_kain':
                                with open('reportGarmen.json', 'w', encoding='utf-8') as report:
                                    json.dump(dataJson, report, indent=4)
                            elif Transaksi == 'garmen':
                                with open('reportToko.json', 'w', encoding='utf-8') as report:
                                    json.dump(dataJson, report, indent=4)

                        if warna_kain_json != dataBackup[a][4]:
                            # print notifikasi
                            print(
                                "Terjadi perubahan pada Json, data sebelumnya %s berubah menjadi %s pada id %s" % (
                                    dataBackup[a][4], warna_kain_json, id_json))
                            # update pada tb_transaksi di database bank
                            cur1.execute(
                                "UPDATE tb_transaksi SET warna_kain = '%s' WHERE id = %s" % (
                                    warna_kain_json, id_json))
                            db1.commit()
                            # update pada tb_transaksi_temp di database bank
                            cur1.execute(
                                "UPDATE tb_transaksi_backup SET warna_kain = '%s' WHERE id = %s" % (
                                    warna_kain_json, id_json))
                            db1.commit()
                            # memasukkan perubahan pada status run_bank menjadi 1
                            dataJson[i]['status'] = '1'
                            if Transaksi == 'toko_kain':
                                with open('reportGarmen.json', 'w', encoding='utf-8') as report:
                                    json.dump(dataJson, report, indent=4)
                            elif Transaksi == 'garmen':
                                with open('reportToko.json', 'w', encoding='utf-8') as report:
                                    json.dump(dataJson, report, indent=4)
                        if panjang_kain_json != dataBackup[a][5]:
                            # print notifikasi
                            print(
                                "Terjadi perubahan pada Server, data sebelumnya %s berubah menjadi %s pada id %s" % (
                                    dataBackup[a][5], panjang_kain_json, id_json))
                            # update pada tb_transaksi di database bank
                            sql = "UPDATE tb_transaksi SET panjang_kain='%s' WHERE id=%s;" % (panjang_kain_json, id_json)
                            cur1.execute(sql)
                            db1.commit()
                            # update pada tb_transaksi_temp di database bank
                            cur1.execute(
                                "UPDATE tb_transaksi_backup SET panjang_kain = '%s' WHERE id = %s" % (
                                    panjang_kain_json, id_json))
                            db1.commit()
                            # memasukkan perubahan pada status run_bank menjadi 1
                            dataJson[i]['panjang_kain'] = '1'
                            if Transaksi == 'toko_kain':
                                with open('reportGarmen.json', 'w', encoding='utf-8') as report:
                                    json.dump(dataJson, report, indent=4)
                            elif Transaksi == 'garmen':
                                with open('reportToko.json', 'w', encoding='utf-8') as report:
                                    json.dump(dataJson, report, indent=4)

                        if (harga_json != dataBackup[a][6]):
                            # print notifikasi
                            print(
                                "Terjadi perubahan pada Server, data sebelumnya %s berubah menjadi %s pada id %s" % (
                                    dataBackup[a][6], harga_json, id_json))
                            # update pada tb_transaksi di database bank
                            cur1.execute(
                                "UPDATE tb_transaksi SET harga = '%s' WHERE id = %s" % (
                                    harga_json, id_json))
                            db1.commit()
                            # update pada tb_transaksi_temp di database bank
                            cur1.execute(
                                "UPDATE tb_transaksi_backup SET harga = '%s' WHERE id = %s" % (
                                    harga_json, id_json))
                            db1.commit()
                            # memasukkan perubahan pada status run_bank menjadi 1
                            dataJson[i]['status'] = '1'
                            if Transaksi == 'toko_kain':
                                with open('reportGarmen.json', 'w', encoding='utf-8') as report:
                                    json.dump(dataJson, report, indent=4)
                            elif Transaksi == 'garmen':
                                with open('reportToko.json', 'w', encoding='utf-8') as report:
                                    json.dump(dataJson, report, indent=4)


            if action == 'insert' and status == '0':
                print(
                    "Terjadi penambahan data pada database Server dengan id = %s, jenis_kain = %s, kwalitas_kain = %s, tekstur_kain = %s, warna_kain = %s, panjang_kain = %s, harga = %s" % (
                    id_json, jenis_kain_json, kwalitas_kain_json, tekstur_kain_json, warna_kain_json, panjang_kain_json, harga_json))

                # insert into tb_transaksi di database bank
                sql = "INSERT INTO tb_transaksi(jenis_kain, kwalitas_kain, tekstur_kain, warna_kain, panjang_kain, harga) VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % (
                    jenis_kain_json, kwalitas_kain_json, tekstur_kain_json, warna_kain_json, panjang_kain_json, harga_json)
                # print(sql)
                cur1.execute(sql)
                db1.commit()

                # insert into tb_transaksi di database bank
                sql = "INSERT INTO tb_transaksi_backup(jenis_kain, kwalitas_kain, tekstur_kain, warna_kain, panjang_kain, harga) VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % (
                    jenis_kain_json, kwalitas_kain_json, tekstur_kain_json, warna_kain_json, panjang_kain_json,
                    harga_json)
                cur1.execute(sql)
                db1.commit()
                # memasukkan perubahan pada status run_bank menjadi 1
                dataJson[i]['status'] = '1'
                if Transaksi == 'toko_kain':
                    with open('reportGarmen.json', 'w', encoding='utf-8') as report:
                        json.dump(dataJson, report, indent=4)
                elif Transaksi == 'garmen':
                    with open('reportToko.json', 'w', encoding='utf-8') as report:
                        json.dump(dataJson, report, indent=4)

            if (action == 'delete' and status == '0'):
                # print notifikasi
                print(
                    "Terjadi penghapusan data pada  Database Server dengan id = %s" % id_json)
                # delete pada tb_transaksi di database bank
                sql = "DELETE FROM tb_transaksi WHERE id = %s" % id_json
                cur1.execute(sql)
                db1.commit()
                # delete pada tb_transaksi_temp di database bank
                sql = "DELETE FROM tb_transaksi_backup WHERE id = %s" % id_json
                cur1.execute(sql)
                db1.commit()
                # memasukkan perubahan pada status run_bank menjadi 1
                dataJson[i]['status'] = '1'
                if Transaksi == 'toko_kain':
                    with open('reportGarmen.json', 'w', encoding='utf-8') as report:
                        json.dump(dataJson, report, indent=4)
                elif Transaksi == 'garmen':
                    with open('reportToko.json', 'w', encoding='utf-8') as report:
                        json.dump(dataJson, report, indent=4)
            # membuat delay
            time.sleep(delay)

            # Menutup koneksi
            # db1.close()

def main():
    lagi = True
    while lagi:

        # pengecekan pada Database Toko
        Transaksi = 'toko_kain'
        db1 = pymysql.connect("localhost","root","","toko_kain")
        db2 = pymysql.connect("localhost","root","","garmen")

        #cursor = db.cursor()
        cur1 = db1.cursor()
        cur2 = db2.cursor()

        # print function
        Cek(Transaksi, cur1, db1)

        # pengecekan pada Database Bank
        Transaksi = 'garmen'
        db2 = pymysql.connect("localhost", "root", "", "toko_kain")
        db1 = pymysql.connect("localhost", "root", "", "garmen")

        # cursor = db.cursor()
        cur1 = db1.cursor()
        cur2 = db2.cursor()

        # print function
        Cek(Transaksi, cur1, db1)

    db1.close()
    db2.close()

while True:
    main()