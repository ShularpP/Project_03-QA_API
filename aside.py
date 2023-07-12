SHEET_ID = '1owFcVCNxPIHYIANlKLL6Ou7kZCvzJNQXmsUCu8xttnc'
SHEET_NAME = 'Sheet1'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)
score_list = [0,0,0,0,0]

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)
class score_collect:
  def __init__(self):
    self.score_01 = 0
    self.score_02 = 0
    self.score_03 = 0
    self.score_04 = 0
    self.score_05 = 0
    self.score_06 = 0
    self.score_07 = 0
    self.score_08 = 0
    self.score_09 = 0
    self.score_10 = 0
  def total(self):
    return self.score_01 + self.score_02 +self.score_03 +self.score_04 +self.score_05 + self.score_06 +self.score_07 + self.score_08 + self.score_09 + self.score_10
  def reset(self):
    self.score_01,self.score_02,self.score_03,self.score_04,self.score_05,self.score_06,self.score_07 ,self.score_08,self.score_09,self.score_10 = 0,0,0,0,0,0,0,0,0,0
    
score_dashboard = score_collect()

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

@app.get("/action=action&question_no ={questions} &answer ={answer}")
def question_answer_01(action:str, question_no: int = 0, answer: str = ""):
  if action == "reset":
    score_dashboard.reset()
    respond = "Score has been reset"
  elif action == "quiz":
    log = question_no-1
    if answer == df['Answer'][log]:
      exec(f"score_dashboard.score_0{question_no}=1")
      respond = f"Q:{question_no} {df['Question'][log]} A: {answer} is correct"
    else:
      exec(f"score_dashboard.score_0{question_no}=0")
      respond = f"Q:{question_no} {df['Question'][log]} A: {answer} is wrong, Correct answer is {df['Answer'][log]}"     
    
  elif action == "sum":
    respond = f"This is to summarize the score"
  total_score = score_dashboard.total()
  return {total_score, respond}