import os
from typing import List

def get_paragraph()->List[str]:
    data_path ='./data/text/charactor.txt'
    if os.path.exists(data_path):
        with open(data_path, encoding='utf-8')as f:
            data = f.read()
            result = data.splitlines()
            paragraph = []
            empty_index = 0
            try:
                while True:
                    empty_index = result.index('')
                    paragraph.append(''.join(result[0: empty_index]))
                    result = result[empty_index+1:]
            except ValueError:
                if result:
                    paragraph.append(''.join(result))
        return paragraph
    raise FileExistsError