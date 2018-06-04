import pymysql
import json
import time

print('|---Integrasi Migrasi Sistem---|')
print('|--------------BY-------------|')
print('|   Eka Krisna   (1605552007) |')
print('|   Bayuguna     (1605552011) |')
print('|   Dode Aditya  (1605552024) |')
print('')
#koneksi
dbGarmen = pymysql.connect("localhost","root","","garmen")

curGarmen = dbGarmen.cursor()

# select semua data dari tb_transaksi pada Database Toko
curGarmen.execute("SELECT * FROM tb_transaksi;")
data = curGarmen.fetchall()

# select semua data dari tb_transaksi_backup pada Database Toko
curGarmen.execute("SELECT * FROM tb_transaksi_backup;")
dataBackup = curGarmen.fetchall()

# hitung banyak data
jumlahData = len(data)
jumlahDataBackup = len(dataBackup)

#input time sleep untuk waktu delay
delay = int(input("masukan waktu delay : "))

#function untuk insert data report dari database Garmen
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
                 'warna_kain': warna_kain, 'panjang_kain': panjang_kain, 'harga': str(harga), 'action': 'update','status': '0'}
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


try:
    while True:
        # koneksi
        dbGarmen = pymysql.connect("localhost", "root", "", "garmen")

        # cursor = db.cursor()
        curGarmen = dbGarmen.cursor()

        # select semua data dari tb_transaksi pada Database Toko
        curGarmen.execute("SELECT * FROM tb_transaksi;")
        data = curGarmen.fetchall()

        # select semua data dari tb_transaksi_backup pada Database Toko
        curGarmen.execute("SELECT * FROM tb_transaksi_backup;")
        dataBackup = curGarmen.fetchall()

        # hitung banyak data
        jumlahData = len(data)
        jumlahDataBackup = len(dataBackup)

        if jumlahData == jumlahDataBackup:
            # proses penyocokan data
            for i in range(0, jumlahData):
                if data[i][1] != dataBackup[i][1]:
                    print(
                        "Update data pada Database garmen pada data jenis_kain, data sebelumnya adalah %s diupdate menjadi %s pada id %s" % (
                            dataBackup[i][1], data[i][1], data[i][0]))

                    # proses update pada tb transaksi backup pada Database Toko
                    curGarmen.execute("UPDATE tb_transaksi_backup SET jenis_kain='%s' WHERE id=%s;" % (
                        data[i][1], dataBackup[i][0]))
                    dbGarmen.commit()

                    UpdateJsonGarmen(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4],data[i][5], data[i][6])


                # cek pembaruan atas nama
                elif data[i][2] != dataBackup[i][2]:
                    print(
                        "Update data pada Database garmen pada data kwalitas_kain, data sebelumnya adalah %s diupdate menjadi %s pada id %s" % (
                            dataBackup[i][2], data[i][2], data[i][0]))

                    # update tb transaksi backup
                    sql = "UPDATE tb_transaksi_backup SET kwalitas_kain='%s' WHERE id=%s;" % (
                        data[i][2], dataBackup[i][0])
                    curGarmen.execute(sql)
                    dbGarmen.commit()

                    UpdateJsonGarmen(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4],
                                         data[i][5], data[i][6])

                # cek pembaruan jumlah
                elif data[i][3] != dataBackup[i][3]:
                    print(
                        "Update data pada Database garmen pada data tekstur_kain, data sebelumnya adalah %s diupdate menjadi %s pada id %s" % (
                            dataBackup[i][3], data[i][3], data[i][0]))

                    # update tb transaksi backup
                    sql = "UPDATE tb_transaksi_backup SET tekstur_kain='%s' WHERE id=%s;" % (
                        data[i][3], dataBackup[i][0])
                    curGarmen.execute(sql)
                    dbGarmen.commit()

                    UpdateJsonGarmen(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4],
                                         data[i][5], data[i][6])

                # cek pembaruan kode unik
                elif data[i][4] != dataBackup[i][4]:
                    print(
                        "Update data pada Database Ggarmen pada data warna_kain, data sebelumnya adalah %s diupdate menjadi %s pada id %s" % (
                            data[i][4], data[i][4], data[i][0]))

                    # update tb transaksi backup
                    sql = "UPDATE tb_transaksi_backup SET warna_kain='%s' WHERE id=%s;" % (
                        data[i][4], dataBackup[i][0])
                    curGarmen.execute(sql)
                    dbGarmen.commit()

                    UpdateJsonGarmen(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4],
                                         data[i][5], data[i][6])

                # cek pembaruan status
                elif data[i][5] != dataBackup[i][5]:
                    print(
                        "Update data pada Database garmen pada data panjang_kain, data sebelumnya adalah %s diupdate menjadi %s pada id %s" % (
                            dataBackup[i][5], data[i][5], data[i][0]))

                    # update tb transaksi backup
                    sql = "UPDATE tb_transaksi_backup SET panjang_kain=%s WHERE id=%s;" % (
                        data[i][5], dataBackup[i][0])
                    curGarmen.execute(sql)
                    dbGarmen.commit()

                    UpdateJsonGarmen(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4],
                                         data[i][5], data[i][6])
                # cek pembaruan no rekening

                # cek pembaruan tanggal
                elif data[i][6] != dataBackup[i][6]:
                    print(
                        "Update data pada Database garmen pada data harga, data sebelumnya adalah %s diupdate menjadi %s pada id %s" % (
                            dataBackup[i][6], data[i][6], data[i][0]))

                    # update tb transaksi backup
                    sql = "UPDATE tb_transaksi_backup SET harga=%s WHERE id=%s;" % (
                        data[i][6], dataBackup[i][0])
                    curGarmen.execute(sql)
                    dbGarmen.commit()

                    UpdateJsonGarmen(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4],
                                         data[i][5], data[i][6])

                else:
                    print("Checking Garmen")

        # proses pengecekan jika terjadi insert data baru di tabel
        elif jumlahData > jumlahDataBackup:

            # proses insert data baru
            insertMin = jumlahDataBackup
            beforeMaxInsert = jumlahData

            for i in range(insertMin, beforeMaxInsert):
                # pemberitahuan
                print(
                    "Insert data pada Database Garmen dengan index %s ,data yang di-insert adalah jenis_kain =%s, kwalitas_kain = %s, tekstur_kain = %s, warna_kain = %s, panjang_kain = %s , harga = %s" % (
                        data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5],
                        data[i][6]))

                # insert into tb_transaksi_backup
                sql = "INSERT INTO tb_transaksi_backup(jenis_kain, kwalitas_kain, tekstur_kain, warna_kain, panjang_kain, harga) " \
                      "VALUES('%s','%s','%s','%s','%s','%s');" % (
                          data[i][1], data[i][2], data[i][3], data[i][4], data[i][5], data[i][6])
                curGarmen.execute(sql)
                dbGarmen.commit()

                InsertJsonGarmen(data[i][0], data[i][1], data[i][2], data[i][3], data[i][4], data[i][5],
                                data[i][6])

            # proses ketika terjadi delete di tabel toko
        elif jumlahData < jumlahDataBackup:

            # proses delete yang terjadi jika id yang di delete pada tabel toko adalah id terakhir
            for i in range(0, jumlahDataBackup):

                curGarmen.execute("SELECT * FROM tb_transaksi WHERE tb_transaksi.`id`=%s;" % dataBackup[i][0])

                if curGarmen.rowcount == 0:
                    print(
                        "Delete data pada Database garmen dengan index %s,data yang di-delete adalah jenis_kain =%s, kwalitas_kain = %s, tekstur_kain = %s, kode unik = %s, panjang_kain = %s , harga = %s" % (
                            dataBackup[i][0], dataBackup[i][1], dataBackup[i][2], dataBackup[i][3],
                            dataBackup[i][4], dataBackup[i][5],
                            dataBackup[i][6]))

                    # delete di tabel transaksi database 1
                    sql = "DELETE FROM tb_transaksi_backup WHERE id=%s;" % dataBackup[i][0]
                    curGarmen.execute(sql)
                    dbGarmen.commit()

                    DeleteJsonGarmen(dataBackup[i][0], dataBackup[i][1], dataBackup[i][2], dataBackup[i][3],
                                         dataBackup[i][4],
                                         dataBackup[i][5], dataBackup[i][6])

                    # temp = i
                    # pemberitahuan
                    print(
                        "Delete data pada Database garmen dengan index %s,data yang di-delete adalah jenis_kain =%s, kwalitas_kain = %s, tekstur_kain = %s, kode unik = %s, panjang_kain = %s , harga = %s" % (
                            dataBackup[i][0], dataBackup[i][1], dataBackup[i][2], dataBackup[i][3],
                            dataBackup[i][4], dataBackup[i][5], dataBackup[i][6]))

            else:
                print("Checking Eror")

        else:
            print("Checking Garmen")

        # Cek Pembahruan dalam JSON file database bank
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
                harga_json = int(dataJson[i]['harga'])

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
                                curGarmen.execute(
                                    "UPDATE tb_transaksi SET jenis_kain = '%s' WHERE id = %s" % (
                                        jenis_kain_json, id_json))
                                dbGarmen.commit()

                                # update pada tabel tb_transaksi_temp di database
                                curGarmen.execute(
                                    "UPDATE tb_transaksi_backup SET jenis_kain = '%s' WHERE id = %s" % (
                                        jenis_kain_json, id_json))
                                dbGarmen.commit()

                                # memasukkan perubahan pada status run_bank menjadi 1
                                dataJson[i]['status'] = '1'

                                with open('reportToko.json', 'w', encoding='utf-8') as report:
                                    json.dump(dataJson, report, indent=4)

                            if kwalitas_kain_json != dataBackup[a][2]:
                                # pemberitahuan
                                print(
                                    "Terjadi perubahan pada Json, data sebelumnya %s berubah menjadi %s pada id %s" % (
                                        dataBackup[a][2], kwalitas_kain_json, id_json))

                                # update pada tb_transaksi di database bank
                                curGarmen.execute(
                                    "UPDATE tb_transaksi SET kwalitas_kain = '%s' WHERE id = %s" % (
                                        kwalitas_kain_json, id_json))
                                dbGarmen.commit()

                                # update pada tabel tb_transaksi_temp di database bank
                                curGarmen.execute(
                                    "UPDATE tb_transaksi_backup SET kwalitas_kain = '%s' WHERE id = %s" % (
                                        kwalitas_kain_json, id_json))
                                dbGarmen.commit()
                                # memasukkan perubahan pada status run_bank menjadi 1
                                dataJson[i]['status'] = '1'

                                with open('reportToko.json', 'w', encoding='utf-8') as report:
                                    json.dump(dataJson, report, indent=4)

                            if tekstur_kain_json != dataBackup[a][3]:
                                # print notifikasi
                                print(
                                    "Terjadi perubahan pada Json, data sebelumnya %s berubah menjadi %s pada id %s" % (
                                        dataBackup[a][3], tekstur_kain_json, id_json))
                                # update pada tb_transaksi di database bank
                                curGarmen.execute(
                                    "UPDATE tb_transaksi SET tekstur_kain = '%s' WHERE id = %s" % (
                                        tekstur_kain_json, id_json))
                                dbGarmen.commit()
                                # update pada tb_transaksi_temp di database bank
                                curGarmen.execute(
                                    "UPDATE tb_transaksi_backup SET tekstur_kain = '%s' WHERE id = %s" % (
                                        tekstur_kain_json, id_json))
                                dbGarmen.commit()
                                # memasukkan perubahan pada status run_bank menjadi 1
                                dataJson[i]['status'] = '1'

                                with open('reportToko.json', 'w', encoding='utf-8') as report:
                                    json.dump(dataJson, report, indent=4)

                            if warna_kain_json != dataBackup[a][4]:
                                # print notifikasi
                                print(
                                    "Terjadi perubahan pada Json, data sebelumnya %s berubah menjadi %s pada id %s" % (
                                        dataBackup[a][4], warna_kain_json, id_json))
                                # update pada tb_transaksi di database bank
                                curGarmen.execute(
                                    "UPDATE tb_transaksi SET warna_kain = '%s' WHERE id = %s" % (
                                        warna_kain_json, id_json))
                                dbGarmen.commit()
                                # update pada tb_transaksi_temp di database bank
                                curGarmen.execute(
                                    "UPDATE tb_transaksi_backup SET warna_kain = '%s' WHERE id = %s" % (
                                        warna_kain_json, id_json))
                                dbGarmen.commit()
                                # memasukkan perubahan pada status run_bank menjadi 1
                                dataJson[i]['status'] = '1'

                                with open('reportToko.json', 'w', encoding='utf-8') as report:
                                    json.dump(dataJson, report, indent=4)

                            if panjang_kain_json != dataBackup[a][5]:
                                # print notifikasi
                                print(
                                    "Terjadi perubahan pada Server, data sebelumnya %s berubah menjadi %s pada id %s" % (
                                        dataBackup[a][5], panjang_kain_json, id_json))
                                # update pada tb_transaksi di database bank
                                sql = "UPDATE tb_transaksi SET panjang_kain='%s' WHERE id=%s;" % (
                                    panjang_kain_json, id_json)
                                curGarmen.execute(sql)
                                dbGarmen.commit()
                                # update pada tb_transaksi_temp di database bank
                                curGarmen.execute(
                                    "UPDATE tb_transaksi_backup SET panjang_kain = '%s' WHERE id = %s" % (
                                        panjang_kain_json, id_json))
                                dbGarmen.commit()
                                # memasukkan perubahan pada status run_bank menjadi 1
                                dataJson[i]['panjang_kain'] = '1'

                                with open('reportToko.json', 'w', encoding='utf-8') as report:
                                    json.dump(dataJson, report, indent=4)

                            if (harga_json != dataBackup[a][6]):
                                # print notifikasi
                                print(
                                    "Terjadi perubahan pada Server, data sebelumnya %s berubah menjadi %s pada id %s" % (
                                        dataBackup[a][6], harga_json, id_json))
                                # update pada tb_transaksi di database bank
                                curGarmen.execute(
                                    "UPDATE tb_transaksi SET harga = '%s' WHERE id = %s" % (
                                        harga_json, id_json))
                                dbGarmen.commit()
                                # update pada tb_transaksi_temp di database bank
                                curGarmen.execute(
                                    "UPDATE tb_transaksi_backup SET harga = '%s' WHERE id = %s" % (
                                        harga_json, id_json))
                                dbGarmen.commit()
                                # memasukkan perubahan pada status run_bank menjadi 1
                                dataJson[i]['status'] = '1'

                                with open('reportToko.json', 'w', encoding='utf-8') as report:
                                    json.dump(dataJson, report, indent=4)

                if action == 'insert' and status == '0':
                    print(
                        "Terjadi penambahan data pada database Server dengan id = %s, jenis_kain = %s, kwalitas_kain = %s, tekstur_kain = %s, warna_kain = %s, panjang_kain = %s, harga = %s" % (
                            id_json, jenis_kain_json, kwalitas_kain_json, tekstur_kain_json, warna_kain_json,
                            panjang_kain_json, harga_json))

                    # insert into tb_transaksi di database bank
                    sql = "INSERT INTO tb_transaksi(jenis_kain, kwalitas_kain, tekstur_kain, warna_kain, panjang_kain, harga) VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % (
                        jenis_kain_json, kwalitas_kain_json, tekstur_kain_json, warna_kain_json, panjang_kain_json,
                        harga_json)
                    # print(sql)
                    curGarmen.execute(sql)
                    dbGarmen.commit()

                    # insert into tb_transaksi di database bank
                    sql = "INSERT INTO tb_transaksi_backup(jenis_kain, kwalitas_kain, tekstur_kain, warna_kain, panjang_kain, harga) VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % (
                        jenis_kain_json, kwalitas_kain_json, tekstur_kain_json, warna_kain_json, panjang_kain_json,
                        harga_json)
                    curGarmen.execute(sql)
                    dbGarmen.commit()
                    # memasukkan perubahan pada status run_bank menjadi 1
                    dataJson[i]['status'] = '1'

                    with open('reportToko.json', 'w', encoding='utf-8') as report:
                        json.dump(dataJson, report, indent=4)

                if (action == 'delete' and status == '0'):
                    # print notifikasi
                    print(
                        "Terjadi penghapusan data pada  Database Server dengan id = %s" % id_json)
                    # delete pada tb_transaksi di database bank
                    sql = "DELETE FROM tb_transaksi WHERE id = %s" % id_json
                    curGarmen.execute(sql)
                    dbGarmen.commit()
                    # delete pada tb_transaksi_temp di database bank
                    sql = "DELETE FROM tb_transaksi_backup WHERE id = %s" % id_json
                    curGarmen.execute(sql)
                    dbGarmen.commit()
                    # memasukkan perubahan pada status run_bank menjadi 1
                    dataJson[i]['status'] = '1'

                    with open('reportToko.json', 'w', encoding='utf-8') as report:
                        json.dump(dataJson, report, indent=4)

                # membuat delay
                time.sleep(delay)

                # Menutup koneksi
                # db1.close()
except:
    ("Checking Error")
