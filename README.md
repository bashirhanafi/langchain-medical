# Medical Department Recommendation API

A minimal FastAPI service that recommends the most appropriate medical department based on patient information. This service uses a **Gemini** via **LangChain** to generate department recommendations.

## Requirements

- Python 3.10+
- `pip` installed

## Installation

1. **Clone this repository**
```bash
git clone https://github.com/bashirhanafi/langchain-medical.git
cd langchain_medical

```
2. **Install Requirements**
```bash
pip install -r requirements.txt

```
3. **Running the API**
```bash
uvicorn main:app --reload
```
The API will available at 
```
http://127.0.0.1:8000

```

## API endpoint
`POST /recommend`

### Request body
```json
{
    "gender": "female",
    "age": 62,
    "symptoms": ["pusing", "mual", "sulit berjalan"]
}
```

### Response example
```json
{
    "recommended_department": "Neurology"
}
```




