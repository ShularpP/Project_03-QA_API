from typing import Union
from fastapi import FastAPI
import pandas as pd
import json


def create_flex(df):
  input_ans = df['No']
  answer = df['Answer']
  image = df['Image']
  flex = {"type": "carousel","contents":[]}
  for q_num in range(len(input_ans)):
      bubble_temp = """{
            "type": "bubble",
            "hero": {
              "type": "image",
              "size": "full",
              "aspectRatio": "20:13",
              "aspectMode": "cover",
              "url": "%s"
            },
            "body": {
              "type": "box",
              "layout": "vertical",
              "spacing": "sm",
              "contents": [
                {
                  "type": "text",
                  "text": "%s",
                  "wrap": true,
                  "weight": "bold",
                  "size": "xl"
                },
                {
                  "type": "box",
                  "layout": "baseline",
                  "contents": [
                    {
                      "type": "text",
                      "text": "%s",
                      "wrap": true,
                      "weight": "bold",
                      "size": "xl",
                      "flex": 0
                    }
                  ]
                }
              ]
            }
          }"""%(image[q_num],input_ans[q_num],answer[q_num])
      bubble_temp = json.loads(bubble_temp)
      flex['contents'].append(bubble_temp)
  return flex

def line_response(flex):
  response = {"response_type": "object","line_payload": []}
  response['line_payload'].append(flex)
  return response

app = FastAPI()

@app.get("/answer_sheet_sum")
def answer_sheet_sum(sheet_id:str, sheet_name:str = "Sheet1",  answer_sheet = "0000011111"):
    SHEET_ID = sheet_id
    SHEET_NAME = sheet_name
    url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
    df = pd.read_csv(url)
    #result = df['Answer'][0]
    #result = list(find_all(answer_sheet , '1'))
    
    answers = []
    for index,digit in enumerate(answer_sheet):
        if str(digit) == "0":
            answers.append(index)


    df = df.loc[answers]
    flex = create_flex(df)    
    response = line_response(flex)
    
    return response
    
    
    
    
    #jsonStr = json.dumps(answers)
    #result = jsonStr
    #return result
