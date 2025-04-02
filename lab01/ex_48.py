# ex_48.py 성적 자동처리
# data 폴더에 학생별 시험점수가 적힌 파일이 학생명.txt로 들어있음
# 이폴더에 파일을 열어서 시험점수를 읽은다음
# 각 학생의 평균점수와 표준편차를 기록하는

# with open("file_w.txt", "a" ,encoding="utf-8") as f:
    
#     # 실질적으로 ,PC가 다른 작업중이라면, 버퍼           링됨 바로 저장되지않음
    
#     f.write("Hello python\n")
#     f.write("안녕 파이썬\n")
#     # 닫지않았을경우에 멀티테스킹일경우나 뭐시깽이 저장이 안될수도있다고함
#     # f.close
#     /
# import ex_45
# # ex_45.mean(), ex_45.std()
# with open("file_w.txt", "r" ,encoding="utf-8") as f:
#     lines = f.readlines()
#     # print(lines, type(lines))
#     for line in lines:
#         print(line, end='')
import ex_45
import os
input_files = os.listdir("./data/")
for file in input_files :
    if file[-4:] =='.txt' :
       file_name = file[0:-4]
       with open('./data/'+file, "r" ,encoding="utf-8") as f:
            lines = f.readlines()
            lines_int =[]
            for i in range(len(lines)):
                lines_int.append(int(lines[i]))
            mean = round(ex_45.mean(lines_int),2)
            std = round(ex_45.std(lines_int),2)
            print(file_name,mean,std)
        