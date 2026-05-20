# AniRank - Website Daftar Anime

## Informasi Kelompok
- **Mata Kuliah**: Pemrograman Back-End  
- **Tugas**: KELOMPOK 8
- **Institusi**: Institut Teknologi Tangerang Selatan  

## Tema Website
Website database anime seperti IMDb, menampilkan daftar anime populer, anime yang sedang tayang, pencarian, dan detail lengkap tiap anime.

## API yang Digunakan
**Jikan API v4** — https://api.jikan.moe/v4  
API publik tidak resmi dari MyAnimeList (MAL), gratis dan tanpa API key.

## Fitur Utama
| Halaman | URL | Fitur |
|---------|-----|-------|
| Beranda | `/` | Top 12 anime + anime sedang tayang |
| Pencarian | `/search?q=naruto` | Cari berdasarkan judul |
| Filter Genre | `/genre/1` | Filter anime per genre |
| Detail Anime | `/anime/20` | Info lengkap + karakter |

## Teknologi
- **Backend**: Python + Flask
- **Frontend**: HTML, CSS (custom), JavaScript
- **HTTP Client**: `requests`
- **API**: Jikan API v4 (Public API)

## Cara Menjalankan

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Jalankan aplikasi
python app.py

# 3. Buka browser
# http://localhost:5000
```

## Struktur Folder
```
anime-website/
├── app.py                  # Flask routes & logika utama
├── requirements.txt        # Dependencies Python
├── README.md               # Dokumentasi ini
├── static/
│   ├── css/style.css       # Stylesheet utama
│   └── js/main.js          # JavaScript
└── templates/
    ├── base.html           # Layout dasar (navbar + footer)
    ├── index.html          # Halaman beranda
    ├── search.html         # Halaman hasil pencarian
    ├── detail.html         # Halaman detail anime
    └── genre.html          # Halaman filter genre
```

## Screenshot
![Alt Text](img/screenshot_website.png)

## Catatan
- API Jikan memiliki rate limit ~3 request/detik, jika halaman gagal dimuat tunggu beberapa detik lalu refresh.
- Pastikan koneksi internet aktif karena data diambil langsung dari API.
