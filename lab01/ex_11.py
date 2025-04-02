height = float(input('키(m)를 입력해 주세요:'))*0.01
weight = float(input('몸무게를 입력해 주세요:'))
BMI = weight/height**2

print(f"BMI:{BMI:0.3}")
