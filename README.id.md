# CV Creator

[English](README.md) · **Bahasa Indonesia**

Pembuat CV berbasis AI yang dibangun dari **aturan Markdown**, bukan kode program. Kamu menyimpan data sendiri di folder; AI membaca aturan lalu menulis CV yang **disesuaikan dengan setiap deskripsi lowongan**, dan tetap jujur.

Bisa dipakai dengan agen AI apa pun yang membaca `AGENTS.md` (Claude Code, Codex, Cursor, Copilot, dan lainnya).

> Semua aturan dan workflow di repo ini ditulis dalam bahasa Inggris supaya bisa dipakai siapa saja. Kamu tetap bisa berbicara dengan AI dalam bahasa Indonesia. AI membalas dalam bahasa yang kamu pakai di chat, dan menulis CV dalam bahasa deskripsi lowongan (lowongan berbahasa Indonesia menghasilkan CV berbahasa Indonesia).

## Cara kerja

```
profile/                info/                   jobs/<lowongan>.md
siapa kamu              bukti kamu              yang diminta perusahaan
     │                       │                       │
     └───────────────────────┼───────────────────────┘
                             ▼
                    rules/ + workflows/
                             │
                             ▼
          output/<tanggal>_<perusahaan>_<posisi>/
            ├─ cv.md              CV yang disesuaikan
            └─ match-report.md    kecocokan, kekurangan, saran
```

## Mulai cepat

1. **Clone** repo ini.
2. **Isi datamu** (pribadi, tidak ikut git). **Cara paling mudah: ceritakan saja kepada AI-mu.** Ceritakan proyek, kisah, dan skill-mu dengan kata-katamu sendiri, dalam bahasa apa pun dan urutan apa pun. AI mengajukan beberapa pertanyaan lanjutan yang singkat, lalu menuliskan entrinya untukmu memakai template (`workflows/interview.md`). Misalnya:

   > Saya mau bercerita tentang proyek, kisah, dan skill saya. Tolong wawancarai saya dan tulis entrinya ke repo ini.

   Tidak ada yang disimpan sebelum kamu mengonfirmasi, dan apa pun yang tidak kamu sebut ditandai `[TODO]`, tidak pernah ditebak. Lebih suka menulis file sendiri? Salin template-nya:
   - `profile/`: salin tiap `*.template.md` menjadi file asli (`personal.md`, `education.md`, `experience.md`).
   - `info/CERTIFICATE`, `info/SKILL`, `info/PROJECT`, `info/RESEARCH`: masukkan file-mu, lalu minta AI mengubahnya menjadi entri (`workflows/add-entry.md`).
   - `info/PROJECT/<nama>.md`: satu file per proyek (salin `project.template.md`). Ceritakan tiap proyek dengan urutan: **judul → masalah → jalan keluar → bagianmu → stack → hasil**. Misalnya: judul *Sales Dashboard*; masalah "para manajer koperasi menebak produk mana yang laku"; jalan keluar "dashboard pendapatan per kategori dan bulan dari data penjualan yang sudah dibersihkan"; bagianmu "sendirian: membersihkan data, menulis query, membangun dan men-deploy-nya". Lihat [`info/PROJECT/README.md`](info/PROJECT/README.md).
   - `profile/story.md`: **cerita dan kepribadianmu** (salin `story.template.md`). Tulis apa yang menarik minatmu, cara kerjamu, dan apa yang kamu inginkan berikutnya, seperti bercerita kepada teman. Setiap sifat butuh satu contoh nyata; sifat tanpa contoh tidak dipakai. Misalnya:

     ```
     Saya adalah tipe orang yang penasaran ketika ada yang tidak cocok, dan saya sangat suka
     menyelesaikan masalah karena setiap masalah itu seperti teka-teki kecil.
     Misalnya, proyek dashboard saya sudah dinilai, tetapi totalnya masih belum cocok dengan
     catatan kertas. Saya terus mencari data ganda sampai cocok, lalu mengirim angka yang
     sudah benar ke para manajer. Mereka memakainya di rapat bulanan.
     (bukti: info/PROJECT/sales-dashboard.md)
     ```

     AI mengubahnya menjadi **alasan dan arah** di ringkasan CV-mu, tidak pernah menjadi kata kosong seperti "pekerja keras". Lihat contoh lengkap (fiktif) di [`examples/sample-user/profile/story.md`](examples/sample-user/profile/story.md).
   - Kamu boleh menulis `story.md` dalam bahasa Indonesia. AI akan menerjemahkan isinya ke bahasa CV.
