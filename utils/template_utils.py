import re
import traceback

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