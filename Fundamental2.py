# Tipe data skalar => Tipe data sederhana
# Jam terbang yang menentukan

anak1 = 'Adjie'
anak2 = 'Dwi'
anak3 = 'Trie'
anak4 = 'Catur'

print(anak1)
print(anak2)
print(anak2)
print(anak3)
print(anak4)

# Tipe data list / daftar /array

print('\ntipe data lis/daftar/array')
anak = ['Adjie', 'Dwi', 'Trie', 'Catur']
print(anak)
anak.append('Limo')
print(anak)

# Sapa anak ke -2

print('\nsapa anak ke-2')
print(f'Hai {anak[1]}!')

# Sapa semua anak

print('\nsapa semua anak')
for a in anak:
    print(f'Hai {a}!')

print('\nSapa semua anak : cara ribet')
for a in range(0, len(anak)):
    print(f'{a+1}.Hai {anak[a]}')