3. **Tambah lowongan**: tempel deskripsi lowongan **lengkap** **ke chat dengan AI-mu** (AI menyimpannya ke `jobs/<perusahaan>_<posisi>.md` untukmu) **atau langsung ke file itu sendiri** (pakai `jobs/job.template.md`). Link atau judul lowongan saja tidak cukup: AI hanya bisa menyesuaikan CV dengan teks yang bisa ia baca. Untuk program atau beasiswa, sertakan juga baris batas waktu dan syarat kelayakan.
4. **Minta agen AI-mu**, misalnya:
   > Buatkan CV untuk `jobs/acme_data-analyst.md` memakai `workflows/generate-cv.md`.
5. Periksa `output/…/cv.md` dan `match-report.md`. Jawab pertanyaan `[TODO]` yang muncul.
6. Ekspor ke PDF: `pip install reportlab`, lalu `python tools/md2pdf.py output/<folder>/cv.md` (lihat [`tools/README.md`](tools/README.md)).

Mau lihat hasilnya dulu? Buka [`examples/sample-user/`](examples/sample-user/): data fiktif, satu lowongan, CV yang dihasilkan, PDF-nya, dan laporan kecocokan.

Kalau sudah punya CV lama, AI bisa mengubahnya jadi entri dan menandai bagian yang bertentangan dengan datamu: lihat [`workflows/import-existing-cv.md`](workflows/import-existing-cv.md).

## Yang dijaga oleh aturan

| Aturan | Jaminan |
|---|---|
| [01 Truthfulness](rules/01-truthfulness.md) (kejujuran) | Tidak ada fakta, angka, atau skill karangan. Kekurangan ditandai, tidak disembunyikan. Status publikasi dan tesis ditulis apa adanya. |
| [02 Job tailoring](rules/02-job-tailoring.md) (menyesuaikan lowongan) | AI menganalisis deskripsi lowongan, mencocokkannya dengan buktimu, lalu menyesuaikan ringkasan, skill, urutan, dan pilihan kata. |
| [03 Writing style](rules/03-writing-style.md) (gaya tulisan) | Bullet kuat dan spesifik; tanpa kata klise; bahasa dan panjang konsisten. Ringkasan ditulis dari lowongan, bukan dari cerita umum. |
| [04 ATS formatting](rules/04-ats-formatting.md) (format ATS) | Satu kolom, heading standar, tata letak seragam, mudah dibaca mesin. |
| [05 Privacy](rules/05-privacy.md) (privasi) | Data pribadi tidak pernah di-commit. Data sensitif (misalnya NIK, agama, status pernikahan) tidak dimasukkan ke CV secara default. |

## Struktur repo

```
AGENTS.md          pintu masuk agen AI (CLAUDE.md menunjuk ke sini)
rules/             aturan wajib untuk AI
workflows/         prosedur langkah demi langkah
templates/         tata letak CV dan laporan kecocokan
tools/             skrip bantu (md2pdf.py)
examples/          contoh fiktif: pengguna, lowongan, CV, dan PDF
profile/           identitas KAMU (pribadi)
info/              bukti KAMU: CERTIFICATE, SKILL, PROJECT, RESEARCH (pribadi)
jobs/              deskripsi lowongan (pribadi)
output/            CV dan laporan hasil (pribadi)
```

## Privasi

`profile/`, `info/`, `jobs/`, dan `output/` tidak ikut git (`.gitignore`); hanya README dan `*.template.md` yang dilacak. Sebelum mem-push fork, jalankan `git status` dan pastikan tidak ada file pribadimu yang ter-stage. Jangan pernah memakai `git add -f` pada folder-folder itu, karena akan melewati perlindungan `.gitignore` dan mengunggah data pribadimu.

## Berkontribusi

Perbaikan aturan, workflow, template, dan contoh sangat diterima, terutama:

- Kebiasaan CV per negara (aturan CV berbeda di tiap negara), termasuk konvensi CV di Indonesia
- Panduan penyesuaian per jenis pekerjaan (misalnya `rules/roles/software-engineer.md`)
- Terjemahan aturan ke bahasa lain
- Workflow baru (surat lamaran, ringkasan LinkedIn, persiapan wawancara)

Jangan pernah menyertakan data pribadi asli dalam kontribusi. Pakai data fiktif di `examples/`.

## Lisensi

[MIT](LICENSE). Lisensi mencakup aturan, workflow, template, dan alat di repo ini. Data CV-mu di `profile/`, `info/`, `jobs/`, dan `output/` tetap milikmu dan tidak pernah menjadi bagian repo.
