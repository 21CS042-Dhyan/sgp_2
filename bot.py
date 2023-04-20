import spacy

# Load the pre-trained language model for English
nlp = spacy.load('en_core_web_md')

# Define the FAQs as a list of strings
faq = [
    "What is your name?",
    "My name is FAQ Bot.",
    "Hi",
    "Hello, how are you doing?",
    "How can I contact you?",
    "You can contact us at info@charusat.ac.in .",
    "What is the size of CHARUSAT University?",
    "An employee strength of 600, student strength of more than 8000 and a Capital Outlay of INR 150 Crores are the scalar dimensions of CHARUSAT.",
    "Who is the founder of CHARUSAT University?",
    "Shri Charotar Moti Sattavis Patidar Kelavani Mandal",
    "What is the rank of CHARUSAT University?",
    "CHARUSAT has been ranked in the 151-200 band among universities in India by the National Institutional Ranking Framework (NIRF) in 2022.",
    "How many programs are there in CHARUSAT university?",
    "CHARUSAT offers 72 programs from UG to PhD",
    "How many Institutes are there in CHARUSAT university?",
    "There are 9 institutes.",
    "How many faculties are there in CHARUSAT university?",
    "There are 6 faculties.",
    "Is CHARUSAT under GTU?",
    "Yes",
    "Which of the reputed companies for which the placement is provided to the students of Charotar University of Science and Technology?",
    "The topmost reputed companies in which placement is provided to the students of Charotar University of Science and Technology are as follows: ICICI SECURITIES, Reliance, IBM, Idea Cellular, Siemens, Ford India LID, IGATE, Bajaj Allianz, Citi Bank, L&T Infotech, Vodafone, Axis Bank, Tech Mahindra, Adnani Group, Berger.",
    "What are the courses offered to the students of Charotar University of Science and Technology (CHARUSAT) ?",
    "The courses offered to the students of Charotar University of Science and Technology are as follows: B.tech, B.Pharma, BPT, and B.Sc courses",
    "Which are the documents required for the admission process of the students?",
    "The documents required for the admission of the students of Charotar University of Science and Technology are as follows: Intermediate Mark-sheets and certificate Transfer Certificate Category Certificate High School Mark-sheets and certificate Income Certificate Admit Card/ Scorecard Degree certificates ( for PG courses)"
]

# Process the FAQs with the language model
processed_faq = [nlp(qa) for qa in faq]

# Run the chatbot
while True:
    user_input = input("You: ")
    processed_input = nlp(user_input)

    if user_input.lower() in ["bye", "goodbye", "exit"]:
        print("FAQ Bot: Goodbye!")
        break
    
    # Find the most similar FAQ using cosine similarity
    max_similarity = -1
    best_match = None
    for i, qa in enumerate(processed_faq):
        similarity = processed_input.similarity(qa)
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = i

    # Get the response from the best matching FAQ
    if max_similarity > 0.5:
        bot_response = faq[best_match + 1]
    else:
        bot_response = "I'm sorry, I didn't understand your question. Please repeat or contact us at info@charusat.ac.in or visit our site at https://www.charusat.ac.in/"

    print("FAQ Bot:", bot_response)