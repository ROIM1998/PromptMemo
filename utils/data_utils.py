from typing import List, Dict, Tuple, Optional
from tqdm import tqdm

SUPPORTED_DATASETS = ['emoji', 'hindu-knowledge', 'known-unknowns', 'bigbench', 'strange-stories', 'winowhy']

def form_example_simple_qa_choice(data):
    results = {}
    results['question'] = data['input']
    for i, k in enumerate(data['target_scores']):
        results['choice' + chr(ord('A') + i)] = k
        if data['target_scores'][k] == 1:
            results['labels'] = [k, chr(ord('A') + i)]
            results['label'] = k
    return results

def form_example_contextual_qa_choice(data):
    results = {}
    results['context'], results['question'] = data['input'].split('\nQ:')
    results['context'], results['quesiton'] = results['context'].strip(), results['question'].strip()
    for i, k in enumerate(data['target_scores']):
        results['choice' + chr(ord('A') + i)] = k
        if data['target_scores'][k] == 1:
            results['labels'] = [k, chr(ord('A') + i)]
            results['label'] = k
    return results

def form_binary_reasoning(data):
    results = {}
    results['reasoning'] = data['input']
    for i, k in enumerate(data['target_scores']):
        results['choice' + chr(ord('A') + i)] = k
        if data['target_scores'][k] == 1:
            results['labels'] = [k, chr(ord('A') + i)]
            results['label'] = k
    return results

PARSE_FUNCS = {
    'emoji': form_example_simple_qa_choice,
    'hindu-knowledge': form_example_simple_qa_choice,
    'known-unknowns': form_example_simple_qa_choice,
    'bigbench': form_example_simple_qa_choice,
    'strange-stories': form_example_contextual_qa_choice,
    'winowhy': form_binary_reasoning,
}

class DataParser:
    def __init__(self, dataset_name: str, raw_data: Optional[List[Dict]] = None):
        if dataset_name not in SUPPORTED_DATASETS:
            raise NotImplementedError(f"Dataset {dataset_name} not supported.")
        self.dataset_name = dataset_name
        self.parse_func = PARSE_FUNCS[dataset_name]
        self.raw_data = None
        self.parsed_data = None

    def parse(self, raw_data: Optional[List[Dict]] = None):
        if raw_data is None:
            if self.raw_data is None:
                raise ValueError("raw_data is None")
            raw_data = self.raw_data
        self.raw_data = raw_data
        self.parsed_data = [self.parse_func(d) for d in tqdm(raw_data)]
        return self.parsed_data
    
    def clear_rawdata(self):
        self.raw_data = None
