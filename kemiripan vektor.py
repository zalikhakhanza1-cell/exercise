import numpy as np
from itertools import permutations

indo_words = {
    'senang': np.array([21, 10]),
    'pria': np.array([6, 29]),
    'wanita': np.array([30, 24]),
    'ayah': np.array([11, 26]),
    'ibu': np.array([36, 19]),
    'raja': np.array([8, 36]),
    'ratu': np.array([32, 29]),
    'sedih': np.array([18, 19]),
    'menang': np.array([26, 8]),
    'kalah': np.array([23, 16])
}

alien_words = {
    'Gohok': np.array([34, 37]),
    'Subi': np.array([28, 29]),
    'Matot': np.array([14, 35]),
    'Befar': np.array([38, 31]),
    'Dursit': np.array([38, 40]),
    'Gien': np.array([29, 19]),
    'Ibakuz': np.array([24, 20]),
    'Gelon': np.array([11, 46]),
    'Wazuke': np.array([10, 42]),
    'Nusgen': np.array([22, 30])
}

print(" Vektor Translasi Bahasa Indonesia ")
# Hubungan Maskulin -> Feminin
vec_wanita_pria = indo_words['wanita'] - indo_words['pria']
vec_ratu_raja = indo_words['ratu'] - indo_words['raja']
vec_ibu_ayah = indo_words['ibu'] - indo_words['ayah']
print(f"wanita - pria = {vec_wanita_pria}")
print(f"ratu - raja   = {vec_ratu_raja}")
print(f"ibu - ayah    = {vec_ibu_ayah}")

# Hubungan Antonim
vec_sedih_senang = indo_words['sedih'] - indo_words['senang']
vec_kalah_menang = indo_words['kalah'] - indo_words['menang']
print(f"sedih - senang = {vec_sedih_senang}")
print(f"kalah - menang = {vec_kalah_menang}")
print("-" * 20)
# Langkah 2: Cari pasangan di Bahasa Alien dengan vektor translasi serupa
solution = {}
alien_names = list(alien_words.keys())
indo_names = list(indo_words.keys())

# Cari semua kemungkinan pasangan dan vektor translasinya
alien_diffs = {}
for w1, w2 in permutations(alien_names, 2):
    alien_diffs[(w1, w2)] = alien_words[w1] - alien_words[w2]

solution['Gohok'] = 'wanita'
solution['Wazuke'] = 'pria'

# Pasangan M/F lainnya: (Befar, Matot) -> (24,-4) dan (Dursit, Gelon) -> (27,-6)
# harus cocok dengan (ratu, raja) dan (ibu, ayah)
# Kita gunakan jarak relatif dari 'pria' untuk menentukan
pria_ayah_dist = np.linalg.norm(indo_words['pria'] - indo_words['ayah'])
pria_raja_dist = np.linalg.norm(indo_words['pria'] - indo_words['raja'])

wazuke_gelon_dist = np.linalg.norm(alien_words['Wazuke'] - alien_words['Gelon'])
wazuke_matot_dist = np.linalg.norm(alien_words['Wazuke'] - alien_words['Matot'])

# Mencocokkan pola jarak:
# Jarak (Wazuke, Gelon) lebih dekat ke (pria, ayah)
# Jarak (Wazuke, Matot) lebih dekat ke (pria, raja)
if abs(pria_ayah_dist - wazuke_gelon_dist) < abs(pria_ayah_dist - wazuke_matot_dist):
    solution['Gelon'] = 'ayah'
    solution['Matot'] = 'raja'
else:
    solution['Gelon'] = 'raja'
    solution['Matot'] = 'ayah'

# Tentukan pasangannya
solution['Dursit'] = 'ibu' # Pasangan dari Gelon (ayah)
solution['Befar'] = 'ratu' # Pasangan dari Matot (raja)

# Langkah 3: Selesaikan pasangan antonim 
remaining_alien = [w for w in alien_names if w not in solution]
# Sisa kata alien: ['Subi', 'Gien', 'Ibakuz', 'Nusgen']
# Sisa kata Indo: ['senang', 'sedih', 'menang', 'kalah']

# Vektor translasi antonim di bahasa alien
# Nusgen - Ibakuz = (-2, 10) -> mirip (sedih - senang) = (-3, 9)
# Subi - Gien = (-1, 10) -> mirip (kalah - menang) = (-3, 8)
# Ini menyiratkan pasangan (Nusgen, Ibakuz) dan (Subi, Gien)

# Gunakan struktur internal untuk memvalidasi
# Vektor dari kata 'positif' pertama ke kedua
vec_menang_senang = indo_words['menang'] - indo_words['senang'] # (5, -2)
# Kandidat di alien
vec_gien_ibakuz = alien_words['Gien'] - alien_words['Ibakuz'] # (5, -1)

# Karena (Gien - Ibakuz) sangat mirip dengan (menang - senang), kita bisa simpulkan:
solution['Ibakuz'] = 'senang'
solution['Gien'] = 'menang'

# Tentukan pasangannya
solution['Nusgen'] = 'sedih' # Pasangan dari Ibakuz (senang)
solution['Subi'] = 'kalah' # Pasangan dari Gien (menang)


# Final: Tampilkan hasil 
print("\n Hasil Perjodohan Kata")
# Urutkan berdasarkan urutan soal
for alien_word in ['Gohok', 'Subi', 'Matot', 'Befar', 'Dursit', 'Gien', 'Ibakuz', 'Gelon', 'Wazuke', 'Nusgen']:
    indo_word = solution[alien_word]
    print(f"{alien_word:<8} = {indo_word}")