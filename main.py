# main.py

import json
import yaml
import xml.etree.ElementTree as ET
import numpy as np
import pandas as pd
import time
from typing import TypedDict
from collections import namedtuple
from dataclasses import dataclass
from pydantic import BaseModel

# -----------------------------
# 1. User structures
# -----------------------------

# TypedDict
class UserDict(TypedDict):
    id: int
    name: str
    email: str

user_typed = UserDict(id=1, name="Ahmed", email="ahmed@example.com")

# namedtuple
UserNT = namedtuple("UserNT", ["id", "name", "email"])
user_namedtuple = UserNT(id=2, name="Leila", email="leila@example.com")

# dataclass
@dataclass
class UserDC:
    id: int
    name: str
    email: str

user_dataclass = UserDC(id=3, name="Said", email="said@example.com")

# pydantic
class UserPD(BaseModel):
    id: int
    name: str
    email: str

user_pydantic = UserPD(id=4, name="Noor", email="noor@example.com")

# -----------------------------
# 2. NumPy array vs Python list
# -----------------------------
py_list = [1, 2, 3, 4, 5]
np_array = np.array([1, 2, 3, 4, 5])

# -----------------------------
# 3. Decorator to measure execution time
# -----------------------------
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} executed in {end - start:.6f} seconds")
        return result
    return wrapper

# -----------------------------
# 4. Compare scalar-vector multiplication
# -----------------------------
@timer
def multiply_list(lst, scalar):
    return [x * scalar for x in lst]

@timer
def multiply_numpy(arr, scalar):
    return arr * scalar

multiply_list(py_list, 10)
multiply_numpy(np_array, 10)

# -----------------------------
# 5. Load CSV with Pandas
# -----------------------------
df = pd.read_csv("data/users.csv")
print("\nPandas DataFrame from CSV:")
print(df.to_string(index=False))

# -----------------------------
# 6. Load JSON
# -----------------------------
with open("data/users.json", "r", encoding="utf-8") as f:
    users_json = json.load(f)
print("\nJSON data:")
print(json.dumps(users_json, indent=4, ensure_ascii=False))

# -----------------------------
# 7. Load YAML
# -----------------------------
with open("data/users.yaml", "r", encoding="utf-8") as f:
    users_yaml = yaml.safe_load(f)
print("\nYAML data:")
print(yaml.dump(users_yaml, allow_unicode=True, sort_keys=False))

# -----------------------------
# 8. Load XML
# -----------------------------
tree = ET.parse("data/users.xml")
root = tree.getroot()
users_xml = [{child.tag: child.text for child in user} for user in root]
print("\nXML data:")
for user in users_xml:
    print(user)

