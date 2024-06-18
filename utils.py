import pathlib
import textwrap
import json

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
import os

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

def get_credentials():
    if os.getenv("GOOGLE_API_KEY"):
        return os.getenv("GOOGLE_API_KEY")
 
# print(get_credentials())
##########################################################
genai.configure(api_key=get_credentials())

model = genai.GenerativeModel('gemini-1.0-pro-latest')

# models/gemini-1.0-pro
# models/gemini-1.0-pro-001
# models/gemini-1.0-pro-latest
# models/gemini-1.0-pro-vision-latest
# models/gemini-1.5-flash
# models/gemini-1.5-flash-001
# models/gemini-1.5-flash-latest
# models/gemini-1.5-pro
# models/gemini-1.5-pro-001
# models/gemini-1.5-pro-latest
# models/gemini-pro
# models/gemini-pro-vision

# context = 'Quiero que seas un esxperto en concina argentina. Necesito que me suguieras recetas no muy caras y de fácil preparación. EN breve te voy a pedir que me enseñes a preparar, devolvela en formato Json.'
# prompt = input('dime en una sola oración, que comida quieres aprender a cocinar: ')

def consulta(context,prompt):
  response = model.generate_content(context + prompt)
  archivo = response.text
  with open("archivo.txt", "w") as f:
    f.write(archivo)

  return display(response.text)


def archivado(context,prompt):
    response = model.generate_content(context + prompt)
  
    json_response = response.text.replace('```json', '').replace('```', '').replace('\'', '"').replace('\n', '')

    with open("respuesta.json", "w") as f:
        f.write(json_response.strip('"'))
        #json.dump(response.text.strip('"'), f)

    display(json_response)






# for m in genai.list_models():
#     if 'generateContent' in m.supported_generation_methods:
#         print(m.name)