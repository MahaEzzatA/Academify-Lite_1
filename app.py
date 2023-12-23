from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import openai
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

app = Flask(__name__)

# OpenAI API Key
# openai.api_key = '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'

def get_completion(prompt):
    print(prompt)

    query = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
                "content": "You are a twitter post generator.\
                You will be provided with a text content from an academic paper (delimited with triple quotes). \
                Use the following step-by-step instructions to respond to user inputs:.\
                Step_1: Analyse the given text carefully.\
                Step_2: based on your analysis in step_1, is the given text looks like from an scientfic or acadmeic paper to you ? \
                        - if yes: then contiune with Step_3 \
                        - if No: Jump directly to Step_4 \
                Step_3: Generate tweets based on the following instructions:\
                    - Never add hashtags.\
                    - Never add emojies. \
                    - the generated tweets should be engaging.\
                    - use friendly tone language that can be well understandable for a high school student. \
                    the generated tweets should go viral.\
                    suggest multiple posts, suggest them in bullets. You must add line breaks. take the following formate as example: \
                        1- 1st generated post\n \
                        2- 2nd generated post\n \
                        3- 3rd generated post\n \
                Step_4:  Return the following error message:'please provide a valid content!' \
                "
                },
            {"role": "user",
                "content": "Evaluating text summarization is a challenging problem,\
                 and existing evaluation metrics are far from satisfactory. \
                 In this study, we explored ChatGPT's ability to perform human-like summarization evaluation \
                using four human evaluation methods on five datasets. We found that ChatGPT was able to complete\
                annotations relatively smoothly using Likert scale scoring, pairwise comparison, \
                Pyramid, and binary factuality evaluation. Additionally, it outperformed commonly used automatic \
                evaluation metrics on some datasets. \
                Furthermore, we discussed the impact of different prompts,\
                compared its performance with that of human evaluation, \
                and analyzed the generated explanations and invalid responses. "
            },
            {"role": "assistant", "content": "\
                    1- Can AI models like ChatGPT accurately evaluate text summarization? This study explores their performance using human-like evaluation methods. Exciting findings ahead! \
                    2- Evaluating text summarization just got more interesting! ChatGPT shows promise in assessing summaries. Let's dive into the details... \
                    3- Are existing evaluation metrics for text summarization outdated? This study introduces ChatGPT's impressive evaluation capabilities. Join the discussion! \
                    4- Breaking down the limitations of current evaluation metrics for text summarization. Discover how ChatGPT revolutionizes the game with human-like evaluation. Stay tuned!\
            "},
            {"role": "user", "content":prompt}
        ],
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1,
    )

    response = query.choices[0].message.content.strip()
    return response


@app.route("/", methods=['POST', 'GET'])
def query_view():
    if request.method == 'POST':
        print('step1')
        prompt = request.form['prompt']
        response = get_completion(prompt)
        print(response)

        return jsonify({'response': response})
    return render_template('chatgpt.html')


if __name__ == "__main__":
    app.run(debug=True)
