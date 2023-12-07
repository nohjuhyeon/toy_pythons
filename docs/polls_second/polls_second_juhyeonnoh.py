# source from ../polls_firsts_sky.py

list_question = [
    "상품의 품질에 대해 어떻게 생각하시나요?",
    "상품의 가격에 대해 어떻게 생각하시나요?",
    "상품의 디자인에 대해 어떻게 생각하시나요?",
    "상품에 대한 전반적인 만족도는 어떠신가요?"
]
list_answer = ["좋음", "중간", "좋아지길"]

list_statistics = [0, 0, 0]
for num_question_count in range(len(list_question)):
    print("{}. {}".format(num_question_count+1, list_question[num_question_count]))
    for num_answer_count in range(len(list_answer)):
        print("{}. {}".format(num_answer_count+1, list_answer[num_answer_count]), end=" ")
    print("")
    str_list_answer = input("당신 생각은 몇 번: ")
    num_answer = int(str_list_answer)
    index = num_answer - 1
    list_statistics[index] =list_statistics[index] + 1
    if num_question_count!=3 : 
            print("")
            print("----------")
    elif num_question_count==3 :
        break
pass
num_average = (list_statistics[0] * 3 + list_statistics[1] * 2 + list_statistics[2] * 1)/(3 + 2 + 1)
print("—--- 통 계 ----")
print("설문자 답항별 갯수 표시 : {}".format(list_statistics))
print("답변별 가중치 (좋음:3, 중간:2, 좋아지길:1)")
print("답항 가중 평균 : ({}*3 + {}*2 +{}*1) / (3+2+1) = {}".format(list_statistics[0],list_statistics[1],list_statistics[2],num_average))
pass
