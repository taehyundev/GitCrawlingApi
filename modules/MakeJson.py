import json

def m_json(path, data):
    with open(path, 'w', encoding='utf-8') as f :
            json.dump(data, f,indent='\t',ensure_ascii=False)