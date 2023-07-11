from typing import Union
from fastapi import FastAPI
import pandas as pd

SHEET_ID = '1owFcVCNxPIHYIANlKLL6Ou7kZCvzJNQXmsUCu8xttnc'
SHEET_NAME = 'Sheet1'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)
score_list = [0,0,0,0,0]
app = FastAPI()

@app.get("/question_no ={questions} &Answer ={answer}")
def question_answer(question_no: int, answer: str):
    log = question_no-1
    if answer == df['Answer'][log]:
        score_list[log] = 1
        return {"question #" + str(question_no) + " " + df['Question'][log] +  " is correct. As your answer is " + df['Answer'][log],
                True,sum(score_list)}
    else:
        log = question_no-1
        return {"question #" + str(question_no) + " " + df['Question'][log] + " is Wrong. As your answer is " + df['Answer'][log],
                False,sum(score_list)}

@app.get("/clear")
def clear():
    score_list = [0,0,0,0,0]
    return {sum(score_list)}

@app.get("/result")
def clear():
    return {sum(score_list)}
