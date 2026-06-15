# MyStudyBuddy — Proses Pengolahan Data untuk Fitur Summarize

Deskripsi singkat tentang alur pengolahan data yang dipakai untuk membuat model AI fitur _summarize_ pada aplikasi MyStudyBuddy.

## Tujuan

Menyusun sebuah dataset yang bersih dan terstandarisasi untuk melatih model ringkasan (summarization). Hasil akhir berupa file CSV/Parquet dengan tiga kolom: `text`, `summary`, dan `source`.

## Sumber Data

- Dataset publik dari Kaggle (berbagai dataset teks yang relevan).
- Dataset publik dari Hugging Face (corpora, news, dan dataset ringkasan tersedia).
- Pengambilan data sendiri dari Wikipedia (artikel yang dipilih dan diproses).

Link dataset:

- Kaggle: https://www.kaggle.com/datasets/linkgish/indosum
- Hugging Face: https://huggingface.co/datasets/csebuetnlp/xlsum

## Overview Proses

1. Pengumpulan (collection)
   - Unduh dataset relevan dari Kaggle dan Hugging Face.
   - Crawl atau ekspor artikel Wikipedia yang diperlukan.
2. Pembuatan Model Peringkas
   - Model peringkas merupakan jenis Peringkas Ekstraksi.
   - Model dilatih menggunakan pretrained MobileBert.
   - Proses fine-tuning, melatih model dengan data yang sudah melalui preprocessing.
   - Export hasil model ke dalam format ONNX.
3. Uji Coba Inference Model
   - Menjalankan endpoint FastAPI untuk ujicoba inference model 
   - Verifikasi tokenizer dan model ONNX.
   - Untuk implementasi percobaan di `models/coba-inference/`, pastikan `Preprocessing` memecah kalimat, tokenisasi berjalan dengan vocab MobileBERT, dan `SummaryGenerator` menghasilkan ringkasan berdasarkan skor kalimat.
