from openai import OpenAI
import numpy as np
client = OpenAI()

def convert_mcq_to_frq(question, options):
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Your goal is to convert this multiple choice question to an open-ended free-response question."},
            {"role": "user", "content": "Please convert this multiple choice question to an open-ended free-response question. Your given question is " + question + " The possible answers are " + np.array2string(options)}
        ]
    )
    return completion