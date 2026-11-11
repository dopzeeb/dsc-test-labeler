# DSC Gelar Rasa 2026 — Test Set Ground-Truth Labeler & Local Submission Evaluator

Tool mandiri berbasis web (`index.html`) + script CLI (`evaluate_submission.py`) untuk melabeli **480 citra `test/`** (`001.jpg`–`480.jpg`) secara cepat pada **keyboard tanpa Numpad (TKL / 60% / Laptop)**, sekaligus mengecek skor akurasi `submission.csv` secara lokal sebelum di-submit ke Kaggle.

## Shortcut Keyboard Ergonomis (Tangan Kiri 2x4: `Q W E R` + `A S D F`)

| Baris Keyboard | Tombol | Kategori Sampah | Alternatif Angka |
|---|---|---|---|
| **Baris Atas** | **`Q`** | `cardboard` | `1` |
| **Baris Atas** | **`W`** | `electronic` | `2` |
| **Baris Atas** | **`E`** | `foodwaste` | `3` |
| **Baris Atas** | **`R`** | `glass` | `4` |
| **Baris Tengah (Home Row)** | **`A`** | `metal` | `5` |
| **Baris Tengah (Home Row)** | **`S`** | `paper` | `6` |
| **Baris Tengah (Home Row)** | **`D`** | `plastic` | `7` |
| **Baris Tengah (Home Row)** | **`F`** | `textile` | `8` |

### Navigasi & Kontrol Cepat
- **`Space` / `Panah Kanan` / `L`**: Gambar berikutnya
- **`Panah Kiri` / `Backspace` / `Z` / `J`**: Gambar sebelumnya (koreksi cepat)
- **`X`**: Tandai gambar sebagai **Ragu-ragu** (dihitung terpisah saat evaluasi akurasi)
- **`Delete`**: Hapus label gambar saat ini

## Cara Pakai
1. Buka `index.html` di browser (atau melalui GitHub Pages).
2. Labeli gambar menggunakan tombol **`Q W E R`** dan **`A S D F`** (tersimpan otomatis di `localStorage` browser).
3. Klik **Download `test_ground_truth.csv`** untuk menyimpan file kunci jawaban ke folder ini.
4. Untuk mengecek skor `submission.csv`:
   - **Lewat Browser**: Klik **"Upload / Pilih File `submission.csv` untuk Cek Akurasi"** di panel kanan `index.html` (Anda juga bisa memfilter hanya gambar yang prediksinya berbeda dengan Ground Truth!).
   - **Lewat Terminal Python**:
     ```bash
     python evaluate_submission.py path/ke/submission.csv
     ```
