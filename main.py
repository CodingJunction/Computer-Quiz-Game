from question import Question
from data import question_data
from logic import Logic
quiz_set=[]
for i in question_data:
    obj=Question(i["question"],i["correct_answer"])
    quiz_set.append(obj)
quiz=Logic(quiz_set)
while not quiz.empty():
    quiz.next()
print('The game ends')
print('Your final score is',quiz.score)
