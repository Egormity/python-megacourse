import json 

PATH = r"C:\Users\kotla\Desktop\python-megacourse\001-experiments\quiz\data.json"

with open(PATH, "r") as file:
    data = json.load(file)


score = 0


for question in data:
    print("\n" + question["question_text"])

    for index, alternative in enumerate(question["alternatives"]):
        print(f"{index + 1}. {alternative}")
    
    user_answer = int(input("Enter your answer: "))
    question["user_answer"] = user_answer

    if user_answer == question["correct_answer"]:
        score = score + 1


print('\n----------------------------------')


for index, question in enumerate(data):
    print(f"\nQuestion {index + 1}: {question['question_text']}")
    print(f"Your answer: {question['user_answer']}")
    print(f"Correct answer: {question['correct_answer']}")


print(f"\nYou scored {score} / {len(data)}")