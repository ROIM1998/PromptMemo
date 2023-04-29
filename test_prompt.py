import json
import random

from templates import PROMPT_TEMPLATES
from utils.template_utils import PromptBuilder
from utils.data_utils import DataParser

def test_prompt(dataset_name):
    data = json.load(open('data/%s.json' % dataset_name, 'r'))
    examples = data['examples'][:10]

    # Testing the prompt in a one-shot setting
    template, fewshot_template = PROMPT_TEMPLATES[dataset_name]['zero-shot'], PROMPT_TEMPLATES[dataset_name]['few-shot']    
    parser = DataParser(dataset_name)
    parsed_data = parser.parse(examples)
    builder = PromptBuilder(template)
    prompt = builder.build_prompt(parsed_data[0])
    fewshot_builder = PromptBuilder(fewshot_template)
    fewshot_prompt = fewshot_builder.build_prompt(parsed_data[:2], setting='few-shot')
    return prompt, fewshot_prompt
    
if __name__ == '__main__':
    dataset_name = 'winowhy'
    print('Testing prompt builder...')
    prompt, fewshot_prompt = test_prompt(dataset_name)
    print('Prompt: {}'.format(prompt))
    print('Few-shot prompt: {}'.format(fewshot_prompt))