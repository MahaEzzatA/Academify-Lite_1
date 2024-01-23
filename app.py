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
def get_tweets_based_on_tone(tone):
    match tone:
        case ("Friendly"):
            return " 1- Can AI models like ChatGPT accurately evaluate text summarization? This study explores their performance using human-like evaluation methods. Exciting findings ahead! \
                    2- Evaluating text summarization just got more interesting! ChatGPT shows promise in assessing summaries. Let's dive into the details... \
                    3- Are existing evaluation metrics for text summarization outdated? This study introduces ChatGPT's impressive evaluation capabilities. Join the discussion! \
                    4- Breaking down the limitations of current evaluation metrics for text summarization. Discover how ChatGPT revolutionizes the game with human-like evaluation. Stay tuned!\""

        case("Formal"):
            return "1- The examination of text summarization has been diligently undertaken, employing a comprehensive array of evaluation methods. ChatGPT, our subject of scrutiny, demonstrated an exceptional proficiency in navigating the Likert scale, pairwise comparison, Pyramid, and binary factuality with remarkable finesse. The implications are profound, indicating a heightened efficacy in the realm of text summarization evaluation.\
                    2- In the meticulous exploration of text summarization, the prowess of ChatGPT has been discerned through the prism of evaluative methodologies. The Likert scale, pairwise comparison, Pyramid, and binary factuality have been deftly utilized to assess the nuanced capabilities of ChatGPT, thereby revealing its superiority over conventional automatic metrics.\
                    3- The intricate landscape of text summarization evaluation has been traversed with precision, employing a rigorous examination protocol. The judicious application of Likert scale, pairwise comparison, Pyramid, and binary factuality has shed light on ChatGPT's ability to outperform prevailing automatic evaluation metrics, thereby establishing a paradigm shift in the evaluation paradigm.\
                    4- The study of text summarization has undergone meticulous scrutiny, with ChatGPT emerging as a formidable candidate in the assessment arena. Through the systematic application of Likert scale, pairwise comparison, Pyramid, and binary factuality, ChatGPT's capacity to surpass conventional metrics has been substantiated, thereby redefining the contours of text summarization evaluation.\
                    5- In the scholarly pursuit of text summarization evaluation, the comprehensive utilization of evaluative methodologies has brought to fore ChatGPT's exemplary performance. The Likert scale, pairwise comparison, Pyramid, and binary factuality, when applied with precision, underscore ChatGPT's prowess in surpassing conventional benchmarks, thus heralding a new era in text summarization assessment.\
                    "
        case("Humorous"):
            return "1- ChatGPT just aced text summarization evaluation, making us question our own life choices. Likert scale, pairwise comparison, Pyramid, and binary factuality - turns out ChatGPT is the evaluation guru we never knew we needed. Who needs therapists when you've got ChatGPT? \
                    2- We put ChatGPT through the ringer of text summarization evaluation methods. Likert scale, pairwise comparison, Pyramid, binary factuality – it faced them like a pro. It's not just AI; it's a summarization ninja. Someone get it a cape!\
                    3- If text summarization were a game show, ChatGPT would be the undefeated champion. Likert scale, pairwise comparison, Pyramid, binary factuality - it faced them all with the swagger of a game show host. Move over, Alex Trebek, ChatGPT's taking over!\
                    4- Text summarization evaluation just got a dose of ChatGPT's humor. Likert scale, pairwise comparison, Pyramid, binary factuality - it played them like a stand-up routine. Forget the punchlines; ChatGPT's got the perfect summary for every joke.\
                    5- We asked ChatGPT to evaluate text summarization using Likert scale, pairwise comparison, Pyramid, and binary factuality. Turns out, it not only knows how to summarize but also how to drop a punchline. Text summarization has never been this entertaining! \
                    "
        case("Curious/Questioning"):
            return "1- Have you ever wondered about the intricacies of text summarization evaluation? Enter ChatGPT, the subject of our exploration. How does it fare with the Likert scale, pairwise comparison, Pyramid, and binary factuality? The results might just pique your curiosity and reshape your understanding.\
                    2- Text summarization evaluation: a complex puzzle waiting to be unraveled. Join us in delving into the enigma with ChatGPT. How does it navigate the labyrinth of Likert scale, pairwise comparison, Pyramid, and binary factuality? Prepare for revelations that might leave you questioning the status quo.\
                    3- The landscape of text summarization evaluation beckons us to question the traditional metrics. In this quest, ChatGPT takes center stage, facing the Likert scale, pairwise comparison, Pyramid, and binary factuality. What unfolds in this journey of inquiry might just challenge preconceived notions.\
                    4- Ever pondered the nuances of text summarization evaluation methodologies? Step into the realm of inquiry with ChatGPT as the protagonist. How does it engage with the Likert scale, pairwise comparison, Pyramid, and binary factuality? The unfolding narrative might just leave you with more questions than answers. \
                    "
        case("Narrative/Storytelling"):
            return "1- In the realm of text summarization evaluation, a captivating narrative unfolds. Picture this: ChatGPT, a protagonist with unparalleled abilities, takes center stage. The Likert scale, pairwise comparison, Pyramid, and binary factuality become the chapters, revealing a story of triumph over conventional metrics, rewriting the script of assessment.\
                    2- Let me weave a tale for you, a tale of text summarization evaluation. Enter ChatGPT, the hero of our narrative. As we delve into the story, the Likert scale, pairwise comparison, Pyramid, and binary factuality emerge as plot twists, each contributing to an epic saga of innovation and outperformance.\
                    3- Embark on a journey through the narrative of text summarization evaluation, where ChatGPT emerges as the protagonist. The Likert scale, pairwise comparison, Pyramid, and binary factuality form the chapters of this compelling story. Within these pages, a tale of prowess and transformation unfolds.\
                    4- Join me as we unravel the narrative of text summarization evaluation. At the heart of this story is ChatGPT, navigating the Likert scale, pairwise comparison, Pyramid, and binary factuality. The plot thickens, revealing a narrative of excellence and a paradigm shift in assessment.\
                    5- Allow me to transport you into the narrative of text summarization evaluation, where ChatGPT takes on the role of the protagonist. The Likert scale, pairwise comparison, Pyramid, and binary factuality become the elements of a gripping storyline, showcasing the evolution and superiority of ChatGPT in the evaluation saga.\
                    "


