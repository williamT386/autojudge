from openai import OpenAI
import numpy as np
client = OpenAI()

def solve_frq(question):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Your goal is to solve this difficult free response question."},
            {"role": "user", "content": "Please solve this difficult free response question, showing your work: " + question}
        ]
    )
    return completion