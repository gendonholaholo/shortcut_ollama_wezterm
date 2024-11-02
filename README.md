**Shourtcut Ollama Wezterm**
=========================

Sebuah aplikasi tray untuk menjalankan WezTerm dengan fitur-fitur tambahan.

**Perlu Diinstal:**

- Python 3.x
- PyStray
- PIL (Pillow)
- Keyboard
- WezTerm
- Pyinstaller

**Langkah-langkah Instalasi:**

1. Clone repository ini menggunakan command `git clone https://github.com/[Nama
Anda]/ollama-run-tray.git`
2. Buka folder yang telah dihasilkan dan jalankan command `pip install -r requirements.txt`
untuk menginstal semua perlu diinstal.
3. Jalankan command `pyinstaller --onefile --nonconsole app.py` untuk menjalankan aplikasi tray.
4. Buka direktori `dist` dan jalankan `app.exe`

**Fitur:**

- Aplikasi tray dengan ikon yang dapat diubah
- Fitur "Exit" untuk keluar dari aplikasi
- Hotkey Alt + F1 untuk membuka WezTerm
- Aplikasi dapat dijalankan secara background

**Konfigurasi:**

- Ikona aplikasi dapat diubah di `icon_path` pada baris 12.
- Fitur hotkey dapat diubah di `setup_hotkeys` pada baris 19.

**Pembuatan Code:**

- Aplikasi ini dibuat menggunakan Python 3.x
- PyStray digunakan untuk membuat ikon aplikasi tray
- PIL (Pillow) digunakan untuk mengubah ikon aplikasi tray
- Keyboard digunakan untuk membuat hotkey
- WezTerm digunakan sebagai aplikasi yang akan dijalankan

**Pencarian Bug:**

- Jika Anda menemukan bug, silakan membuat issue baru di GitHub dan menjelaskan bagaimana Anda
menemukannya.
- Pastikan Anda untuk memberikan contoh kode yang dapat dibuat di reproduksi bug tersebut
