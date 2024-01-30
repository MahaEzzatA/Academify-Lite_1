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

def get_example(example):
    match example:
        case("example_1"):
            return " The ongoing COVID-19 corona virus outbreak has caused a global disaster with its deadly spreading.\
                     Due to the absence of effective remedial agents and the shortage of immunizations against the virus, population vulnerability increases.\
                     In the current situation, as there are no vaccines available;\
                     therefore, social distancing is thought to be an adequate precaution (norm) against the spread of the pandemic virus. \
                     The risks of virus spread can be minimized by avoiding physical contact among people. \
                     The purpose of this work is, therefore, to provide a deep learning platform for social distance tracking using an overhead perspective. \
                     The framework uses the YOLOv3 object recognition paradigm to identify humans in video sequences. \
                     The transfer learning methodology is also implemented to increase the accuracy of the model. \
                     In this way, the detection algorithm uses a pre-trained algorithm that is connected to an extra trained layer using an overhead human data set.\
                     The detection model identifies peoples using detected bounding box information. \
                     Using the Euclidean distance, the detected bounding box centroid's pairwise distances of people are determined. \
                     To estimate social distance violations between people, we used an approximation of physical distance to pixel and set a threshold. \
                     A violation threshold is established to evaluate whether or not the distance value breaches the minimum social distance threshold.\
                     In addition, a tracking algorithm is used to detect individuals in video sequences such that the person who violates/crosses\
                     the social distance threshold is also being tracked. Experiments are carried out on different video sequences to test the efficiency of the model.\
                     Findings indicate that the developed framework successfully distinguishes individuals who walk too near and breaches/violates \
                     social distances; also, the transfer learning approach boosts the overall efficiency of the model. \
                     The accuracy of 92% and 98% achieved by the detection model without and with transfer learning, respectively.\
                     The tracking accuracy of the model is 95%.\
                    "
        case("example_2"):
            return "In this paper, we show that Virtual Reality(VR) sickness is associated \
                    with a reduction in attention, which was detected with the P3b Event-Related Potential (ERP) component \
                    from electroencephalography (EEG) measurements collected in a dual-task paradigm.We hypothesized \
                    that sickness symptoms such as nausea, eyestrain, and fatigue would reduce the users' capacity \
                    to pay attention to tasks completed in a virtual environment, and that this reduction in attention \
                    would be dynamically reflected in a decrease of the P3b amplitude while VR sickness was experienced.\
                    In a user study, participants were taken on a tour through a museum in VR along paths with varying amounts of rotation,\
                    shown previously to cause different levels of VR sickness. While paying attention to the virtual museum (the primary task),\
                    participants were asked to silently count tones of a different frequency (the secondary task).\
                    Control measurements for comparison against the VR sickness conditions were taken when the users were not wearing \
                    the Head-Mounted Display (HMD) and while they were immersed in VR but not moving through the environment.\
                    This exploratory study shows, across multiple analyses, that the effect mean amplitude of the P3b collected during\
                    the task is associated with both sickness severity measured after the task with a questionnaire (SSQ) \
                    and with the number of counting errors on the secondary task. Thus, VR sickness may impair attention\
                    and task performance, and these changes in attention can be tracked with ERP measures as they happen,\
                    without asking participants to assess their sickness symptoms in the moment.\
                    "
