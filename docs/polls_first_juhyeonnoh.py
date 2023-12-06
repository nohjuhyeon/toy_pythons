list_question = [
    "상품의 품질에 대해 어떻게 생각하시나요?",
    "상품의 가격에 대해 어떻게 생각하시나요?",
    "상품의 디자인에 대해 어떻게 생각하시나요?",
    "상품에 대한 전반적인 만족도는 어떠신가요?"
]       
list_answer = ["좋음", "중간", "좋아지길"] 
for num_question_counts in [1,2,3,4]:
    num_question_counts = num_question_counts - 1
    num_question = num_question_counts + 1
    str_question = list_question[num_question_counts]
    print("{}. {}".format(num_question,str_question))
    for num_answer_counts in [1,2,3]:
        num_answer_counts = num_answer_counts - 1
        num_answer = num_answer_counts + 1
        str_answer = list_answer[num_answer_counts]
        print("{}. {}".format(num_answer,str_answer), end = " ")
    if num_question_counts != 3:
        print("")
        print("-----------------")
