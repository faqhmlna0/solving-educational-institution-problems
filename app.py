import pickle
import streamlit as st
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load model
with open("model.pkl", "rb") as file:
    model_load = pickle.load(file)

minmaxscaler_load = MinMaxScaler()

# Daftar kolom fitur sesuai model
kolom_data = ['Marital_status', 'Displaced', 'Debtor', 'Tuition_fees_up_to_date',
              'Gender', 'Scholarship_holder', 'Age_at_enrollment',
              'Curricular_units_1st_sem_credited', 'Curricular_units_1st_sem_enrolled',
              'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
              'Curricular_units_2nd_sem_credited', 'Curricular_units_2nd_sem_enrolled',
              'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade']

def yesno_convert(option):
    return int(option == 'Yes')

def gender_convert(option):
    return int(option == 'Man')

def marital_convert(option):
    mapping = {
        'Single': 1,
        'Married': 2,
        'Widower': 3,
        'Divorced': 4,
        'Facto Union': 5,
        'Legally Separated': 6
    }
    return mapping.get(option, 0)

def page_deskripsi():
    st.title("🎓 Jaya Jaya Institut Dashboard")

    st.subheader("Apa itu Jaya Jaya Institut?", divider='grey')
    st.markdown('''**Jaya Jaya Institut** merupakan institusi pendidikan tinggi berbasis teknologi yang berkomitmen untuk mencetak lulusan yang berkualitas, adaptif, dan siap menghadapi tantangan masa depan. Dengan dukungan sistem informasi modern, kami secara konsisten berinovasi untuk meningkatkan mutu akademik dan pengalaman belajar mahasiswa secara menyeluruh.''')

    st.subheader("Apa fungsi Predict Machine ini?", divider='grey')
    st.markdown('''**Predict Machine** adalah fitur cerdas berbasis Machine Learning yang dikembangkan untuk memprediksi potensi mahasiswa mengalami dropout (berhenti studi). Sistem ini menggunakan data historis untuk membantu institusi dalam:
- Mengidentifikasi mahasiswa yang memiliki risiko tinggi putus studi.
- Memberikan intervensi dan tindakan preventif secara lebih tepat waktu.
- Meningkatkan efektivitas program retensi dan keberhasilan akademik mahasiswa.''')

    st.subheader("Bagaimana cara menggunakannya?", divider='grey')
    st.markdown('''
1. Lengkapi data mahasiswa pada formulir yang telah disediakan.
2. Masukkan informasi seperti usia, status pernikahan, status beasiswa, serta nilai akademik
3. Tekan tombol **Predict** untuk memperoleh hasil prediksi.
4. Sistem akan menampilkan apakah mahasiswa tersebut berpotensi mengalami dropout atau tidak.
    ''')

def page_prediction():
    st.markdown("## 🎯 Predict Dropout Student")
    st.write("Isi data mahasiswa di bawah ini untuk mendapatkan hasil prediksi.")

    gender_col, age_col, marital_col = st.columns([1.5, 1.5, 2])
    with gender_col:
        Gender = gender_convert(st.radio("Gender", ["Man", "Woman"]))
    with age_col:
        Age_at_enrollment = st.slider("Age at Enrollment", 10, 100, 18)
    with marital_col:
        Marital_status = marital_convert(st.selectbox("Marital Status", 
            ["Single", "Married", "Widower", "Divorced", "Facto Union", "Legally Separated"]))

    debt_col, tuition_col, scholarship_col, displaced_col = st.columns(4)
    with debt_col:
        Debtor = yesno_convert(st.radio("Debtor", ["Yes", "No"], index=1))
    with tuition_col:
        Tuition_fees_up_to_date = yesno_convert(st.radio("Tuition Fees Up to Date", ["Yes", "No"], index=0))
    with scholarship_col:
        Scholarship_holder = yesno_convert(st.radio("Scholarship Holder", ["Yes", "No"], index=1))
    with displaced_col:
        Displaced = yesno_convert(st.radio("Displaced", ["Yes", "No"], index=1))

    sem1_col1, sem1_col2, sem1_col3, sem1_col4 = st.columns(4)
    with sem1_col1:
        Curricular_units_1st_sem_credited = st.number_input("1st Sem Credited", 0.0)
    with sem1_col2:
        Curricular_units_1st_sem_enrolled = st.number_input("1st Sem Enrolled", 0.0)
    with sem1_col3:
        Curricular_units_1st_sem_approved = st.number_input("1st Sem Approved", 0.0)
    with sem1_col4:
        Curricular_units_1st_sem_grade = st.number_input("1st Sem Grade", 0.0)

    sem2_col1, sem2_col2, sem2_col3, sem2_col4 = st.columns(4)
    with sem2_col1:
        Curricular_units_2nd_sem_credited = st.number_input("2nd Sem Credited", 0.0)
    with sem2_col2:
        Curricular_units_2nd_sem_enrolled = st.number_input("2nd Sem Enrolled", 0.0)
    with sem2_col3:
        Curricular_units_2nd_sem_approved = st.number_input("2nd Sem Approved", 0.0)
    with sem2_col4:
        Curricular_units_2nd_sem_grade = st.number_input("2nd Sem Grade", 0.0)

    if st.button("✨ Predict"):
        input_data = pd.DataFrame([[Marital_status, Displaced, Debtor, Tuition_fees_up_to_date,
                                    Gender, Scholarship_holder, Age_at_enrollment,
                                    Curricular_units_1st_sem_credited, Curricular_units_1st_sem_enrolled,
                                    Curricular_units_1st_sem_approved, Curricular_units_1st_sem_grade,
                                    Curricular_units_2nd_sem_credited, Curricular_units_2nd_sem_enrolled,
                                    Curricular_units_2nd_sem_approved, Curricular_units_2nd_sem_grade]],
                                  columns=kolom_data)

        try:
            result = model_load.predict(input_data)
            if result[0] == 0:
                st.success("✅ **Prediksi: Mahasiswa tidak berpotensi dropout.**")
                st.balloons()
            else:
                st.error("⚠️ **Prediksi: Mahasiswa berpotensi mengalami dropout.**")
        except Exception as e:
            st.error(f"❌ Terjadi kesalahan saat melakukan prediksi: {e}")

def main():
    st.set_page_config(page_title="Jaya Jaya Institut", layout="wide")
    tab1, tab2 = st.tabs(["🧾 Description", "🤖 Predict Machine"])
    with tab1:
        page_deskripsi()
    with tab2:
        page_prediction()

if __name__ == "__main__":
    main()