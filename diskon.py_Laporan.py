# ================================
# KALKULATOR DISKON - CLEAN CODE (PYTHON)
# ================================

BATAS_HARGA_MURAH = 50000

def hitung_harga_setelah_diskon(harga_awal: float, persen_diskon: float) -> float:
    """Menghitung harga akhir setelah dipotong diskon"""
    potongan = harga_awal * (persen_diskon / 100)
    return harga_awal - potongan

def tentukan_status_harga(harga_akhir: float) -> str:
    """Menentukan apakah harga termasuk murah atau mahal"""
    return "Murah" if harga_akhir < BATAS_HARGA_MURAH else "Mahal"

def tampilkan_hasil(harga_awal: float, persen_diskon: float) -> None:
    """Menampilkan hasil perhitungan diskon ke console"""
    harga_akhir = hitung_harga_setelah_diskon(harga_awal, persen_diskon)
    status = tentukan_status_harga(harga_akhir)
    
    print(f"Harga awal: Rp{harga_awal}")
    print(f"Diskon: {persen_diskon}%")
    print(f"Harga akhir: Rp{harga_akhir}")
    print(f"Status: {status}")
    print("-" * 24)

# Data transaksi
transaksi_list = [
    {"harga_awal": 100000, "diskon": 20},
    {"harga_awal": 200000, "diskon": 30}
]

for transaksi in transaksi_list:
    tampilkan_hasil(transaksi["harga_awal"], transaksi["diskon"])
