products = [
    {
        "category": "Electronics",
        "items": [
            {"name": "Laptop", "price": 1200, "stock": 5},
            {"name": "Smartphone", "price": 800, "stock": 10}
        ]
    },
    {
        "category": "Home Appliances",
        "items": [
            {"name": "Vacuum Cleaner", "price": 150, "stock": 7},
            {"name": "Air Conditioner", "price": 500, "stock": 3}
        ]
    }
]

result = {
    "Laptop": {"price": 1200, "stock": 5},
    "Smartphone": {"price": 800, "stock": 10},
    "Vacuum Cleaner": {"price": 150, "stock": 7},
    "Air Conditioner": {"price": 500, "stock": 3}
    }
##########################################3
# def convert_data(products):
#     for i in range(len(products)):
#         for k,v in products[i].items():
#             Choise = []
#             dename = []
#             for j in range(len(v)):
#                 if type(v[j]) == dict :
#                     Choise = v[j].copy()
#                     dename = v[j].copy()
#                     dename.pop('name')
#                     # print('"',Choise['name'],'"',':',dename)
#                     return Choise['name'],dename
#####################################################

# print(products['items'])

def convert_data(products):
    result={}
    for category in products :
        for item in category['items']:
            name = item['name']
            # del item['name']
            item.pop('name')
            result[name] = item
    return result


print(convert_data(products))













orders = [
    {
        "country": "USA",
        "customers": [
            {
                "customer_id": "C001",
                "orders": [
                    {"product": "Laptop", "quantity": 1, "unit_price": 1200},
                    {"product": "Mouse", "quantity": 2, "unit_price": 25}
                ]
            },
            {
                "customer_id": "C002",
                "orders": [
                    {"product": "Smartphone", "quantity": 1, "unit_price": 800}
                ]
            }
        ]
    },


    
    {
        "country": "Canada",
        "customers": [
            {
                "customer_id": "C003",
                "orders": [
                    {"product": "Laptop", "quantity": 2, "unit_price": 1150},
                    {"product": "Keyboard", "quantity": 1, "unit_price": 100}
                ]
            }
        ]
    }
]


result = {
    "C001": {
        "country": "USA",
        "products": ["Laptop", "Mouse"],
        "total_amount": 1250  # (1 x 1200) + (2 x 25)
    },
    "C002": {
        "country": "USA",
        "products": ["Smartphone"],
        "total_amount": 800
    },
    "C003": {
        "country": "Canada",
        "products": ["Laptop", "Keyboard"],
        "total_amount": 2400  # (2 x 1150) + (1 x 100)
    }
}
# 주문자 아이디 = 나라 , 제품 , 토탈 