import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

response = model.generate_content(
    "Build a CRM with login, dashboard and contacts. Return only JSON."
)

print(response.text)