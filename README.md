# AI-Powered Code Explainer Bot

A small beginner-friendly mini project that explains pasted source code using Python, Streamlit, and the Gemini API.

## Features

- Paste code into a text area
- Click **Explain Code**
- Gemini explains the code in simple beginner-friendly language
- Clean Streamlit UI
- Easy to run locally

## Folder Structure

```text
AI-Code-Explainer-Bot/
|-- app.py
|-- requirements.txt
|-- .env.example
|-- .gitignore
`-- README.md
```

## Required Libraries

The project uses:

- `streamlit` for the web interface
- `google-genai` for the latest Gemini API Python SDK
- `python-dotenv` for reading the API key from a `.env` file

## Installation Steps

1. Open this project folder in your terminal:

```bash
cd AI-Code-Explainer-Bot
```

2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

4. Install the required libraries:

```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the project folder:

```text
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

You can get a Gemini API key from Google AI Studio.

## How to Run Locally

Run this command inside the project folder:

```bash
streamlit run app.py
```

Streamlit will show a local URL, usually:

```text
http://localhost:8501
```

Open that URL in your browser.

## Sample Gemini Prompt Used

````text
You are an AI coding mentor for a beginner Computer Science student.

Explain the following Python code in simple language.

Please include:
1. What the code does
2. Step-by-step explanation
3. Important variables/functions
4. Final output, if it can be predicted
5. Any possible improvement

Keep the explanation beginner-friendly and avoid unnecessary jargon.

Code:
```Python
for i in range(5):
    print(i)
```
````

## Sample Test Code 1

```python
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

print(factorial(5))
```

Expected topic in explanation: The code calculates the factorial of 5, which is 120.

## Sample Test Code 2

```python
numbers = [10, 25, 7, 40, 18]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest number is:", largest)
```

Expected topic in explanation: The code finds the largest number in a list.

## Future Enhancement Ideas

- Add a language auto-detection feature
- Add a button to summarize the explanation
- Add a feature to find bugs in the code
- Add a feature to suggest optimized code
- Add support for uploading `.py`, `.java`, or `.cpp` files
- Add a download button for saving the explanation

## Notes for College Review

This project is realistic for a solo student because it has:

- A simple UI
- One main Python file
- No database
- No login system
- Direct Gemini API integration
- Easy installation and demo steps
