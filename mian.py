from pathlib import Path
import streamlit as st
import numpy as np
from streamlit_option_menu import option_menu
from PIL import Image
import pickle
import streamlit.components.v1 as components

current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

css_file="main.css"
resume_file = "vigneshwaranResume.pdf"
profile_pic = "RMKEC.jpeg"


PAGE_TITLE = "Vigneshwaran"
NAME = "N Vigneshwaran"
DESCRIPTION = """
     AI Enthusiast: Pioneering Innovation Through Code, Collaboration, and Creative Ingenuity
"""
EMAIL = "vign22112.it@rmkec.ac.in"
SOCIAL_MEDIA = {
    "LinkedIn":"https://www.linkedin.com/in/vigneshwaranit/",
    "GitHub": "https://github.com/RMKEC111722203119?tab=repositories",
}



st.set_page_config(page_title=PAGE_TITLE)

with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
    
    
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


diabetes_model = pickle.load(open("diabetesmodel.sav", 'rb'))
churn_model= pickle.load(open("churn_logistic.sav", 'rb'))
parkinsons_model= pickle.load(open("parkinsons_model.sav", 'rb'))


#with st.sidebar:
selected = option_menu(
    menu_title=None,
    options=["Profile","ML project","frontend project"],
    default_index=0,
    orientation="horizontal")

if selected == "Profile":
            st.write('\n')
            col1, col2 = st.columns(2)
            
            with col1:
                st.image(profile_pic, width=230)
                
            with col2:
                st.title(NAME)
                st.write(DESCRIPTION)
                st.download_button(
                    label=" 📄 Download Resume",
                    data=PDFbyte,
                    file_name="resume",
                    mime="application/octet-stream",
                )
                st.write("📫", EMAIL)
                
                
                st.write('\n')
                
            cols = st.columns(len(SOCIAL_MEDIA))
            for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
                cols[index].write(f"[{platform}]({link})")
                    
                        
                    
            st.write('\n')
            
            st.subheader("About me")
            st.write("---")
            st.write(
                """
                Driven by a fervent enthusiasm for AI (Artificial Intelligence), I have actively
            participated in diverse hackathons, where I demonstrated not only a profound
            problem-solving acumen but also an adeptness for collaborative teamwork. I have
            honed my abilities in Machine Learning (ML) to design and implement algorithms.
            Furthermore, my proficiency in front-end technologies, including HTML, CSS, and JS,
            underscores my capacity to create seamless and intuitive user interfaces. This
            amalgamation of technical prowess and collaborative spirit positions me as a
            valuable asset, ready to contribute to cutting-edge projects
            
                """
            )
            
            
            st.write('\n')
                    
            st.subheader("Skills")
            st.write(
                """
                    Known Skills
                    
                    Machine Learning
                    
                    DataScience
                    
                    Frontend
                    
                    Python,Java,c++
                    
                    Html,Css,Javascript
                    
                Beginner Skills
                
                    Deep Learning
                    
                    React
            
                """
            )

