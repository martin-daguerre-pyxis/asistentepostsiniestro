from openai import OpenAI
import streamlit as st

# Page title
st.set_page_config(page_title='Asistente ante siniestros de transito', page_icon='🚗')
st.title('Asistente ante siniestros de transito')

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    api_key=api_key
)

st.write(response.choices[0].text)


st.write('¡Bienvenido a Asistente Post-Siniestro!\n\nEstamos aquí para ayudarte a navegar por los momentos difíciles después de un siniestro de tránsito. Nuestra IA está lista para brindarte información clara y asistencia personalizada. Comienza por indiicarnos algunos datos y te guiaremos en cada paso del camino.')
st.markdown('**IMPORTANTE**')

st.warning('Esta aplicación se encuentra en fase de pruebas y no tiene que ser usada como un sustituto de un profesional en el area de seguros o de transito. Por favor, no tome decisiones basadas en los resultados de esta aplicación.')