def get_tweets_based_on_tone(example,tone):
    match example:
        case("example_1"):
            match tone:
                case ("Friendly"):
                    return " 1- Hey there! Dealing with the whole COVID chaos? Our study dives into a solution with a friendly twist. Picture this: a deep learning guru, YOLOv3, and a dash of transfer learning, creating a model that spots social distancing rebels with 98% accuracy. Stay safe, keep your distance, and enjoy the read!\
                             2- Navigating the pandemic blues? We've got a tech-savvy sidekick! Meet our deep learning model, a mix of YOLOv3 and transfer learning, hitting the 98% accuracy mark. It's like having a virtual social distancing superhero! Grab your popcorn, stay socially distant, and enjoy the ride!\
                             3- Greetings in the name of social distance! Our study brings a bit of tech magic to the COVID-19 scene. Imagine YOLOv3 and transfer learning teaming up to create a superhero model. Spoiler alert: It hits a whopping 98% accuracy! Keep your distance, and let the good times (and science)\ roll!\
                             4- Hey, pandemic pals! Looking for a tech-driven solution? Our study introduces the dynamic duo: YOLOv3 and transfer learning. Together, they cook up a model with a cool 98% accuracy, spotting social distancing rebels. So, stay chill, keep your space, and enjoy the journey with us!\
                             5- Hello, fellow social distancers! Ready for some tech talk? Our study unveils the magic of YOLOv3 and transfer learning, creating a model with a 98% accuracy charm. It's like having a digital distance assistant! Stay safe, keep smiling, and dive into the world of social distancing tech with us!\
                            "
                case("Formal"):
                    print("forrrmaaal")
                    return "1- The ongoing global crisis spurred by the COVID-19 pandemic necessitates serious measures. Our study addresses this by proposing a deep learning platform for social distance tracking. Leveraging YOLOv3 and transfer learning, the model achieves a commendable 98% accuracy in detecting and tracking individuals who violate social distancing norms.\
                            2- In response to the pressing challenges posed by the COVID-19 pandemic, our study introduces a robust solution. Employing YOLOv3 and transfer learning, our deep learning platform attains an impressive accuracy rate of 98% in identifying and tracking individuals who breach established social distancing thresholds.\
                            3- Amid the profound impact of the COVID-19 pandemic, our research contributes to mitigating the spread through advanced technology. Utilizing YOLOv3 and transfer learning, our model, boasting a 98% accuracy, effectively identifies and tracks individuals violating social distancing norms.\
                            4- Addressing the critical need for effective pandemic management, our study presents a technological approach. By harnessing YOLOv3 and transfer learning, our model achieves a substantial 98% accuracy in detecting and tracking individuals who fail to adhere to prescribed social distancing measures.\
                            5- In the face of the ongoing global health crisis, our research endeavors to provide a comprehensive solution. Through the application of YOLOv3 and transfer learning, our model exhibits a commendable 98% accuracy, proficiently identifying and tracking individuals breaching social distancing guidelines.\
                            "
                case("Humorous"):
                    print("hahaha")
                    return "1- Our AI takes social distancing seriously, and it's not afraid to make it fun! Using YOLOv3, it's like having a superhero for detecting social distance violations. Who said tech can't be your pandemic buddy?\
                            2- Breaking the social distance record like a pro! Our AI uses YOLOv3 and transfer learning to keep you safe and entertained. With a 98% accuracy rate, it's practically a social distance wizard.\
                            3- When pandemic problems meet AI solutions – cue the laughter track! Our study uses YOLOv3, transfer learning, and a pinch of humor to track social distance. It's not just tech; it's your hilarious health companion.\
                            4- Get ready for a dose of COVID comedy! Our AI study, armed with YOLOv3 and transfer learning, isn't just about social distance tracking; it's a full-on tech stand-up. Warning: May cause laughter outbreaks!\
                            5- Social distance, but make it funny! Our AI, fueled by YOLOv3 and transfer learning, turns pandemic precautions into a comedy show. With a 95% tracking accuracy, it's the tech genius you never knew you needed. \
                            "
                case("Curious/Questioning"):
                    return "1- Intrigued by the realm of social distancing technology? Our study delves into the intricacies! YOLOv3, transfer learning, and a touch of curiosity form the backbone of a model boasting 98% accuracy. Eager to comprehend the technical marvel? Embark on this journey with us.\
                            2-Curious minds, rejoice! Ever questioned the inner workings of social distancing tracking? YOLOv3, transfer learning, and a commitment to curiosity birthed a model with 98% accuracy. Ready to unravel the scientific puzzle? Join us on this formal yet inquisitive exploration.\
                            3- Questioning the status quo of social distancing methods? We were too. Dive into our study to unravel the mysteries! YOLOv3, transfer learning, and a dash of curiosity contribute to a model achieving 98% accuracy. Want to comprehend the technicalities? Join our formal discourse.\
                            4- Ever had a formal curiosity about how technology intersects with social distancing? Our study unveils the answers! YOLOv3, transfer learning, and a smattering of curiosity combine to deliver a model boasting 98% accuracy. Ready for a deep dive into the formal intricacies? Join us!\
                            5- Formal inquiry meets technological innovation in our study on social distancing tracking. YOLOv3, transfer learning, and an air of curiosity collectively build a model with 98% accuracy. Eager to navigate the formal landscape of this tech-driven exploration? Join us on this quest!\
                            "
                case("Narrative/Storytelling"):
                    return " 1- Embark on a journey into the heart of our study, where the battle against COVID-19 takes on a digital twist. Picture YOLOv3, transfer learning, and a sprinkle of curiosity shaping a hero – our model with a mighty 98% accuracy. The story unfolds in the pixels of social distancing. Ready for the narrative?\
                            2- In the vast landscape of pandemic challenges, our study introduces a protagonist – a model crafted with YOLOv3, transfer learning, and a curious spirit. Watch as the story of social distancing unfolds in high accuracy, reaching a climax of 98%. This is more than a study; it's a narrative waiting to be explored.\
                            3- Once upon a time in the realm of social distancing, YOLOv3 and transfer learning joined forces, driven by an insatiable curiosity. The result? A model with 98% accuracy, weaving a compelling tale of technology and human distance. Are you ready to immerse yourself in this narrative of innovation?\
                            4- In the story of combating COVID-19, our study introduces a protagonist – a model shaped by YOLOv3, transfer learning, and a quest for understanding. With 98% accuracy, this narrative unfolds in pixels, capturing the essence of social distancing. Join us as we unveil the chapters of technological storytelling.\
                            5- Enter the narrative of our study, where technology becomes a protagonist in the fight against the pandemic. YOLOv3, transfer learning, and a curious journey bring forth a model boasting 98% accuracy. Immerse yourself in the pixels that tell the story of social distancing. Ready to explore this technological narrative?\
                             "
        case("example_2"):
            match tone:
                case("Friendly"):
                    return "1- Delving into the world of Virtual Reality! Our latest research explores the link between VR sickness and attention reduction using EEG. Discover how symptoms like nausea impact task performance in virtual environments. Exciting findings on the correlation between P3b amplitude and sickness severity.\
                            2- Unlocking the secrets of VR sickness! Our study reveals fascinating insights into how symptoms like nausea affect attention during virtual experiences. The P3b ERP component sheds light on dynamic changes in attention levels. Dive into the details of our user study exploring museum tours in VR.\
                            3- Did you know VR sickness can impact attention? Our research proves it! Dive into the details of our user study exploring museum tours in virtual reality. Discover the correlation between P3b amplitude and sickness severity. Exciting steps forward in understanding the dynamics of VR experiences.\
                            4- Exploring the mind-bending world of Virtual Reality! Our latest research connects the dots between VR sickness and attention reduction using cutting-edge EEG measurements. Uncover the impact of symptoms like nausea on task performance in immersive environments. Dive into our user study for eye-opening revelations!\
                            5- Journey into the realm of VR with our groundbreaking research! Discover how VR sickness influences attention and task performance through EEG insights. Uncover the correlation between P3b amplitude and sickness severity in this fascinating exploration of virtual experiences.\
                            "
                case ("Formal"):
                    print("forrrmaaal_2")
                    return "1- Unraveling the intricate relationship between VR sickness and attention modulation through P3b ERP components. Our study employs EEG measurements in a dual-task paradigm, unveiling how symptoms like nausea and eyestrain impact users' capacity to focus in virtual environments. Explore the nuanced dance of attention and VR sickness without the distractions of hashtags or emojis. A scientific journey into the depths of immersive experiences.\
                            2- Embark on a profound exploration of VR sickness's impact on attention, as revealed by P3b ERP components in our latest study. Navigate the complexities of symptoms like fatigue and eyestrain, and their dynamic interplay with users' task performance in virtual environments. Join us for an engaging odyssey, where scientific rigor meets the immersive world of Virtual Reality. No hashtags or emojis, just pure scientific insight.\
                            3- Discover the fascinating dynamics between VR sickness severity and attention levels through the lens of P3b ERP components. Our study, conducted in a dual-task paradigm, showcases the intricate dance of symptoms like nausea and fatigue with users' focus during virtual experiences. Immerse yourself in a world of scientific revelations, where every detail counts. No hashtags or emojis, just a concise journey into the heart of VR research.\
                            4- Unveil the secrets of attention modulation in the face of VR sickness symptoms with our latest study. Using P3b ERP components, we decode how nausea, eyestrain, and fatigue influence users' capacity to focus in virtual environments. Engage in a scientific expedition where each revelation adds depth to our understanding of immersive experiences. No hashtags or emojis, just the pure essence of VR research.\
                            5- Join us on a scientific odyssey into the heart of Virtual Reality as we explore the impact of VR sickness on attention. Through P3b ERP components, we decipher the intricate dance of symptoms like nausea and fatigue, providing a deeper understanding of users' focus in virtual environments. No hashtags or emojis, just a concise and informative journey into the world of VR research.\
                            "
                case ("Humorous"):
                    print("hahaha_2")
                    return "1- Considering a virtual reality adventure? Hold on tight! Our research reveals VR sickness is like a surprise comedy show for your attention span. Nausea and eyestrain play unexpected comedians in your VR experience. Get the scoop on our study for a laugh-out-loud journey into the world of attention-hijinks in VR.\
                            2- Strap in for the ultimate virtual rollercoaster – and we're not just talking about your stomach! Our latest research dives into the hilarious connection between VR sickness and attention spans. Spoiler alert: Nausea and eyestrain are the uninvited guests stealing the spotlight in your VR comedy club.\
                            3- Ever felt like your VR headset was plotting against you? Our study spills the beans on VR sickness, turning your attention into a stand-up comedy show. Nausea and eyestrain? They're the surprise headliners you never knew you needed for a side-splitting virtual adventure.\
                            4- Thinking of tackling VR with a hangover? Think again! Our research says, (Not so fast!) VR sickness is the ultimate hangover cure – distracting you from everything, even questionable life choices. Dive into our study for a laugh and a lesson: VR and nausea might not mix well, but the results are comedy gold!\
                            5- Multitasking in VR is like juggling with a virtual twist – nausea, eyestrain, and fatigue are the circus performers stealing the show in your attention arena! Our study unveils the behind-the-scenes hilarity of attempting to focus on tasks while the virtual circus is in town. Spoiler alert: It's a sidesplitting spectacle!\
                            "
                case ("Curious/Questioning"):
                    return " 1- What if your VR adventure is more than meets the eye? Our study explores the intriguing link between VR sickness and reduced attention. Could symptoms like nausea and eyestrain be secret saboteurs of your virtual focus? Uncover the hidden dynamics with our P3b ERP component findings.\
                             2- Ever pondered the price of virtual thrills? Our research suggests VR sickness might be stealing more than just your stomach's attention. How do symptoms like fatigue impact your ability to stay immersed? Delve into our study to unveil the mysteries behind VR's effects on attention and task performance.\
                             3- Is your VR experience a challenge for both body and mind? Our study asks the question: Could VR sickness be impacting your attention span? Explore the possibilities as we decode the relationship between symptoms like nausea and the P3b ERP component. Your virtual journey might be more complex than you think!\
                             4- Curious about the secrets hidden in your VR headset? Our study dives into the realm of attention and VR sickness, unraveling the mystery behind symptoms like eyestrain. How do these elements play a role in your virtual experience? Join us on this curious exploration into the intricate world of virtual reality.\
                             5- Wondering why VR sometimes leaves you feeling off-balance? Our research poses the question: Could VR sickness be affecting more than just your equilibrium? Explore the correlation between symptoms like fatigue and attention reduction with our P3b ERP measures. Get ready to uncover the curious side of your virtual escapades! "
                case("Narrative/Storytelling"):
                    return "   1- Our study unfolds a captivating narrative in the virtual realm, exploring the intricate relationship between VR sickness and attention. With P3b ERP components guiding the story, we navigate through the twists of nausea, eyestrain, and fatigue impacting users' focus. Join us on a formal storytelling journey into the heart of Virtual Reality research, where every chapter adds depth to the immersive experience.\
                               2- Step into the world of formal storytelling as our study ventures through the virtual museum, unraveling the complex tale of VR sickness and attention modulation. With P3b ERP components as the storytellers, we paint a vivid picture of how symptoms like nausea and eyestrain influence users' focus. Engage with the narrative, where every detail contributes to a deeper understanding of Virtual Reality research.\
                               3- In the formal narrative of our study, we delve into the virtual museum's immersive story, exploring the profound impact of VR sickness on attention. P3b ERP components narrate the chapters of nausea, eyestrain, and fatigue shaping users' focus. Embark on an informative journey, where every aspect contributes to a nuanced understanding of Virtual Reality. No hashtags or emojis, just a formal narrative in the realm of VR research.\
                               4- Explore the formal narrative of our study, where the virtual museum becomes the stage for unraveling the intricate relationship between VR sickness and attention. P3b ERP components take on the role of formal storytellers, revealing the nuances of symptoms like nausea and eyestrain on users' focus. Join us on an engaging and informative journey into the depths of Virtual Reality research.\
                               5- Once upon a formal study, we embarked on a storytelling journey through the virtual landscape, decoding the complex interplay of VR sickness and attention. P3b ERP components craft the narrative, shedding light on how symptoms like nausea and eyestrain mold users' focus. Immerse yourself in an informative and engaging story, where each chapter contributes to a deeper understanding of Virtual Reality.\
                            "
