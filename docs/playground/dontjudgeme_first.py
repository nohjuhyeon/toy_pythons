# # 문제 만들기 _ juuuuuu
# 아래는 4개의 Python 관련 문제와 각 문항의 난이도에 따른 점수화
# 1. 문제: Python에서 변수를 선언하는 방법은? (점수: 10점)
#    1) var name, 2) name = value, 3) set name, 4) name == value
#    - 정답: 2
# 2. 문제: Python에서 리스트(List)의 특징은 무엇인가요? (점수: 15점)
#    1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다
#    - 정답: 1
# 3. 문제: Python에서 조건문을 작성하는 방법은? (점수: 10점)
#    1) if-else, 2) for-in, 3) while, 4) def
#    - 정답: 1
# 4. 문제: Python에서 함수를 정의하는 방법은? (점수: 5점)
#    1) class, 2) def, 3) import, 4) return
#    - 정답: 2

# —----- 결과 —-------------
# 응답한 내용 : 1번 2, 2번 1, 3번 1, 4번 2
# 당신 응답 합계 : 40점
# 학점은 A 입니다.
# # 
    
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