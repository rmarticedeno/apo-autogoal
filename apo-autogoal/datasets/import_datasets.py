from datasets import load_dataset
from pathlib import Path

def import_and_save_dataset(path, name, param=None):
    folder_name = f"{name}-{param}" if param else name
    if not (Path('datasets') / folder_name).exists():
        ds = load_dataset(path,param)
        ds.save_to_disk('datasets/' + folder_name)

import_and_save_dataset("ChilleD/MultiArith", "MultiArith")
import_and_save_dataset("deepmind/aqua_rat", "Aqua-Rat", "raw")
import_and_save_dataset("deepmind/aqua_rat", "Aqua-Rat", "tokenized")
import_and_save_dataset("openai/gsm8k", "gsm8k", "main")
import_and_save_dataset("openai/gsm8k", "gsm8k", "socratic")