import json
import pickle

with open('res2.json','r',encoding='UTF-8') as f1:
    with open('res5.pickle','wb') as f2:
        data=json.load(f1)
        pickle.dump(data,f2)
