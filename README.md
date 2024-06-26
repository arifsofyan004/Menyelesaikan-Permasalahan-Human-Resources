# Menyelesaikan-Permasalahan-Human-Resources

## Business Understanding
Perusahaan Jaya Jaya Maju merupakan perusahaan multinasional yang beroperasi sejak 2000, memiliki lebih dari 1000 karyawan di seluruh negeri. Meskipun besar, perusahaan mengalami attrition rate yang tinggi (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%. Hal ini menunjukkan adanya masalah dalam retensi karyawan dan manajemen sumber daya manusia. Untuk menjaga pertumbuhan dan produktivitas, penting untuk memahami faktor-faktor yang memengaruhi kepuasan dan retensi karyawan.

### Permasalahan Bisnis
- **Tingkat Attrition yang Tinggi**: Perusahaan mengalami tantangan dalam menurunkan tingkat turnover karyawan, yang dapat mengganggu kontinuitas operasional dan stabilitas tim.
- **Kekurangan Sumber Daya Manusia**: Setiap kali karyawan meninggalkan perusahaan, itu berarti kehilangan sumber daya manusia yang berpengalaman dan berpotensi, mengakibatkan biaya tambahan untuk merekrut dan melatih karyawan baru.
- **Pentingnya Analisis Faktor-Faktor**: Memahami faktor-faktor yang mempengaruhi keputusan karyawan untuk meninggalkan perusahaan menjadi kunci untuk mengimplementasikan strategi retensi yang efektif.
- **Dampak Terhadap Produktivitas**: Tingginya tingkat attrition dapat mengganggu produktivitas tim, mempengaruhi morale karyawan, dan mengurangi efisiensi operasional.
- **Risiko Reputasi dan Kompetitivitas**: Attrition yang tinggi dapat merusak reputasi perusahaan sebagai tempat kerja yang stabil dan mengurangi daya tarik bagi calon karyawan, mempengaruhi kemampuan perusahaan untuk bersaing di pasar tenaga kerja.

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
pip install -r requirements.txt
```

## Business Dashboard
Business dashboard yang telah dibuat memberikan gambaran lengkap tentang data karyawan perusahaan. Di dalamnya, terdapat informasi  seperti total jumlah karyawan, jumlah karyawan yang mengalami attrition, dan tingkat attrition secara keseluruhan. Selain itu, dashboard ini juga menampilkan jumlah karyawan yang aktif, jumlah karyawan dengan status "Unknown", serta berbagai plot yang menggambarkan hubungan attrition dengan berbagai faktor, seperti grup usia, jabatan, jarak tempuh, tahun bekerja, status pernikahan, lembur, dan jenis kelamin. Dengan demikian, dashboard ini memberikan pandangan menyeluruh yang dapat membantu manajemen dalam membuat keputusan strategis terkait pengelolaan sumber daya manusia perusahaan.

```
https://public.tableau.com/shared/CYH9HKZZD?:display_count=n&:origin=viz_share_link
```

```
https://app.powerbi.com/groups/b55d87d5-8f7f-438c-a9fc-f69c2155c150/reports/6a37047a-c972-42a8-ab78-37d1bd2ccaa7?ctid=a9363dc0-72ee-460b-8b09-7926ec16cd69&pbi_source=linkShare
```

## Menjalankan Sistem Machine Learning

Untuk menjalankan prototipe sistem machine learning yang telah dibuat, Anda dapat mengikuti langkah-langkah berikut. Langkah-langkah ini bertujuan untuk membantu departemen HR dalam menggunakan script tersebut untuk menganalisis data karyawan dan memprediksi tingkat attrition.

## Menjalankan Sistem Machine Learning

### Langkah-langkah:

1. **Download Script dan Dataset**
   - Pastikan Anda telah mengunduh script dan dataset yang diperlukan. Anda dapat mengunduh script machine learning dari link berikut:
   ```
   https://github.com/arifsofyan004/Menyelesaikan-Permasalahan-Human-Resources/blob/main/submission_pertama_menyelesaikan_permasalahan_human_resources.py
   ```

2. **Setup Environment**
   - Buat environment baru menggunakan Anaconda atau virtual environment. Berikut adalah contoh cara membuat environment baru menggunakan Anaconda:
     ```
     conda create --name HumanResources python=3.9
     conda activate HumanResources
     ```
   - Instal semua paket yang diperlukan dengan menggunakan pip:
     ```
     pip install -r requirements.txt
     ```

3. **Jalankan Script**
   - Buka script yang telah diunduh menggunakan IDE atau editor kode seperti Jupyter Notebook, VSCode, atau PyCharm.
   - Pastikan dataset berada di lokasi yang benar dan sesuai dengan path yang ditentukan dalam script.
   - Jalankan script untuk memulai proses training model machine learning dan evaluasi hasilnya.

### Proses yang Dilakukan dalam Script:
- **Load Dataset**: Membaca dataset karyawan.
- **Preprocessing Data**: Melakukan pembersihan data dan preprocessing, termasuk handling missing values, encoding categorical variables, dan scaling.
- **Oversampling**: Menggunakan SMOTE untuk menangani ketidakseimbangan kelas.
- **Model Training**: Melatih model Logistic Regression dan XGBoost dengan hyperparameter tuning menggunakan GridSearchCV atau RandomizedSearchCV.
- **Model Evaluation**: Mengevaluasi model menggunakan metrik seperti confusion matrix, classification report, dan ROC-AUC score.
- **Model Saving**: Menyimpan model yang terlatih menggunakan joblib untuk digunakan deployment membuat aplikasi prediksi attrition.

### Mengakses Aplikasi Prediksi Attrition:
- Anda dapat mengakses Aplikasi Prediksi Attrition melalui link berikut:
```
https://aplikasi-prediksi-attrition.streamlit.app/
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
