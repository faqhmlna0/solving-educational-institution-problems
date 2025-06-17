# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut adalah institusi pendidikan tinggi berbasis teknologi yang telah berdiri sejak tahun 2000 dan dikenal menghasilkan lulusan berkualitas. Namun, institusi ini menghadapi tantangan serius terkait tingginya angka dropout mahasiswa, yang berdampak pada reputasi, efisiensi operasional, dan pemanfaatan sumber daya. Untuk mengatasinya, Jaya Jaya Institut berupaya mengidentifikasi mahasiswa yang berisiko putus studi sedini mungkin agar dapat memberikan intervensi dan bimbingan yang tepat, sehingga meningkatkan retensi dan keberhasilan akademik secara keseluruhan.

### Permasalahan Bisnis
Jaya Jaya Institut menghadapi tantangan serius terkait tingginya angka mahasiswa yang mengalami dropout, khususnya dalam dua semester pertama. Fenomena ini berdampak langsung pada reputasi, keberlangsungan keuangan, serta kepercayaan masyarakat terhadap kualitas institusi. Saat ini, belum tersedia sistem prediktif yang mampu mengidentifikasi mahasiswa berisiko tinggi sejak awal, sehingga intervensi sering terlambat diberikan.

Tingkat retensi yang bervariasi antar program studi dan minimnya analisis berbasis data juga menghambat pengambilan keputusan yang efektif. Oleh karena itu, dibutuhkan solusi berbasis model klasifikasi yang dapat memetakan potensi dropout mahasiswa secara akurat, berdasarkan data pendaftaran dan kinerja akademik awal. Dengan adanya sistem ini, institusi dapat menyusun strategi intervensi yang lebih tepat untuk meningkatkan tingkat kelulusan dan daya saing.

### Cakupan Proyek
Proyek ini bertujuan untuk menyelesaikan permasalahan di atas dengan cakupan sebagai berikut:
- Mengembangkan dashboard interaktif yang menyajikan data performa mahasiswa serta tren dropout secara real time.
- Membangun model machine learning berbasis data historis untuk memprediksi potensi mahasiswa mengalami dropout.
- Merancang prototipe sistem prediksi menggunakan Streamlit sebagai antarmuka yang mudah diakses oleh pihak akademik.
- Menyusun rekomendasi strategis berbasis data guna membantu institusi dalam menekan angka dropout.

### Persiapan

Sumber data: Dataset yang digunakan berasal dari dicoding untuk latihan menyelesaikan permsalahan data science.
[dataset](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:
```
# Setup virtual environment
python -m venv venv
source venv/bin/activate  # Jika menggunakan Unix/Mac
venv\Scripts\activate     # Jika menggunakan Windows


# Install dependencies
pip install -r requirements.txt

```

## Business Dashboard
Insight dashboard:
Dashboard ini menunjukkan bahwa sekitar 32,1% mahasiswa mengalami dropout, jumlah yang cukup tinggi dan perlu mendapat perhatian serius. Mahasiswa yang tidak menerima beasiswa dan menunggak pembayaran biaya kuliah tampak lebih berisiko mengalami putus studi, yang mengindikasikan bahwa faktor finansial berperan penting terhadap retensi. Selain itu, distribusi gender relatif seimbang, namun tidak menunjukkan perbedaan signifikan terhadap tingkat dropout. Program studi dengan jumlah mahasiswa terbanyak adalah Nursing, Management, dan Social Service, menjadikannya prioritas utama dalam strategi intervensi karena potensi dampaknya yang besar terhadap keseluruhan angka dropout.

Di sisi lain, beberapa jurusan seperti Biofuel Production Technologies, Equinculture, dan Oral Hygiene memiliki jumlah mahasiswa yang sangat sedikit, yang bisa menjadi bahan evaluasi lebih lanjut bagi institusi. Dashboard ini juga memperlihatkan bahwa mahasiswa penerima beasiswa cenderung memiliki tingkat kelulusan lebih tinggi, mendukung perlunya optimalisasi distribusi beasiswa sebagai bentuk intervensi preventif. Dengan visualisasi interaktif ini, manajemen Jaya Jaya Institut dapat lebih mudah mengidentifikasi pola dropout dan menyusun strategi peningkatan retensi secara tepat sasaran.

[Link akses dashboard](https://lookerstudio.google.com/reporting/fd06e6f5-147f-4a8a-be64-c999f4bd31c8)

## Menjalankan Sistem Machine Learning
Sebuah prototipe sistem prediksi mahasiswa yang berpotensi dropout dikembangkan dengan memanfaatkan algoritma Logistic Regression, yang dikenal handal dalam menangani masalah klasifikasi. Sistem ini diintegrasikan ke dalam antarmuka interaktif berbasis Streamlit, sehingga dapat diakses dan digunakan dengan mudah oleh pihak akademik.

Fitur utama pada dashboard untuk melakukan prediksi yaitu:
- Gender
- Age at Enrollment
- Debtor
- Tuition Fees Up to Date
- Scholarship Holder
- Displaced
- Informasi akademi semester 1 dan 2

Setelah data mahasiswa dimasukkan, sistem akan menampilkan hasil prediksi terkait kemungkinan dropout, disertai dengan tampilan visual yang informatif dan mudah dipahami.

```
# Cara Menjalankan Aplikasi
streamlit run app.py
```
[Link prototype Streamlit]()

## Conclusion
Dari proyek ini ditemukan bahwa:
- Sekitar 32% mahasiswa tercatat mengalami dropout selama masa studi mereka.
- Sejumlah variabel seperti usia, status pernikahan, nilai akademik, jumlah mata kuliah yang diambil dan diselesaikan, serta status beasiswa, terbukti memiliki pengaruh signifikan terhadap kemungkinan mahasiswa menyelesaikan studi atau tidak.
- Model Logistic Regression digunakan dalam sistem prediksi dan mampu memberikan hasil yang cukup akurat, dengan tingkat akurasi mencapai 88.9% dalam mengklasifikasikan potensi dropout mahasiswa.

### Rekomendasi Action Items
- Pemantauan Dini: Manfaatkan dashboard interaktif dan sistem prediksi untuk mengidentifikasi mahasiswa dengan risiko tinggi mengalami dropout sejak dini, khususnya pada awal tahun akademik.
- Intervensi Akademik: Sediakan program remedial, bimbingan belajar, atau tutor sebaya bagi mahasiswa dengan performa akademik rendah, karena nilai akademik terbukti menjadi faktor signifikan dalam keputusan dropout.
- Evaluasi Program Beasiswa: Lakukan peninjauan ulang terhadap kriteria penerima beasiswa, agar distribusi lebih tepat sasaran dan mendukung mahasiswa dari latar belakang ekonomi rentan agar tidak terpaksa keluar.
- Monitoring Status Keuangan: Pantau status pembayaran uang kuliah secara aktif. Mahasiswa dengan tunggakan pembayaran dapat diberi pendekatan personal, pengingat, atau opsi cicilan agar tidak terdorong dropout karena alasan finansial.
- Pendekatan Personal untuk Mahasiswa Berisiko: Kembangkan pendekatan berbasis pembimbing akademik atau konselor yang bisa melakukan check-in rutin terhadap mahasiswa dengan indikator risiko dropout tinggi.
- Peningkatan Work-Life Balance: Bagi mahasiswa yang mengikuti kelas malam atau bekerja sambil kuliah, institusi dapat menawarkan opsi fleksibel seperti kelas hybrid atau waktu belajar yang disesuaikan.
