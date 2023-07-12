from typing import Union
from fastapi import FastAPI
import pandas as pd
import json

app = FastAPI()

@app.get("/sheet_id={sheet_id}&answer_sheet=answer_sheet")
def answer_sheet_sum(sheet_id:str, answer_sheet = "0000010001"):
    SHEET_ID = sheet_id
    SHEET_NAME = 'Sheet1'
    url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
    df = pd.read_csv(url)
    #result = df['Answer'][0]
    #result = list(find_all(answer_sheet , '1'))
    
    answer = []
    for index, digit in enumerate(answer_sheet):
        if int(digit) == 0:
            answer.append([index, df['Answer'][index],df['Image'][index]])

    df_a = pd.DataFrame(answer, columns = (['No','Answer','Image']))
    
    #jsonStr = json.dumps(answers)
    #result = jsonStr
    #return result
