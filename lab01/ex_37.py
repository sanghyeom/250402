# ex_37.py 영한 사전을 한영 사전으로 바꾸기
# 다음 사전형으로 제시된 영한 사전을 한영 사전으로 바꾸기




en2ko ={'book':'책',
        'snake':'뱀',
        'language':'언어',
        }
ko2en = {}

for k,v in en2ko.items():
    ko2en[v]=k
print(ko2en)