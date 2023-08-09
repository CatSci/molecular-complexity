from molecular_complexity import molecular_complexity
import streamlit as st
import pandas as pd

st.title('Molecular Complexity')

smile_input = st.text_input('Enter smile...')

data = {
    'Smile': [],
    'cm*': []
}

submit_btn = st.button('Submit')

if submit_btn:
    for s_input in smile_input.split(','):
        _, cm_star, _ = molecular_complexity(smiles= s_input)
        data['Smile'].append(s_input)
        data['cm*'].append(cm_star)


    df = pd.DataFrame(data= data)
    st.dataframe(df)


