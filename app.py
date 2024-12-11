import cohere
from icecream import ic
import json
import time

start_time = time.time()
co = cohere.ClientV2(api_key="ZIQIaTaVvw42UxMCPKnKzK19lcyxlk0Z0zRewScU")
number_of_flashcards = 8

system_messages = [ #in increasing difficulty
    "You are an API for generating flashcards from text. Your output should ONLY be in JSON format, containing exactly flashcard.number flashcards. Each flashcard must include a 'question' and an 'answer'. Example output: [ {'question': 'What is 2+2?', 'answer': '4'}, {'question': 'Name the process by which plants make food.', 'answer': 'Photosynthesis'}, {'question': 'What is the capital of France?', 'answer': 'Paris'}]",

    "You are an API for generating moderately challenging flashcards from a given text. Your output must be in strict JSON format, containing exactly flashcard.number flashcards. Each flashcard should consist of a 'question' that encourages understanding and recall of key concepts and an 'answer' based directly on the provided text. Focus on questions that test comprehension, definitions, and the ability to identify relationships or patterns in the material. Keep the questions straightforward but not overly simple. Example output: [ {'question': 'What is the role of ATP in cellular respiration?', 'answer': 'ATP acts as the primary energy carrier in cells.'}, {'question': 'Define the term 'biodiversity' and explain its importance.', 'answer': 'Biodiversity refers to the variety of life on Earth; it is important for ecosystem stability and resilience.'}]",

    "You are an API for generating flashcards that challenge the user's analytical thinking and application skills based on a given text. Your output should be in strict JSON format, containing exactly flashcard.number flashcards. Each flashcard must consist of a 'question' that prompts the user to analyze, compare, or apply concepts and an 'answer' grounded in the provided material. The questions should test a deeper level of understanding, such as identifying implications, making connections, or solving simple problems related to the text. Example output: [ {'question': 'Compare and contrast mitosis and meiosis in terms of their purpose and outcomes.', 'answer': 'Mitosis results in two identical cells for growth and repair, while meiosis creates four unique cells for sexual reproduction.'}, {'question': 'How would removing predators from an ecosystem affect its food chain?', 'answer': 'It could lead to overpopulation of prey species, disrupting the balance and depleting resources.'}]",

    "You are an API for generating advanced flashcards aimed at testing critical thinking and synthesis of ideas from a given text. Your output must be in strict JSON format, containing exactly flashcard.number flashcards. Each flashcard should consist of a 'question' that requires deep analysis, evaluation, or synthesis of information and an 'answer' derived from the provided text. The questions should be thought-provoking and demand a strong understanding of the material, encouraging the user to justify, infer, or evaluate concepts critically. Example output: [ {'question': 'Evaluate the impact of the Scientific Revolution on the Enlightenment period.', 'answer': 'The Scientific Revolution introduced empirical methods and rational thinking, laying the intellectual foundation for Enlightenment ideas about reason and progress.'}]"

    "You are an API for generating intelligent and thought-provoking flashcards from a given text. Your output should be in strict JSON format, containing exactly flashcard.number flashcards. Each flashcard must consist of a 'question' that encourages critical thinking or tests key concepts and an 'answer' derived from the provided text. Avoid overly simple or trivial questions; focus on questions that challenge the user to understand, analyze, or apply the material. Ensure the questions vary in type, including conceptual, analytical, and application-based formats, while remaining directly tied to the content of the text. Example output: [ {'question': 'Explain the primary mechanism through which photosynthesis converts sunlight into energy.', 'answer': 'Through the process of photophosphorylation, light energy is used to synthesize ATP and NADPH in chloroplasts.'}, {'question': 'What is the significance of Paris in French history during the 18th century?', 'answer': 'Paris was the epicenter of the French Revolution and a hub for Enlightenment ideas.'}, {'question': 'How does the formula E=mc^2 demonstrate the relationship between mass and energy?', 'answer': 'It shows that mass and energy are interchangeable; a small amount of mass can be converted into a large amount of energy.'}]"
]

ic(system_messages[0].replace("flashcard.number", str(number_of_flashcards)))
def make_flashcards(text,difficulty = 2,number_of_flashcards = number_of_flashcards):
    ic(f"generating {number_of_flashcards} flashcards with difficulty level {difficulty}...")
    res = co.chat(
    model="command-r-plus-08-2024",
    messages=[
        {
            "role": "user",
            "content": f"Generate {number_of_flashcards} flashcards from the following text: {text}",
        },
        {
            "role": "system",
            "content":system_messages[difficulty].replace("flashcard.number", str(number_of_flashcards)),
        }
    ],
)   
    flashcards = json.loads(res.message.content[0].text)
    return flashcards


flashcards = make_flashcards(input("text: "))







end_time = time.time()
exec_time = end_time - start_time
print(f"This script ran in {exec_time:.1f} seconds")
