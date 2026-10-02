# IB_irfan_erza — Tugas Kelompok Berbasis Kasus 01

## Kasus: Robot Kurir Kampus GU → LK

Robot kurir kampus mencari rute dari **GU (Gerbang Utama)** ke **LK (Lab Komputasi)**.

Tentukan rute **GU → LK** menggunakan:
1. **UCS** (Uniform Cost Search)
2. **IDS** (Iterative Deepening Search)
3. **GBFS** (Greedy Best-First Search)
4. **A\*** (A-Star)

Gunakan bobot pada graf untuk **IDS**, naikkan batas kedalaman secara bertahap.

Diskusikan perbedaan **urutan ekspansi, rute, dan total cost** yang dihasilkan oleh UCS, IDS, GBFS, dan A*.

---

## 1. Graf Kampus

Simpul:

| Kode | Nama |
|------|------|
| GU | Gerbang Utama |
| PB | Parkir Barat |
| R | Rektorat |
| GKU | Gedung Kuliah Umum |
| PR | Perpustakaan |
| K | Kantin |
| M | Masjid |
| A | Aula |
| AS | Asrama |
| IF | Teknik Informatika |
| SC | Sport Center |
| LK | Lab Komputasi |

### Daftar sisi (hasil pembacaan graf — perlu verifikasi ulang dari gambar slide 33)

> Catatan: angka pada gambar agak kecil. Jika ada yang beda saat coding, update tabel ini.

| Dari | Ke | Bobot |
|------|----|-------|
| GU | PB | 3 |
| GU | R | 4 |
| PB | GKU | 4 |
| PB | K | 6 |
| R | PR | 3 |
| GKU | PR | 2 |
| GKU | A | 7 |
| PR | A | 6 |
| PR | IF | 4 |
| R | K | 5 (?) |
| K | M | 5 |
| K | AS | 5 |
| A | M | 3 |
| A | LK | 5 |
| M | IF | 4 |
| IF | LK | 3 |
| IF | SC | 6 (?) |
| AS | IF | 6 (?) |
| AS | SC | 6 |
| SC | LK | 4 |

Start: `GU`
Goal: `LK`

---

## 2. Nilai Heuristik h(n)

Perkiraan jarak dari setiap simpul ke LK:

| Simpul | h(n) | Simpul | h(n) | Simpul | h(n) | Simpul | h(n) |
|--------|------|--------|------|--------|------|--------|------|
| GU | 12 | PB | 10 | R | 9 | GKU | 7 |
| PR | 6 | K | 9 | M | 7 | A | 4 |
| AS | 5 | IF | 2 | SC | 3 | LK | 0 |

Dipakai untuk GBFS dan A*.

---

## 3. Yang Harus Dibuat

### Program sederhana (bahasa bebas)

Untuk tiap metode tampilkan:
- urutan ekspansi simpul
- rute GU → LK yang ditemukan
- total cost (jumlah bobot sisi) rute tersebut

Khusus IDS:
- pakai bobot graf sebagai cost
- naikkan depth limit bertahap (0, 1, 2, ... sampai ketemu LK)
- tampilkan hasil per iterasi

### Analisis perbandingan

- beda urutan ekspansi UCS vs IDS vs GBFS vs A*
- beda rute dan total cost
- mana yang optimal / tidak optimal, kenapa
- pengaruh h(n) pada GBFS dan A*

---

Mata kuliah: **Inteligensi Buatan — 2026**
