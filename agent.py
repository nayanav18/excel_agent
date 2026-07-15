from google import genai

PROJECT_ID = "vf-grp-gbissdbx-dev-1"
LOCATION = "europe-west1"
MODEL = "gemini-2.5-flash"

client = genai.Client(
    vertexai= True,
    project =PROJECT_ID,
    location =LOCATION
)

def ask_gemini(prompt):


    """Connects to Google's Gemini AI model.
Creates a client object that knows how to talk to Gemini.
Defines a function called ask_gemini().
Sends a prompt (question) to Gemini.
Returns Gemini's answer."""

def generate_pandas_code(question, columns):
 
    prompt = f"""
You are a Pandas expert.
 
DataFrame name is df.
 
Available Columns:
{', '.join(columns)}
 
User Question:
{question}
 
Return ONLY executable pandas code.
 
Do not explain.
 
Do not use markdown.
 
Return one line only.
"""
 
    response = client.models.generate_content(
        model=MODEL,
        contents=prompt
    )
 
    return response.text.strip()