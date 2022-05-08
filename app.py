from utility import isRegexPass

questions = ["What is your name?",
             "What is you DOB (dd/mm/yyyy)?", "What is your occupation?"]

question_and_answer = dict()

i = 0
while i < len(questions):
    answer = input(questions[i])

    if "What is you DOB (dd/mm/yyyy)?" == questions[i] and not isRegexPass(answer):
        print("invalid answer: ", answer)

    else:
        question_and_answer.update({questions[i]: answer})
        i += 1

print(question_and_answer)
