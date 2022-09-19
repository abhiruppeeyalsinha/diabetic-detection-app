import streamlit as st,pickle
import datetime

yr = datetime.datetime.now().year

model = pickle.load(open("dt_clf!!.sav","rb"))
def main():
    string = "Diabetic Detection!!"
    st.set_page_config(page_title=string, page_icon="⚕️")
    st.title("Diabetic Detection ⚕️")
    st.markdown("Let's Do Diagnosis")
    st.image("test_img.png", width=1000
             )
    st.write("")
    st.write("")
    age = st.number_input("Birth Year? ",step=1,key='age')
    # age = yr - dob
    Pregnancies = st.number_input("Pregnancies",key = "Pregnancies")
    Glucose = st.number_input("Glucose",key = "Glucose")
    Blood_Pressure = st.number_input("Blood Pressure",key = "Blood Pressure")
    SkinThickness = st.number_input("SkinThickness",key = "SkinThickness")
    Insulin = st.number_input("Insulin",key = "Insulin")
    BMI = st.number_input("BMI",key = "BMI")
    Diabetes_Pedigree_Function = st.number_input("Diabetes Pedigree Function",key = "Diabetes Pedigree Function")

    if st.button("Result", key="predict"):
        try:
            prediction = model.predict([[age,Pregnancies,Glucose,Blood_Pressure,SkinThickness,Insulin,BMI,Diabetes_Pedigree_Function]])
            output = round(prediction[0],2)
            if output == 0:
                st.success("The Patient is Non Diabetic!!")
            else:
                st.success("The Patient is Diabetic")

        except:
            st.warning("Opps!! Something went wrong\n Try again")


if __name__ =="__main__":
    main()

