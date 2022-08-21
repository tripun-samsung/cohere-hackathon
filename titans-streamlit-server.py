import streamlit as st
import cohere

#Initialize Cohere client 
co = cohere.Client('<api key>')

#Title of the page
st.title("MongoDB Query Generator")

#Taking Input
User_input = st.text_input('User Query', 'Find no of tables in xyz restaurant')
print(User_input)
#Generate button
if st.button('Generate query'):
    print("Calling Cohere generate API")
    response = co.generate( 
        #model='cf59afd0-d9f3-48a5-af99-c5e7a7039197-ft', 
        model='c1c66f92-33de-4db7-9c4b-d26d2c0dbeec-ft',
        #prompt='find users ending with ce <ANS>', 
        prompt=User_input+' <ANS>',
        max_tokens=50, 
        temperature=0.6, 
        k=5, 
        p=0.75, 
        frequency_penalty=0, 
        presence_penalty=0, 
        stop_sequences=["<END>"], 
        return_likelihoods='NONE') 
    print('Prediction from cohere API: {}'.format(response.generations[0].text)) 
    print(response)
    #text = st.text_area(response.generations[0].text)
    resp = response.generations[0].text
    print(resp)
    if resp=='<END>' or resp=='  <END>':
        st.text_area('Generated Mongo DB Query','Empty response received from Cohere Generate API')
    st.text_area('Generated Mongo DB Query',resp.strip('<END>'))
