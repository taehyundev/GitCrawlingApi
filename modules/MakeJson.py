import json

def m_json(path, data): # 경로와 데이터를 받는다.
    with open(path, 'w', encoding='utf-8') as f :
            json.dump(data, f,indent='\t',ensure_ascii=False)