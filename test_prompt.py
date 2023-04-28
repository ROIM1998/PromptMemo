import json
import random

from utils.template_utils import parse_bracket_template

if __name__ == '__main__':
    data = json.load(open('data/emoji.json'))
    
    examples = data['examples']
    # Testing the prompt in a one-shot setting
    ex, question = random.sample(examples, 2)
    template = 'Guess popular movies from their emoji descriptions. What movie does this emoji describe? {emoji} A.  {choiceA} B.  {choiceB} C.  {choiceC} D.  {choiceD} E.  {choiceE}'
    params = {
        'emoji': '👧🐟🐠🐡',
        'choiceA': 'Finding Nemo',
        'choiceB': 'the wolf of wall street',
        'choiceC': 'se7en',
        'choiceD': 'the shining',
        'choiceE': 'mr. Smith goes to washington'
    }