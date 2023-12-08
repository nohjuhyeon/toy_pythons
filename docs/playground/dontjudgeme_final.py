# 요기에 주르륽 나열하기

question_list = ["1. 문제: Python에서 변수를 선언하는 방법은? (점수: 10점)",
                 "2. 문제: Python에서 리스트(List)의 특징은 무엇인가요? (점수: 15점)",
                 "3. 문제: Python에서 조건문을 작성하는 방법은? (점수: 10점)",
                 "4. 문제: Python에서 함수를 정의하는 방법은? (점수: 5점)"
                 ]
answer_list = ["1) var name, 2) name = value, 3) set name, 4) name == value",
               "1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다",
               "1) if-else, 2) for-in, 3) while, 4) def",
               "1) class, 2) def, 3) import, 4) return"
]
input_answer = [2,1,1,2]
user_answer = []
correct_answer = [2,1,1,2]
score_list=[10,15,10,5]
for a in range(len(question_list)):
    print(question_list[a])
    print(answer_list[a])
    print("- 정답: {}".format(input_answer[a]))
    user_answer.append(input_answer[a])
    pass
pass

def result_cal() :
    score=[]
    for i in range(len(user_answer)):
       if user_answer[i] == correct_answer[i] :
            score.append(int(score_list[i]))
            user_sum = sum(score)
    if user_sum >=30 :
        user_score = "A"
    elif user_sum >=20 :
        user_score = "B"
    else:
        user_score = "C"
    print ("--------결과---------")
    print("응답한 내용 : 1번 {}, 2번 {}, 3번 {}, 4번 {}".format(user_answer[0], user_answer[1],user_answer[2], user_answer[3]))
    print("당신 응답 합계 : {}점".format(user_sum))
    print("학점은 {}입니다.".format(user_score))
 

result_cal()
