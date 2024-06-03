import streamlit as st
import pandas as pd
import numpy as np
import joblib

model_lr = joblib.load('logistic_regression_model.pkl')
encoder = joblib.load('preprocessor.pkl')
image = 'Employee-Attrition.jpg'

def preprocess_input(data, encoder):
    data_encoded = encoder.transform(data)
    return data_encoded

def display_sidebar():
    st.sidebar.subheader("Masukkan Data Karyawan")

    education_desc = "Tingkat Pendidikan (1: 'Below College', 2: 'College', 3: 'Bachelor', 4: 'Master')"
    education = st.sidebar.selectbox(education_desc, [1, 2, 3, 4], key='education')

    environment_satisfaction_desc = "Kepuasan Lingkungan (1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High')"
    environment_satisfaction = st.sidebar.selectbox(environment_satisfaction_desc, [1, 2, 3, 4], key='environment_satisfaction')

    job_involvement_desc = "Keterlibatan Pekerjaan (1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High')"
    job_involvement = st.sidebar.selectbox(job_involvement_desc, [1, 2, 3, 4], key='job_involvement')

    job_level = st.sidebar.selectbox("Level Pekerjaan", [1, 2, 3, 4, 5], key='job_level')

    job_satisfaction_desc = "Kepuasan Pekerjaan (1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High')"
    job_satisfaction = st.sidebar.selectbox(job_satisfaction_desc, [1, 2, 3, 4], key='job_satisfaction')

    num_companies_worked = st.sidebar.number_input("Jumlah Perusahaan yang Dikerjakan Sebelumnya", min_value=0, key='num_companies_worked')

    percent_salary_hike = st.sidebar.slider("Persentase Kenaikan Gaji Terakhir", min_value=0, max_value=100, step=1, key='percent_salary_hike')

    relationship_satisfaction_desc = "Kepuasan Hubungan (1: 'Low', 2: 'Medium', 3: 'High', 4: 'Very High')"
    relationship_satisfaction = st.sidebar.selectbox(relationship_satisfaction_desc, [1, 2, 3, 4], key='relationship_satisfaction')

    stock_option_level = st.sidebar.selectbox("Level Opsi Saham di Perusahaan", [0, 1, 2, 3], key='stock_option_level')

    training_times_last_year = st.sidebar.number_input("Jumlah Pelatihan yang Diikuti Tahun Lalu", min_value=0, key='training_times_last_year')

    work_life_balance_desc = "Keseimbangan Kehidupan Kerja (1: 'Bad', 2: 'Good', 3: 'Better', 4: 'Best')"
    work_life_balance = st.sidebar.selectbox(work_life_balance_desc, [1, 2, 3, 4], key='work_life_balance')

    years_since_last_promotion = st.sidebar.number_input("Tahun Sejak Promosi Terakhir", min_value=0, key='years_since_last_promotion')

    overtime = st.sidebar.selectbox("Lembur", ["Yes", "No"], key='overtime')

    travel = st.sidebar.selectbox("Frekuensi Perjalanan Dinas", ["Travel_Rarely", "Travel_Frequently", "Non-Travel"], key='travel')

    department = st.sidebar.selectbox("Departemen", ["Sales", "Research & Development", "Human Resources"], key='department')

    education_field = st.sidebar.selectbox("Bidang Pendidikan", ["Life Sciences", "Medical", "Marketing", "Technical Degree", "Human Resources", "Other"], key='education_field')

    gender = st.sidebar.selectbox("Jenis Kelamin", ["Male", "Female"], key='gender')

    job_role = st.sidebar.selectbox("Jabatan", ["Sales Executive", "Research Scientist", "Laboratory Technician", "Manufacturing Director", "Healthcare Representative", "Manager", "Sales Representative", "Research Director", "Human Resources"], key='job_role')

    marital_status = st.sidebar.selectbox("Status Pernikahan", ["Single", "Married", "Divorced"], key='marital_status')

    age_group = st.sidebar.selectbox("Kelompok Usia", ["<30", "30-39", "40-49", "50+"], key='age_group')

    daily_rate_group = st.sidebar.selectbox("Penghasilan Harian", ["0-599", "600-999", "1000-1299", "1300+"], key='daily_rate_group')

    monthly_rate_group = st.sidebar.selectbox("Penghasilan Bulanan", ["0-4.999", "5.000-9.999", "10.000-14.999", "15.000-19.999", "20.000+"], key='monthly_rate_group')

    distance_group = st.sidebar.selectbox("Jarak Tempuh ke Tempat Kerja", ["0-4 miles", "5-9 miles", "10-14 miles", "15-19 miles", "20+ miles"], key='distance_group')

    hourly_rate_group = st.sidebar.selectbox("Tarif Per Jam", ["0-49", "50-69", "70+"], key='hourly_rate_group')

    years_at_company_group = st.sidebar.selectbox("Lama Bekerja di Perusahaan", ["0-4 years", "5-9 years", "10-14 years", "15+ years"], key='years_at_company_group')

    input_data = pd.DataFrame({
        'Education': [education],
        'EnvironmentSatisfaction': [environment_satisfaction],
        'JobInvolvement': [job_involvement],
        'JobLevel': [job_level],
        'JobSatisfaction': [job_satisfaction],
        'NumCompaniesWorked': [num_companies_worked],
        'PercentSalaryHike': [percent_salary_hike],
        'RelationshipSatisfaction': [relationship_satisfaction],
        'StockOptionLevel': [stock_option_level],
        'TrainingTimesLastYear': [training_times_last_year],
        'WorkLifeBalance': [work_life_balance],
        'YearsSinceLastPromotion': [years_since_last_promotion],
        'OverTime': [overtime],
        'BusinessTravel': [travel],
        'Department': [department],
        'EducationField': [education_field],
        'Gender': [gender],
        'JobRole': [job_role],
        'MaritalStatus': [marital_status],
        'AgeGroup': [age_group],
        'DailyRateGroup': [daily_rate_group],
        'MonthlyRateGroup': [monthly_rate_group],
        'DistanceGroup': [distance_group],
        'HourlyRateGroup': [hourly_rate_group],
        'YearsAtCompanyGroup': [years_at_company_group]
    })

    return input_data

def predict_attrition(data):
    data_encoded = preprocess_input(data, encoder)
    probability = model_lr.predict_proba(data_encoded)[:, 1]
    return round(probability[0], 2)

def main():
    st.set_page_config(page_title="Aplikasi Prediksi Attrition", page_icon=":bar_chart:", layout="wide")
    st.title("Aplikasi Prediksi Attrition")

    st.image(image, use_column_width=True)

    # Display sidebar
    input_data = display_sidebar()

    st.markdown("***")

    if st.sidebar.button("Prediksi"):
        probability = predict_attrition(input_data)
        st.subheader("Hasil Prediksi Attrition:")
        st.write("Probabilitas Attrition:", probability)
        if probability > 0.5:
            st.error("Ya")
        else:
            st.success("Tidak")


    st.markdown("***")
    st.markdown(
        "<div style='text-align: center; color: #666; margin-top: 30px;'>Copyright © 2024 | arifsofyan004@gmail.com</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
