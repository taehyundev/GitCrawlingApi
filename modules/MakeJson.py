import json

def m_json(path, data):
    with open(path, 'w') as f :
            json.dump(data, f,ensure_ascii=False)