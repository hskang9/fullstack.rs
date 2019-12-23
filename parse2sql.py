import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import json

import os
print(os.listdir("./"))
data=pd.read_json("./recipes.json",lines=True)

outF = open("data2db.sql", "w")


def parse_data(string):
    return string.replace("'", "''").replace('"', "''")
    

def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]

def parse_double_quotation(string):
    open = 0
    for idx, i in enumerate(string):
        if i == '"':
            if open == 0:
                i = '\'\"'
                replacer('"',i, idx)
                open = 1
            else:
                i = '\"\''
                replacer('"',i, idx)
                open = 0 
    return string

for index, data in data.iterrows():
    name = parse_data(data["Name"])
    if data["Description"] != None:
        description = parse_data(data["Description"])
    else:
        description = 'None'
    ingredients = [parse_data(i) for i in data["Ingredients"]]
    method = [parse_data(i) for i in data["Method"]]
    sql = "INSERT INTO recipes (id, name, author, description, ingredients, method, url) VALUES ({},'{}','{}','{}',ARRAY{},ARRAY{},'{}');\n".format(index, name, data["Author"], description, ingredients, method, data["url"])
    outF.write(sql.replace('"', "'"))
    outF.write("\n")
outF.close()

