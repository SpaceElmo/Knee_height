#Height calculator from Knee height
import numpy as np
from datetime import datetime,date
import streamlit as st

st.title('Height calculator from entered knee height')
st.write('Three alternative methods are used here. The Argentine method is CP specific. Please enter knee height in cm')
st.write('This app does not caclutate centile but that may be a future feature')
format ="%d/%m/%Y"
calc_type={'Stevenson':True,'Indonesian':True,'Argentine_CP':True}
calc_type={key:False for key in calc_type}
today = datetime.today()
kh = st.number_input("Enter knee height (in cm):", min_value=0.0, max_value=100.0, step=0.1, format="%.2f")


option1=st.radio('Select a calculation type',['Stevenson','Indonesian','Argentine_CP'])
calc_type[option1]=True
if calc_type['Stevenson']:
    ht=2.69*kh+24.2
    st.markdown(f"<h1 style='font-size:40px;'>The approximate height is {ht:.1f}cm using Stevenson</h1>", unsafe_allow_html=True)


if calc_type['Argentine_CP']:
    
    GMFCS={'I-III':False,'IV-V':False}
    gender={key:False for key in GMFCS}

    function= st.selectbox("Select GMFCS group:", ["I-III", "IV-V"])
    if function=='I=III':
        GMFCS['I-III']=True
    else:
        GMFCS['IV-V']=True   
    dob = st.date_input("Enter the date of birth:", value=date.today(), min_value=date(2005, 1, 1),
    format="DD/MM/YYYY")

 
    delta_year = today.year - dob.year
    delta_month = today.month - dob.month
    age_months = delta_year*12 + delta_month
    age_years=age_months/12
    st.write(f'This equates to {age_years:.1f} years')
    if GMFCS['I-III']:
        ht=1.5*kh+2.28*age_years+51
        st.markdown(f"<h1 style='font-size:40px;'>The approximate height is {ht:.1f}cm using Argentine for GMFCS I-III</h1> ", unsafe_allow_html=True)
    if GMFCS['IV-V']:
        ht=2.13*kh+0.91*age_years+37   
        st.markdown(f"<h1 style='font-size:40px;'>The approximate height is {ht:.1f}cm using Argentine for GMFCS IV-V</h1> ", unsafe_allow_html=True)

if calc_type['Indonesian']:
    
    gender={'Male':False,'Female':False}
    gender={key:False for key in gender}

    sex= st.selectbox("Select Birth Gender:", ["m", "f"])
    if sex=='m':
        gender['Male']=True
    else:
        gender['Female']=True   
    dob = st.date_input("Enter the date of birth:", value=date.today(), min_value=date(2005, 1, 1),
    format="DD/MM/YYYY")

 
    delta_year = today.year - dob.year
    delta_month = today.month - dob.month
    age_months = delta_year*12 + delta_month
    st.write(f'This equates to {age_months} whole months')
    if gender['Male']:
        ht=29.895+(0.081*age_months+2.267*kh)
        st.markdown(f"<h1 style='font-size:40px;'>The approximate height is {ht:.1f}cm using Indonesian</h1> for a Male", unsafe_allow_html=True)
    if gender['Female']:
        ht=26.297+(0.11*age_months+2.278*kh)    
        st.markdown(f"<h1 style='font-size:40px;'>The approximate height is {ht:.1f}cm using Indonesian</h1> for a Female", unsafe_allow_html=True)
st.markdown(f"<h1 style='font-size:30px;'>References</h1>",unsafe_allow_html=True)
st.write('Indonesian equations are from this paper:')
st.write('*Rumapea F, Fadlyana E, Dhamayanti M, Tarigan R, Rahmayani R, Rusmil K. Height Prediction Using the Knee Height Measurement Among Indonesian Children. Food Nutr Bull. 2021 Jun;42(2):247-258.*',unsafe_allow_html=True)
st.write ('Argentine equations are from this paper:')
st.write('*Ruiz Brunner M, Cieri ME, Lucero Brunner RA, Condinanzi AL, Gil C, Cuestas E. Software and equations using segmental measures to estimate height in children and adolescents with cerebral palsy considering the level of gross motor function. Clin Nutr ESPEN. 2024 Aug;62:234-240.*',unsafe_allow_html=True)   
st.write('The Stevenson equation is from this paper:')
st.write('*Stevenson RD. Use of segmental measures to estimate stature in children with cerebral palsy. Arch Pediatr Adolesc Med. 1995 Jun;149(6):658-62.*',unsafe_allow_html=True)

st.markdown("""<h1 style='font-size:30px;'>To obtain a knee height this is the SOP</h1>""",unsafe_allow_html=True)
st.markdown("""
1. Remove shoes and any splints on lower legs
2. Ensure the child is sat in wheelchair with it in an upright position
3. Ensure lower leg is clear of trousers where it is possible to roll them to ensure contact of segmometer with skin
4. Ensure the knee and ankle are at right ankles to the lower leg long bones (tibia and fibia)
5. Measure from heel to anterior surface of thigh (top of the knee)
6. Repeat for both left and right leg on 1st measurement. 
7. Document which side measured as the longest knee  and repeat all subsequent future measurements with the same leg
8. Use this value in the calculation above
""")

