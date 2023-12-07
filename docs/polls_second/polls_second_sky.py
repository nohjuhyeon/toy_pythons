# source from ../polls_firsts_juhyeonnoh.py

list_question = [
    "상품의 품질에 대해 어떻게 생각하시나요?",
    "상품의 가격에 대해 어떻게 생각하시나요?",
    "상품의 디자인에 대해 어떻게 생각하시나요?",
    "상품에 대한 전반적인 만족도는 어떠신가요?"
]       
list_answer = ["좋음", "중간", "좋아지길"] 
answer_list=[]

for num_question_counts in range(len(list_question)):
    print("{}. {}".format(num_question_counts + 1,list_question[num_question_counts]))
    for num_answer_counts in range(len(list_answer)):
        print("{}. {}".format(num_answer_counts + 1, list_answer[num_answer_counts]), end = " ")
        pass
    print("")
    answer_a = int(input("당신 생각은 몇 번 : "))
    answer_list.append(answer_a)
    if num_question_counts!=3 :
        print("")
        print("-----------------")
        pass
    elif num_question_counts ==3:
        break

answer_1_num = int(answer_list.count(1))
answer_2_num = int(answer_list.count(2))
answer_3_num = int(answer_list.count(3))
answer_average = (3*answer_1_num+2*answer_2_num+1*answer_3_num)/(answer_1_num + answer_2_num + answer_3_num)

print("")
print("—--- 통 계 ----")
print("설문자 답항별 갯수 표시 : [{},{},{}]".format(answer_1_num,answer_2_num,answer_3_num))
print("답변별 가중치(좋음:3,중간:2,좋아지길:1)")
print("답항 가중 평균:")
print("({}*3+{}*2+{}*1)/({}+{}+{})={}".format(answer_1_num,answer_2_num,answer_3_num,answer_1_num,answer_2_num,answer_3_num,answer_average))
