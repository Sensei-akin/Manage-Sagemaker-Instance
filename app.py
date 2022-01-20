#!/usr/bin/python3

import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

# data
natophonetics = {"A":"Alpha","B":"Bravo","C":"Charlie","D":"Delta","E":"Echo","F":"Foxtrot",\
    "G":"Golf","H":"Hotel","I":"India","J":"Juliett","K":"Kilo","L":"Lima","M":"Mike",\
    "N":"November","O":"Oscar","P":"Papa","Q":"Quebec","R":"Romeo","S":"Sierra",\
    "T":"Tango","U":"Uniform","V":"Victor","W":"Whiskey","X":"X-Ray","Y":"Yankee","Z":"Zulu"}
leet_dict = {'a': '4','b': 'l3', 'c': '(', 'd': '[)', 'e': '3', 'l': '1', 's': '5', 't': '+',\
    'w': '\\/\\/', 'o': '0'}
leet_dict_gk = {'a': 'α', 'b': 'β', 'g': 'γ', 'd': 'δ', 'e': 'ε', 'z': 'ζ', 'h': 'η', 'th': 'θ',\
     'i': 'ι','k': 'κ', 'l': 'λ', 'm': 'μ', 'n': 'ν', 'x': 'ξ', 'o': 'ω', 'p': 'π', 'r': 'ρ', \
    't': 'τ', 'u': 'υ', 'ph': 'φ', 'ch': 'χ', 'ps': 'ψ', 's': 'σ'}

def leet_converter(term, option='Normal'):
    if option == 'Normal':
        def_dict = leet_dict
    else:
        def_dict = leet_dict_gk
    result= [def_dict.get(i,i) for i in list(term.lower())]
    return ''.join(result)


def get_natophonetics(term):
	result = ' '.join([natophonetics.get(i, i) for i in list(term.upper())])
	return result

# @st.cache(suppress_st_warning=True)
def plot_wordcloud(docx):
    mywordcloud = WordCloud().generate(docx)
    fig = plt.figure(figsize=(20,10))
    plt.imshow(mywordcloud,interpolation='bilinear')
    plt.axis('off')
    st.pyplot(fig)

def main():
    st.title("LeetSpeak App")

    menu = ['Home','About']
    choice = st.sidebar.selectbox('Menu',menu)
    if choice == 'Home':
        col1, col2 = st.columns(2)
        with col1:
            st.info('Leet Converter')
            with st.form(key='leetform',clear_on_submit=True):
                raw_text = st.text_input('Text', placeholder='Enter Text Here')
                conv_choice = st.selectbox('Choice',['Normal','Greek'])
                submit_button = st.form_submit_button(label='Convert')
                
            if submit_button:
                if len(raw_text) != 0:
                    st.info('Results')
                    st.write(f'Original text:  {raw_text}')
                    result = leet_converter(raw_text,conv_choice)
                    st.code(result)

                    with st.expander("Visualiser"):
                        plot_wordcloud(raw_text)
                else:
                    st.warning('No Text was passed')
        with col2:
            st.success('Nato Phonetizer')
            with st.form("mynatoform",clear_on_submit=True):
                raw_text = st.text_area("Your Text")
                submit_button = st.form_submit_button("Phonetize")
            
            if submit_button:
                st.success("Results")
                st.write("Original:: {}".format(raw_text))
                results = get_natophonetics(raw_text)
                st.code(results)
                
                with st.expander("Visualize"):
                    plot_wordcloud(results)
    else:
        st.subheader("About")
        st.text('Letspeak App')

if __name__ == '__main__': 

    main()