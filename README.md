# Menyelesaikan-Permasalahan-Human-Resources

## Business Understanding
Perusahaan Jaya Jaya Maju merupakan perusahaan multinasional yang beroperasi sejak 2000, memiliki lebih dari 1000 karyawan di seluruh negeri. Meskipun besar, perusahaan mengalami attrition rate yang tinggi (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%. Hal ini menunjukkan adanya masalah dalam retensi karyawan dan manajemen sumber daya manusia. Untuk menjaga pertumbuhan dan produktivitas, penting untuk memahami faktor-faktor yang memengaruhi kepuasan dan retensi karyawan.

### Permasalahan Bisnis
- Menurunkan tingkat turnover karyawan (attrition) dalam perusahaan.
- Meningkatkan pemahaman terhadap faktor-faktor yang memengaruhi keputusan karyawan untuk meninggalkan perusahaan.
- Mengidentifikasi pola-pola yang berkaitan dengan attrition untuk pengambilan keputusan yang lebih efektif dalam manajemen sumber daya manusia.

### Cakupan Proyek
- Analisis data untuk mengidentifikasi faktor-faktor yang berkorelasi dengan tingkat attrition.
- Visualisasi dan pemodelan data untuk pemahaman yang lebih baik tentang pola-pola attrition.
- Pengembangan strategi atau rekomendasi berdasarkan hasil analisis untuk mengurangi tingkat attrition.
- Pembuatan Dashboard di Power BI
- Melakukan deployment dengan membuat aplikasi prediksi attrition di streamlit

### Persiapan

Sumber data: [....](https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee)

Setup environment:
```
conda create --name HumanResources python=3.9
conda activate HumanResources
pip install pandas matplotlib seaborn numpy scikit-learn xgboost plotly imbalanced-learn joblib
```

## Business Dashboard
Business dashboard yang telah dibuat memberikan gambaran lengkap tentang data karyawan perusahaan. Di dalamnya, terdapat informasi  seperti total jumlah karyawan, jumlah karyawan yang mengalami attrition, dan tingkat attrition secara keseluruhan. Selain itu, dashboard ini juga menampilkan jumlah karyawan yang aktif, jumlah karyawan dengan status "Unknown", serta berbagai plot yang menggambarkan hubungan attrition dengan berbagai faktor, seperti grup usia, jabatan, jarak tempuh, tahun bekerja, status pernikahan, lembur, dan jenis kelamin. Dengan demikian, dashboard ini memberikan pandangan menyeluruh yang dapat membantu manajemen dalam membuat keputusan strategis terkait pengelolaan sumber daya manusia perusahaan.

```
https://app.powerbi.com/groups/b55d87d5-8f7f-438c-a9fc-f69c2155c150/reports/6a37047a-c972-42a8-ab78-37d1bd2ccaa7?ctid=a9363dc0-72ee-460b-8b09-7926ec16cd69&pbi_source=linkShare
```

## Menjalankan Sistem Machine Learning

```
https://drive.google.com/file/d/1lS1cz-iM7NYQ9jru9E1z38id_TxFfvEC/view?usp=sharing
```

## Conclusion
Proyek ini memberikan wawasan yang berharga tentang faktor-faktor yang berkontribusi terhadap tingkat attrition di perusahaan. Analisis data menunjukkan bahwa variabel seperti usia, tingkat pendidikan, jenis kelamin, dan kepuasan kerja memiliki korelasi yang signifikan dengan attrition. Dari sini, dapat disimpulkan bahwa perusahaan perlu memperhatikan faktor-faktor ini dalam upaya untuk mengurangi tingkat attrition dan mempertahankan tenaga kerja yang berharga.

### Rekomendasi Action Items
- meninjau kembali kebijakan kompensasi untuk memastikan keseimbangan yang adil dan kompetitif
- evaluasi kepuasan kerja di tingkat entry-level 
- Meningkatkan program pengembangan karir untuk karyawan yang baru 
- meningkatkan program keseimbangan kerja-hidup yang fleksibel
- Pertimbangkan strategi untuk mengelola waktu dan tugas agar meminimalkan lembur yang berlebihan
- menyediakan lebih banyak kesempatan pengembangan karir untuk karyawan yang berstatus single.

## Run steamlit app
```
streamlit run prediksi_attrition_app.py
```
## Untuk mencoba aplikasi bisa lewat link dibawah ini
```
https://aplikasi-prediksi-attrition.streamlit.app/
```
