from typing import List, Dict, Tuple, Optional
from tqdm import tqdm

SUPPORTED_DATASETS = ['emoji', 'sarcasm', 'sentiment140', 'stanford_sentiment_treebank']

def form_example_emoji(data):
    results = {}
    results['emoji'] = data['input']
    for i, k in enumerate(data['target_scores']):
        results['choice' + chr(ord('A') + i)] = k
    results['labels'] = [data['target'], chr(ord('A') + list(data['target_scores']).index(data['target']))]
    results['label'] = results['labels'][0]
    return results

PARSE_FUNCS = {
    'emoji': form_example_emoji,
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
