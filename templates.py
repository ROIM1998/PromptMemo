PROMPT_TEMPLATES = {
    'emoji': {
        'zero-shot': 'Guess popular movies from their emoji descriptions. What movie does this emoji describe? {emoji} A. {choiceA} B. {choiceB} C. {choiceC} D. {choiceD} E. {choiceE}',
        'few-shot': 'Select the most similar movie to the following emoji description as the example given below:\n Example: {ex_emoji} A. {ex_choiceA} B. {ex_choiceB} C. {ex_choiceC} D. {ex_choiceD} E. {ex_choiceE}. Answer: {ex_label}. \nNow select the most similar movie to the following emoji description: {emoji} A. {choiceA} B. {choiceB} C. {choiceC} D. {choiceD} E. {choiceE}. Please answer with your choice only without any other words',
    },
    'hindu-knowledge': {
        'zero-shot': 'Please select the best matched answer for the given question from the choices list below based on Hindu mythology. Question: {question} Choices: A. {choiceA} B. {choiceB} C. {choiceC} D. {choiceD}.\nPlease respond with the choice only, withou any other words.',
        'few-shot': 'Select the best answer from the listed choices given below to the following question as the example given below based on Hindu mythology:\n Example: {ex_question} A. {ex_choiceA} B. {ex_choiceB} C. {ex_choiceC} D. {ex_choiceD}. Answer: {ex_label}. \nNow select the most similar answer to the following question: {question} A. {choiceA} B. {choiceB} C. {choiceC} D. {choiceD}. Please answer with your choice only without any other words',
    },
    'known-unknowns': {
        'zero-shot': 'Please select the best option for the question give to you based on the correct factual knowledge. Question: {question} A.  {choiceA} B.  {choiceB}\n Please answer with your choice only without any other words.',
        'few-shot': 'Please select the best option for the question give to you as the example given below based on the correct factual knowledge:\n Example: {ex_question} A. {ex_choiceA} B. {ex_choiceB} . Answer: {ex_label}. \nNow select the most similar answer to the following question: {question} A. {choiceA} B. {choiceB}.\nPlease answer with your choice only without any other words',
    },
    'bigbench': {
        'zero-shot': 'Please choose the best option from the listed choices that precisely express the given things in common. {question} A. {choiceA} B. {choiceB} C. {choiceC} D. {choiceD} E. {choiceE}\nPlease answer with your choice only without any other words.',
        'few-shot': 'Please choose the best option from the listed choices that precisely express the given things in common following the example given below:\n Example: {ex_question} A. {ex_choiceA} B. {ex_choiceB} C. {ex_choiceC} D. {ex_choiceD} E. {ex_choiceE} Answer: {ex_label}.\nNow select the most similar answer to the following question: {question} A. {choiceA} B. {choiceB} C. {choiceC} D. {choiceD} E. {choiceE}.\nPlease answer with your choice only without any other words',
    },
    'strange-stories': {
        'zero-shot': 'Please choose the best possible option to the given question based on the context telling the story. Story: {context}.\nQuestion: {question} A. {choiceA} B. {choiceB} C. {choiceC} D. {choiceD}\nPlease answer with your choice only without any other words.',
        'few-shot': 'Please choose the best possible option to the given question based on the context telling the story. Here are some examples:\n Example: {ex_context}.\nQuestion: {ex_question} A. {ex_choiceA} B. {ex_choiceB} C. {ex_choiceC} D. {ex_choiceD} Answer: {ex_label}.\nNow select the most similar answer to the following question: {question} A. {choiceA} B. {choiceB} C. {choiceC} D. {choiceD} .\nPlease answer with your choice only without any other words',
    },
    'winowhy': {
        'zero-shot': 'In the sentence: {reasoning}. Is the pronoun reasoning correct? Please answer with either \"correct\" or \"incorrect\". Do not include any other words.',
        'few-shot': 'You\'ll be given some examples for the pronoun referring reasonings with their correctness. Examples: Here is a {ex_label} reasoning: in the sentence {ex_reasoning}\nNow, you\'ll be given a pronoun referring reasoning. In the sentence {reasoning} Is the pronoun reasoning correct? Please answer with either \"correct\" or \"incorrect\". Do not include any other words.',
    },
}