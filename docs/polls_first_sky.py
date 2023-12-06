list_question = [
    "상품의 품질에 대해 어떻게 생각하시나요?",
    "상품의 가격에 대해 어떻게 생각하시나요?",
    "상품의 디자인에 대해 어떻게 생각하시나요?",
    "상품에 대한 전반적인 만족도는 어떠신가요?"
]
list_answer = ["좋음", "중간", "좋아지길"]

for num_question_count in range(len(list_question)):
    print("{}. {}".format(num_question_count+1, list_question[num_question_count]))
    for num_answer_count in range(len(list_answer)):
        print("{}. {}".format(num_answer_count+1, list_answer[num_answer_count]), end=" ")
    if num_question_count!=3 : 
            print("")
            print("----------")
    elif num_question_count==3 :
        break
    


