import re
import traceback

from typing import Optional, Dict, List, Union

def parse_bracket_template(s, params):
    if not isinstance(s, str):
        return s
    try:
        s = s.format(**params)
        return s
    except KeyError as e:
        print('Error: {} not found in params'.format(e))
        print('Params: {}'.format(params))
        print('Template: {}'.format(s))
        traceback.print_exc()
        return None
    
class PromptBuilder:
    def __init__(self, template:Optional[str]=None):
        self.template = template

    def build_prompt(self, params: Union[Dict[str, str], List[Dict[str, str]]], setting: str = 'zero-shot'):
        if self.template is None:
            print('No template found, returning params by simple key-value concatenation')
            return ' '.join('{}: {}'.format(k, v) for k, v in params.items())
        if setting == 'zero-shot':
            assert isinstance(params, dict)
            return parse_bracket_template(self.template, params)
        elif setting == 'few-shot':
            assert isinstance(params, list)
            # Simply treating the first example as the query, and the rest as the support set
            query, supports = params[0], params[1:]
            params = query
            if len(supports) == 1:
                for k, v in supports[0].items():
                    params['ex_{}'.format(k)] = v
            else:
                for i, support in enumerate(supports):
                    for k, v in support.items():
                        params['ex{}_{}'.format(i, k)] = v
        return parse_bracket_template(self.template, params)
        