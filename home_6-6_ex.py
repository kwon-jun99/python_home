orders = [
    {"주문번호": 1001, "고객명": "김철수", "구매금액": 120000, "가입일": "2021-03-15", "지역": "서울"},
    {"주문번호": 1002, "고객명": "이영희", "구매금액": None, "가입일": "2020-08-10", "지역": "부산"},
    {"주문번호": 1003, "고객명": "박민수", "구매금액": 35000, "가입일": "2024-01-20", "지역": "서울"},
    {"주문번호": 1004, "고객명": "최지은", "구매금액": -5000, "가입일": "2019-05-12", "지역": "대구"},
    {"주문번호": 1005, "고객명": "정우성", "구매금액": 550000, "가입일": "2018-11-02", "지역": "서울"},
    {"주문번호": 1006, "고객명": "한지민", "구매금액": None, "가입일": "2022-07-01", "지역": "부산"},
    {"주문번호": 1007, "고객명": "강호동", "구매금액": 25000, "가입일": "2023-09-15", "지역": "광주"},
    {"주문번호": 1008, "고객명": "신세경", "구매금액": 9999999, "가입일": "2021-12-24", "지역": "서울"},
    {"주문번호": 1009, "고객명": "유재석", "구매금액": 89000, "가입일": "2020-01-05", "지역": "대전"},
    {"주문번호": 1010, "고객명": "송혜교", "구매금액": 175000, "가입일": "2017-04-30", "지역": "서울"},
]


#자료 갯수 파악

print(len(orders))                    #10

                    # 문제1) 이상치 탐지(구매금액이 0~1,000,000원 범위를 벗어나면 이상치로 판단)

count=0

for order in orders:
    if order["구매금액"] is not None:
        if order["구매금액"] > 1000000 or order["구매금액"]<0:
            count+=1
print(count)

                    # 문제2) 이상치 처리/다음기준으로 처리하시오.(1,000,000 초과 → 1,000,000 / 0 미만 → 0)

for order in orders:
    if order["구매금액"] is not None:
        if order["구매금액"] <0:
            order["구매금액"]=0
        
        if order["구매금액"]>1000000:
            order["구매금액"]=1000000

print(orders)

                    # 문제3) 결측지 확인 / 금액이 결측치(None)인 데이터의 개수를 구하시오.

wrong=0

for order in orders:
    if order["구매금액"] is None:
        wrong+=1

print(wrong)

                    # 문제4) 결측지 처리 / 결측치를 제외한 구매금액 평균을 계산한 후 결측치를 평균값으로 대체하시오.

prices=[]

for order in orders:
    if order["구매금액"] is not None:
        prices.append(order["구매금액"])

avg= round(sum(prices)/len(prices))
print(avg)

for order in orders:
    if order["구매금액"] is None:
        order["구매금액"]=avg

print(orders)


                    # 문제5) 회원 가입 연수 계산 (특성 추출) / 현재 연도를 기준으로 회원가입 후 몇 년이 지났는지 계산하여 "가입연수" 컬럼을 추가하시오.

from datetime import datetime

year=datetime.now().year

for order in orders:
    join_year=order["가입일"].split("-")[0]

    order["가입연수"]= int(year)-int(join_year)

print(orders)

                    #문제6) VIP 여부 생성 (특성 추출) / 구매금액 기준 200000원 이상 → VIP / 200000원 미만 → 일반으로 "회원등급" 컬럼을 추가하시오.

for order in orders:
    if order["구매금액"] > 200000:
        order["회원등급"]= "VIP"
    else:
        order["회원등급"]= "일반"

print(orders)

                    # 문제7) 기술통계 / 구매금액에 대한 개수, 합계, 평균, 최대값, 최소값을 출력하시오.

prices=[]

for order in orders:
    prices.append(order["구매금액"])

print(len(prices))
print(sum(prices))
print(sum(prices)/len(prices))
print(max(prices))
print(min(prices))

                    # 문제8) 지역별 평균 구매금액을 구하시오.

local={}
pay={}

for order in orders:

    place=order["지역"]
    p=order["구매금액"]
    
    if place not in local:
        local[place]=0
        pay[place]=0

    local[place]= local[place] + 1
    pay[place]= pay[place] + p


for place in local:
    print(place,pay[place]/local[place])

                    # 문제9) 회원등급별 평균 구매금액 / VIP 회원과 일반 회원의 평균 구매금액을 구하시오.

grade_sum = {}
grade_count = {}

for order in orders:
    grade = order["회원등급"]
    price = order["구매금액"]

    if grade not in grade_sum:
        grade_sum[grade] = 0
        grade_count[grade] = 0

    grade_sum[grade] = grade_sum[grade] + price
    grade_count[grade] = grade_count[grade] + 1

for grade in grade_sum:
    avg = grade_sum[grade] / grade_count[grade]
    print(grade, avg)

                    # 문제10) 가입연수별 그룹 분석 / 가입연수를 기준으로 다음과 같이 그룹을 나누시오. / 0~2년, 3~5년, 6년 이상 각 그룹의 평균 구매금액을 구하시오.

price1 , price2, price3= 0, 0, 0
num1, num2, num3 = 0, 0, 0

for order in orders:
    year=order["가입연수"]

    if year <=2:
        price1= price1 + order["구매금액"]
        num1= num1 +1
    if year>2 and year<=5:
        price2=price2 +order["구매금액"]
        num2= num2 +1
    if year>5:
        price3=price3 +order["구매금액"]
        num3= num3 +1

print(price1/num1,price2/num2,price3/num3)