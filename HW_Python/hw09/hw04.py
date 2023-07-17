import json

def save_to_json(func):

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        data = {
            "args": args,
            "kwargs": kwargs,
            "result": result
        }
        
        with open('result.json', 'w') as file:
            json.dump(data, file)
        return result

    return wrapper
