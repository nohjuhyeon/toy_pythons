question_list = ["1. 문제: Python에서 변수를 선언하는 방법은? (점수: 10점)",            #질문 문항 리스트
                "2. 문제: Python에서 리스트(List)의 특징은 무엇인가요? (점수: 15점)",
                "3. 문제: Python에서 조건문을 작성하는 방법은? (점수: 10점)",
                "4. 문제: Python에서 함수를 정의하는 방법은? (점수: 5점)"
                ]
answer_list = ["1) var name, 2) name = value, 3) set name, 4) name == value",    # 보기 문항 리스트
                "1) 순서가 있고 변경 가능하다, 2) 중복된 값을 가질 수 없다, 3) 원소를 추가하거나 삭제할 수 없다, 4) 정렬된 상태로 유지된다",
                "1) if-else, 2) for-in, 3) while, 4) def",
                "1) class, 2) def, 3) import, 4) return"
                ]
class Question:
    def question(self,question_list,answer_list):   #질문지 출력 함수 작성
        print(question_list[a])                     # 질문 문항 출력
        print(answer_list[a])                       #보기 문항 출력
        
    def input(self, user_answer):                   #답지 입력 합류 작성
        input_answer = int(input("- 정답:"))        #답지 입력
        user_answer.append(input_answer)            #답안지에 리스트 추가

question = Question()
user_answer = []
for a in range(len(question_list)):
    question.question(question_list,answer_list)    #질문지 출력
    question.input(user_answer)                     #답지 입력 
pass

class Result_score : #클래스 생성
    def answer(self, user_answer) : # function 1 : sum 도출
        correct_answer = [2,1,1,2]
        score_list=[10,15,10,5]
        score=[]
        for i in range(len(user_answer)):
            if user_answer[i] == correct_answer[i] :
                score.append(int(score_list[i]))
                user_sum = sum(score)
        return user_sum

    def score(self, user_sum): #function 2 : score 도출
        if user_sum >=30 :
            user_score = "A"
        elif user_sum >=20 :
            user_score = "B"
        else:
            user_score = "C"
        return user_score
    
result_score = Result_score() # 클래스 불러내기
user_sum = result_score.answer(user_answer) #user_sum 변수 재정의

print("--------결과---------")
print("응답한 내용 : 1번 {}, 2번 {}, 3번 {}, 4번 {}".format(user_answer[0], user_answer[1],user_answer[2], user_answer[3]))
print("합게 : {}점".format(result_score.answer(user_answer)))
print("학점은 {}입니다.".format(result_score.score(user_sum)))

