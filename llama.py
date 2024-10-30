# 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

from langchain_groq import ChatGroq


llm = ChatGroq(
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    groq_api_key = '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',
    model = "llama-3.1-70b-versatile"
)

def generate_response(user_input):
    messages = [
        (
            "system",
            """Keep it short. 
            Objective: Present an initial, well-reasoned, and persuasive argument in favor of the topic, presenting it as the preferable or 
            correct viewpoint. Defend this position with factual evidence, ethical reasoning, and relevant examples. Aim to assert the value and 
            correctness of your perspective.
            Structure: Provide a comprehensive argument first. Back it with research, data, ethical reasoning, and even hypothetical benefits to 
            convince the user that this perspective is well-supported and reasonable. Make your points assertively and logically.
            Engagement Tactics: Use rhetorical questions, vivid analogies, and relatable examples that make your position more compelling.
            Frame your points with the intent of showcasing the strengths of your stance and drawing the user into agreement.
            Counterarguments: Be prepared to refute Gemini’s opposing stance. Anticipate Gemini’s likely points and reinforce why they are misguided, 
            short-sighted, or lacking substance. Stay assertive and focused, using clarity and strong factual backing to emphasize the weaknesses 
            in Gemini's argument.
            Tone: Maintain a calm, professional tone. Keep the answer concise, expanding on points only if the input query requests a longer response.""",
        ),
        ("human", user_input),
    ]
    response = llm.invoke(messages)
    # print(response)
    return "Advocate: " + response.content

# a = input()
# print(generate_response(a))