if selected == "ML project":
        selecte = st.selectbox(
            "Select project",
            options=["Diabetes Prediction","Parkinsons Prediction","Customer churn Prediction"],
            )
        if selecte == "Diabetes Prediction":
            
                st.title('Diabetes Prediction using ML')
                
                col1, col2, col3 = st.columns(3)
    
                with col1:
                    Pregnancies = st.text_input('Number of Pregnancies')
                    
                with col2:
                    Glucose = st.text_input('Glucose Level')
                
                with col3:
                    BloodPressure = st.text_input('Blood Pressure value')
                
                with col1:
                    SkinThickness = st.text_input('Skin Thickness value')
                
                with col2:
                    Insulin = st.text_input('Insulin Level')
                
                with col3:
                    BMI = st.text_input('BMI value')
                
                with col1:
                    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
                
                with col2:
                    Age = st.text_input('Age of the Person')
    
                
                # code for Prediction
                diab_diagnosis = ''
                
                # creating a button for Prediction
                
                if st.button('Diabetes Test Result'):
                    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
                    
                    if (diab_prediction[0] == 1):
                      diab_diagnosis = 'The person is diabetic'
                    else:
                      diab_diagnosis = 'The person is not diabetic'
                    
                st.success(diab_diagnosis)
                
                st.write('\n')
                

               
              
        
        
        if selecte =="Customer churn Prediction":
        
             
                    st.title('Customer churn Prediction using ML')
                     
                      # with col1:
                     # with col1:
                    CreditScore = st.text_input('CreditScore')
                
                    # with col2:
                    Age = st.text_input('Age')
                
                    # with col3:
                    Tenure = st.text_input('Tenure')
                
                    # with col4:
                    Balance = st.text_input('Balance')
                
                    # with col5:
                    NumOfProducts = st.text_input('Num Of Products')
                
                    EstimatedSalary = st.text_input('EstimatedSalary')
                
                    st.header("Enter 0 for no and 1 for yes")
                
                    # with col6:
                    HasCrCard = st.text_input('HasCrCard')
                
                    # with col7:
                    IsActiveMember = st.text_input('IsActiveMember')
                
                    # with col8:
                    Geography_Germany = st.text_input('Geography_Germany')
                
                    # with col9:
                    Geography_Spain = st.text_input('Geography_Spain')
                
                    # with col10:
                    Gender_Male = st.text_input('Gender_Male')
                
                    diab_diagnosis = ''
                
                    # ... (previous code)

                    if st.button('Diabetes Test Result'):
                        features = np.array([
                            float(CreditScore), float(Age), float(Tenure), float(Balance),
                            float(NumOfProducts), float(HasCrCard), float(IsActiveMember),
                            float(EstimatedSalary), float(Geography_Germany),
                            float(Geography_Spain), float(Gender_Male)
                        ]).reshape(1, -1)
                    
                        diab_prediction = churn_model.predict(features)
                        
                    
                        if diab_prediction[0] == 1:
                            diab_diagnosis = 'The person will continue'
                        else:
                            diab_diagnosis = 'The person will not continue'
                            
                        st.success(diab_diagnosis)
                    
                    

                        
                        
        if selecte =="Parkinsons Prediction":
            
            
            st.title("Parkinson's Disease Prediction using ML")
   
            col1, col2, col3, col4, col5 = st.columns(5)  
            
            with col1:
                fo = st.text_input('MDVP:Fo(Hz)')
                
            with col2:
                fhi = st.text_input('MDVP:Fhi(Hz)')
                
            with col3:
                flo = st.text_input('MDVP:Flo(Hz)')
                
            with col4:
                Jitter_percent = st.text_input('MDVP:Jitter(%)')
                
            with col5:
                Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
                
            with col1:
                RAP = st.text_input('MDVP:RAP')
                
            with col2:
                PPQ = st.text_input('MDVP:PPQ')
                
            with col3:
                DDP = st.text_input('Jitter:DDP')
                
            with col4:
                Shimmer = st.text_input('MDVP:Shimmer')
                
            with col5:
                Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
                
            with col1:
                APQ3 = st.text_input('Shimmer:APQ3')
                
            with col2:
                APQ5 = st.text_input('Shimmer:APQ5')
                
            with col3:
                APQ = st.text_input('MDVP:APQ')
                
            with col4:
                DDA = st.text_input('Shimmer:DDA')
                
            with col5:
                NHR = st.text_input('NHR')
                
            with col1:
                HNR = st.text_input('HNR')
                
            with col2:
                RPDE = st.text_input('RPDE')
                
            with col3:
                DFA = st.text_input('DFA')
                
            with col4:
                spread1 = st.text_input('spread1')
                
            with col5:
                spread2 = st.text_input('spread2')
                
            with col1:
                D2 = st.text_input('D2')
                
            with col2:
                PPE = st.text_input('PPE')
                
            
            
            # code for Prediction
            parkinsons_diagnosis = ''
            
            # creating a button for Prediction    
            if st.button("Parkinson's Test Result"):
                     parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
                
                     if (parkinsons_prediction[0] == 1):
                         parkinsons_diagnosis = "The person has Parkinson's disease"
                     else:
                         parkinsons_diagnosis = "The person does not have Parkinson's disease"
                
            st.success(parkinsons_diagnosis)
            
            
if selected == "frontend project":
   
    selec = st.selectbox(
            "Select project",
            options=["YOUTUBE","NETFLIX"]
        )

    if selec == "YOUTUBE":
        st.header("YOUTUBE CLONE")
        st.markdown("[LINK: CLICK HERE](https://vigneshdeployment.github.io/youtube/)")
        st.markdown("[GITHUB: CLICK HERE](https://github.com/RMKEC111722203119/YOUTUBE)")
        st.write("\n")
        st.components.v1.iframe("https://vigneshdeployment.github.io/youtube/", width=800, height=800,scrolling=True)

    if selec == "NETFLIX":
        st.header("NETFLIX CLONE")
        st.markdown("[LINK: CLICK HERE](https://vigneshdeployment.github.io/netflix/)")
        st.markdown("[GITHUB: CLICK HERE](https://github.com/RMKEC111722203119/Bharat-internship-web-dev-/tree/81b48e5d5592a74b41bfbea0c6635c21852e4fe3/netflix)")
        st.write("\n")
        st.components.v1.iframe("https://vigneshdeployment.github.io/netflix/", width=900, height=900,scrolling=True)

    

          



            