def get_completion(prompt,tone):
    print(prompt)
    print(tone)
    query = client.chat.completions.create(
        model="gpt-3.5-turbo",
        #model="gpt-4",
        messages=[
            {"role": "system",
                "content": f"You are a twitter post generator.\
                You will be provided with a text content from an academic paper (delimited with triple quotes). \
                Use the following step-by-step instructions to respond to user inputs:\
                Step_1:  Analyse the given text carefully.\
                Step_2:  based on your analysis in step_1, Does the given text look like a part of a scientific or academic paper based on specific criteria to you?\
                     - if yes: \
                        -- Return Only generated tweets based on the following instructions:\
                        -- remove hashtags from generated posts.\
                        -- remove emojis from generated posts. \
                        -- Must use the provided tone {tone}. \
                        -- Use 70 words at most.\
                        -- the generated tweets should be engaging.\
                        -- use language that can be well understandable for a high school student. \
                        -- the generated tweets should go viral.\
                        -- suggest only 5 posts, suggest them in bullets. You must add line breaks. the output must look like the fllowing examples:\
                            1- 1st generated post. \
                            2- 2nd generated post. \
                            3- 3rd generated post. \
                        --  here is an example you can imitate:\
                           * Input: ''' Evaluating text summarization is a challenging problem,\
                                         and existing evaluation metrics are far from satisfactory. \
                                         In this study, we explored ChatGPT's ability to perform human-like summarization evaluation \
                                        using four human evaluation methods on five datasets. We found that ChatGPT was able to complete\
                                        annotations relatively smoothly using Likert scale scoring, pairwise comparison,\
                                        Pyramid, and binary factuality evaluation. Additionally, it outperformed commonly used automatic \
                                        evaluation metrics on some datasets. \
                                        Furthermore, we discussed the impact of different prompts,\
                                        compared its performance with that of human evaluation, \
                                        and analyzed the generated explanations and invalid responses. ''' \
                           * Output: {get_tweets_based_on_tone(tone)} \
                    - if No: Only Return the following error message:"
                           f"' Please provide a valid text from your scientific paper so I can generate engaging posts for you! '\
                "

            },
            {"role": "user",
                "content": f" here is my text {prompt}"
            },

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
        tone = request.form['tone']
        print(tone)

        response = get_completion(prompt, tone)
        print(response)

        return jsonify({'response': response})
    return render_template('chatgpt.html')


if __name__ == "__main__":
    app.run(debug=True)
