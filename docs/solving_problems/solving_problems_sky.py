# 답을 받아서 산출하기...sky


# 입력 리스트 [] 정답리스트 [] 점수 리스트[]
# if문으로 비교해서 점수 넣기(function쓰기 가능)
# 최종 점수 계산식
# function 2개, class 1개 사용

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

