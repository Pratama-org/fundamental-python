"""
Tipe data dictionary sekedar menghubungkan KEY & Value
KVP = Key Value Pair
dictionary = kamus
"""

# Digunakan untuk microservices

kamus_ind_eng = {'anak': 'son', 'istri': 'wife', 'ayah': 'Father', 'ibu': 'Ibu'}

print(kamus_ind_eng)
print(kamus_ind_eng['ayah'])
print(kamus_ind_eng['ibu'])

print('Data ini dikirimkan oleh server Gojek utk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {
    'tanggal': '2020-06-10',
    'driver_list': [
        {'nama': 'Eko', 'jarak': 10},
        {'nama': 'Dwi', 'jarak': 30},
        {'nama': 'Trie', 'jarak': 100},
        {'Catur', 'jarak' : 1000}
    ]
}

print(data_dari_server_gojek)
print(f"Driver disekitar sini {data_dari_server_gojek['driver-list']}")
print(f"Driver #1 {data_dari_server_gojek['driver-list'][0]}")
print(f"Driver #4 {data_dari_server_gojek['driver-list'][3]}")
print(f"Driver terdekat berjarak #1{data_dari_server_gojek}['driver_list'][0]['jarak']}} meter ")





# Tipe data string di python hrs di beri petik yg konsisten 1/2.















