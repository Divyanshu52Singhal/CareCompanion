from flask import Flask, render_template, request, redirect, url_for,flash
from time import sleep
#import google.generativeai as genai
import urllib

app = Flask(__name__)
app.secret_key = "password"
# Set your OpenAI API key
#openai.api_key = ''
api = ''
#genai.configure(api_key=api)


def doctor_find(query):
  generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
  }

  safety_settings = [
    {
      "category": "HARM_CATEGORY_HARASSMENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_HATE_SPEECH",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
      "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
      "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
  ]

  model = genai.GenerativeModel(model_name="gemini-1.0-pro",generation_config=generation_config,safety_settings=safety_settings)
  prompt_parts = [
  "the user input will tell the symptoms he is facing according to that you have to tell the department of doctor he should visit give only one or two word answer",
  "input: pimple and acne",
  "output: dermatologist",
  ]
  prompt_parts.append(f"input: {query}")
  response = model.generate_content(prompt_parts)
  print(response)
  response_text = response.text
  encoded_response = urllib.parse.quote_plus(response_text)
  google_maps_url = f'https://www.google.com/maps/search/{encoded_response}+doctor+near+me/'
  return response_text, google_maps_url


# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat',methods = ['GET','POST'])
def chat():
    if request.method=='POST':
        data=request.form['symptoms']
        if data:
            response_text, google_maps_url = doctor_find(data)
            return render_template('chat.html', response=response_text, google_maps_url=google_maps_url)
    return render_template('chat.html')

@app.route('/bmi',methods= ['GET','POST'])
def bmi():
    if request.method=='POST':
        weight = float(request.form['Weight'])
        height = float(request.form['Height'])
        if weight and height:
            height_in_m = height/100
            bmi_val=round(weight/(height_in_m**2),1)
            status="Obese"
            if bmi_val<18.5:
                status="UnderWeight"
            elif bmi_val<25:
                status="Normal"
            elif bmi_val<40:
                status="OverWeight"
            return render_template('bmi.html', bmi_val=bmi_val, status=status)
    return render_template('bmi.html')
            


if __name__ == '__main__':
    app.run(debug=True)