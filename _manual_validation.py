import requests

url = "http://127.0.0.1:8000/predict"

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
}

data = {
    "alcohol": 9.4,
    "volatile_acidity": 0.7,
    "fixed_acidity": 7.4,
    "citric_acid": 0.0,
    "residual_sugar": 1.9,
    "chlorides": 0.076,
    "free_sulfur_dioxide": 11,
    "total_sulfur_dioxide": 34,
    "density": 0.9978,
    "pH": 3.51,
    "sulphates": 0.56,
}

resp = requests.post(url, headers=headers, json=data)
print(resp.json())
