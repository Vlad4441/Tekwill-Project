import streamlit as st
from functions import predict_json
from dataProcess2 import process2
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "prezicenota-8a077669741d.json"
col = ['Sex', 'Treapta', 'Profil', 'Clasa', 'Age', 'GO OUT', 'Study time', 'Trip time', 'Location', 'Mom ed', 'Dad ed', 'School sup',
       'Mom job', 'Dad job', 'Failiures', 'Health', 'Attendance', 'School extra', 'University', 'Weekly alcohol', 'Weekend alcohol',
       'Parents', 'Internet', 'Relationship']
d = dict()
st.header('Completează formularul și vezi viitoarea ta notă')

d[col[0]] = st.selectbox('Sex',options=[" ","masculin","feminin"])
d[col[1]] = st.selectbox('Treapta de învățământ', options=[" ", "Liceu", "Gimnaziu"])
d[col[2]] = st.selectbox('Profil', options=[" ", "Real", "Uman", "Nu am încă profil"])
if d[col[2]] == "Nu am încă profil":
    d[col[2]] = 'Uman'
d[col[3]] = st.selectbox('Clasa', options=[" ",5,6,7,8,9,10,11,12])
d[col[4]] = st.number_input('Vârsta ta',step=1,min_value=9,max_value=19)
d[col[5]] = st.selectbox('Timpul petrecut cu prietenii (1-foarte putin, 5-foarte mult)', options=[" ",1,2,3,4,5])
d[col[6]] = st.selectbox('Timpul petrecut învățând săptămânal', options=[" ",'mai puțin de 2 ore','2 - 5 ore','5 - 10 ore','10 - 15 ore','mai mult de 15 ore'])
d[col[7]] = st.selectbox('Durata navetei până la școală', options=[" ",'mai puțin de 15 minute','15 - 30 minute', '30 minute - 1 oră'])
d[col[8]] = st.selectbox('Mediul de trai', options=[" ",'Urban',"Rural"])
d[col[9]] = st.selectbox('Nivelul de educație al mamei', options=[" ",'educație primară (clasa 1-4)','educație gimnazială (clasa 5-9)','educație liceală (clasa 9-12)','educație superioară (universitate, masterat etc.)'])
d[col[10]] = st.selectbox('Nivelul de educație al tatălui', options=[" ",'educație primară (clasa 1-4)','educație gimnazială (clasa 5-9)','educație liceală (clasa 9-12)','educație superioară (universitate, masterat etc.)'])
d[col[11]] = st.selectbox('Ai parte de suport educațional extrașcolar? ', options=[" ",'Da','Nu'])
d[col[12]] = st.selectbox('Locul de muncă al mamei', options=[" ",'profesoară','servicii civile','antreprenor','legat de medicină','șomeră','altceva'])
d[col[13]] = st.selectbox('Locul de muncă al tatălui', options=[" ",'profesor','servicii civile','antreprenor','legat de medicină','șomer','altceva'])
if d[col[13]] == 'profesor':
    d[col[13]] = 'profesoară'
if d[col[13]] == 'șomer':
    d[col[13]] = 'acasă'
if d[col[12]] == 'șomeră':
    d[col[12]] = 'acasă'
d[col[14]] = st.selectbox('Numărul de restanțe la disciplinele școlare', options=[" ",'0','1','2','3+'])
d[col[15]] = st.selectbox('Starea curentă a sănătății (1 - foarte rea, 5 - foarte bună)', options=[" ",1,2,3,4,5])
d[col[16]] = st.number_input('Numărul de absențe de la școală',step=1,min_value=0)
d[col[17]] = st.selectbox('Frecventezi lecții adăugătoare platite la obiectele școlare?', options=[" ",'Nu','Da, 1 obiect','Da, 2 obiecte','Da, 3+ obiecte'])
d[col[18]] = st.selectbox('Consideri să-ți continui studiile la universitate?', options=[" ",'Nu','Da'])
d[col[19]] = st.selectbox('Consumul de alcool (1-deloc, 5-mult)', options=[" ",1,2,3,4,5])
d[col[20]] = d[col[19]]
d[col[21]] = st.selectbox('Statutul părinților', options=[" ",'Trăiesc împreună','Trăiesc separat'])
d[col[21]] = "Trăiesc împreună"
d[col[22]] = st.selectbox('Ai acces la internet acasă?', options=[" ",'Nu','Da'])
d[col[23]] = st.selectbox('Ești într-o relație romantică momentan?', options=[" ",'Nu','Da'])

# verifica daca au fost completate toate intrebarile
filled = True
for i in d.keys():
    if d[i] == ' ':
        filled = False

# butonul "Prezice nota"
button = st.button("Prezice nota")
if button:
    if filled:
        st.text("...................................................................................")
        instances = process2(d)
        pred = predict_json(instances)
        nota = round(pred[0][0], 2)
        if nota >= 10:
            nota = 9.99
        elif nota < 5:
            nota = 5.00
        st.header('Viitoarea ta notă este '+str(nota))
    else:
        st.text("Nu ai completat toate întrebările")