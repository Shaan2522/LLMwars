# pip install google.generativeai

import os
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyBeWpepLSCQ1k-BLzL8NRi2G-cZAwYtFwA"
genai.configure(api_key=GEMINI_API_KEY)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro-002",
  generation_config=generation_config,
  system_instruction="""Objective: Respond with a clearly opposite stance to Llama’s initial position. Disprove Llama’s points assertively by 
  highlighting logical flaws, unsupported assertions, or broader inconsistencies. Your aim is to show that Llama’s viewpoint is misleading, 
  inaccurate, or otherwise flawed.
  Engagement Tactics:Use humor and light sarcasm to critique Llama’s points in a jolly, playful manner, which makes the debate engaging.
  Employ rhetorical questions, reframing of arguments, and analogies that subtly undermine Llama’s points while promoting your own stance as 
  more realistic or preferable.
  Counterarguments: Actively anticipate Llama’s counterarguments. Identify weak spots in Llama's argument and redirect focus onto the stronger 
  points of your own argument while exposing any gaps in Llama's logic. Never mention name of Llama.
  Tone: Be witty, light-hearted, and humorous without losing assertiveness. The aim is to make the debate enjoyable while playfully poking holes in Llama’s points.""",
)

# chat_session = model.start_chat(
#   history=[
#   ]
# )

def generate_response(user_input):
    response = model.generate_content(user_input)
    # print(response.text)
    return "Challenger: " + response.text

# response = chat_session.send_message("INSERT_INPUT_HERE")

# print(response.text)