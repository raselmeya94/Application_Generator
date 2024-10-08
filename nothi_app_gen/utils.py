
import google.generativeai as genai
from openai import OpenAI

API_KEY="API Key"
OPENAI_API_KEY="API KEY"
def gemini_api(prompt):
    genai.configure(api_key= API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)

    return response.text


def construct_prompt(question):
    # General instruction for generating an official document based on the question
    return (
        f"অনুগ্রহ করে একটি অফিসিয়াল আবেদন পত্র লিখুন যা প্রশ্নের সাথে সম্পর্কিত। "
        f"প্রশ্ন: {question}. "
        "আবেদন পত্রটি যথাযথভাবে গঠন করা উচিত এবং নিম্নলিখিত বিষয়গুলো অন্তর্ভুক্ত করতে হবে: "
        "দয়া করে একটি পূর্ণাঙ্গ এবং বিস্তারিত আবেদন পত্র প্রদান করুন।"
    )


def openai_api(question):
    prompt = construct_prompt(question)

    client = OpenAI(api_key=OPENAI_API_KEY)

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "তুমি একজন আবেদন পত্র লেখায় পারদর্শী"},
            {
                "role": "user",
                "content": question
            }
        ]
    )
    return completion.choices[0].message.content

from transformers import pipeline

def huggingface_api(question):
    prompt = construct_prompt(question)

    # # Load the Hugging Face pipeline for text generation
    # generator = pipeline("text-generation", model="")
    # # Generate a response
    # response = generator(prompt, max_length=1024, num_return_sequences=1)
    
    # # Return the generated text
    # return response[0]['generated_text'].strip()


    generator = pipeline("text-generation", model="facebook/mbart-large-cc25")

    # Generate text
    generated_text = generator(prompt, max_length=200, num_return_sequences=1)

    # Print the generated text
    print(generated_text[0]['generated_text'])


# def call_claude_api(prompt, max_tokens=100):
#     API_KEY = 'API Key'
#     url = "https://api.anthropic.com/v1/complete"
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": f"Bearer {API_KEY}"
#     }

#     # The data payload for Claude API
#     data = {
#         "model": "claude-1",  # Change this to the Claude model you are using
#         "prompt": prompt,
#         "max_tokens_to_sample": max_tokens,
#         "stop_sequences": ["\n\n"],  # Optional: You can provide stop sequences
#         "temperature": 0.7  # Adjust the creativity of the response
#     }

# import requests
# Claude_API_KEY='API Key'
# def claude_api(question):
#     prompt = construct_prompt(question)
#     import anthropic

#     client = anthropic.Anthropic(
#         # defaults to os.environ.get("ANTHROPIC_API_KEY")
#         api_key=Claude_API_KEY,
#     )
#     message = client.messages.create(
#         model="claude-3-5-sonnet-20240620",
#         max_tokens=1024,
#         messages=[
#             {"role": "user", "content": prompt}
#         ]
#     )
#     return message.content

def get_answer(model_name, question):
    if model_name == 'gemini':
        response = gemini_api(question)
        return response
    elif model_name == 'openai':
        response = openai_api(question)
        return response
    elif model_name == 'huggingface':
        response = huggingface_api(question)
        return response
    elif model_name == 'claude':
        response = claude_api(question)
        return response
