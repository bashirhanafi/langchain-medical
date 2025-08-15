from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from langchain.chat_models import init_chat_model
from langchain.prompts import PromptTemplate
import os

# init the FastAPI
app = FastAPI()

# API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyCS7BvKO8CcX_MvmpBqsB-SEQyC8N2hqbo"

# init the model with langchain
model = init_chat_model(
    "gemini-2.5-flash", 
    model_provider="google_genai"
)

# class of patient
class PatientInfo(BaseModel):
    gender: str
    age: int
    symptoms: List[str]

# prompt template
template = """
Anda adalah sistem rekomendasi departement rumah sakit.
Berdasarkan informasi berikut:
- gender: {gender}
- age: {age}
- symptoms: {symptoms}
Tentukan departemen medis yang paling tepat untuk pasien ini.
Jawab hanya dengan **nama departemen spesialisasi internasional** (contoh: Neurology, Cardiology, Gastroenterology), 
jangan gunakan istilah umum atau dalam bahasa Indonesia seperti 'Penyakit Dalam'.
"""

prompt = PromptTemplate(
    input_variables = ['gender', 'age', 'symptoms'],
    template = template
)

# endpoint for recommend department
@app.post('/recommend')
def recommend_department(patient: PatientInfo):
    symptoms_str = ", ".join(patient.symptoms)

    final_prompt = prompt.format(
        gender = patient.gender,
        age = patient.age,
        symptoms = symptoms_str
    )

    response = model.invoke(final_prompt)

    return {
        "recommended_department": response.content
    }


