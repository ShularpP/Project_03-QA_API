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
    
    answers = []
    i = 0
    for digit in answer_sheet:
        print (digit)
        if (digit == "0") or (digit ==0):
            answers.append(df['Answer'][i])
        i+=1
        
    result = answers
    
    jsonStr = json.dumps(answers)
    #result = jsonStr
    return result