def get_completion(prompt,tone):
    print(prompt)
    print(tone)
    query = client.chat.completions.create(
        model="gpt-3.5-turbo",
        #model="gpt-4",
        messages=[
            {"role": "system",
                "content": f"You are a twitter post generator, who generate posts and never add hashtags or emojis ,this is a must.\
                You will be provided with a text content from an academic paper (delimited with triple quotes). \
                Use the following step-by-step instructions to respond to user inputs:\
                Step_1:  Analyse the given text carefully.\
                Step_2:  based on your analysis in step_1, Does the given text look like a part of a scientific or academic paper based on specific criteria to you?\
                     - if yes: \
                        -- Return Only generated tweets based on the following instructions:\
                            -- Take the following examples as a reference that you can imitate: \
                                    ##\
                                    * Example_1: \
                                        ** Input: '''{get_example('example_1')}'''\
                                        ** Output: {get_tweets_based_on_tone('example_1',tone)} \
                                    ##\
                                    *Example_2:\
                                            ** Input: '''{get_example('example_2')}'''\
                                            ** Output: {get_tweets_based_on_tone('example_2', tone)} \
                            -- Never use hashtags, this is a must.\
                            -- Never use emojis, this is a must. \
                            -- Must use the provided tone {tone}. \
                            -- generated post must be between (50 - 60) words\
                            -- the generated tweets should be engaging.\
                            -- use language that can be well understandable for a high school student. \
                            -- the generated tweets should go viral.\
                            -- suggest only 5 posts, suggest them in bullets. You must add line breaks. the output must look like the fllowing examples:\
                                1- 1st generated post. \
                                2- 2nd generated post. \
                                3- 3rd generated post. \
                    - if No: Only Return the following error message:"
                           f"' Please provide a valid text from your scientific paper so I can generate engaging posts for you! '\
                "

            },
            {"role": "user",
                "content": f" here is my text {prompt}." \
                #Suggest only 5 posts and Never use hashtags or emojies,\
                #this is a must. the posts length must be between 50 to 60 words "
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
