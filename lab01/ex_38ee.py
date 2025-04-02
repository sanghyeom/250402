orders = [
# P 루프시작
    {
        "country": "USA",
# S 루프시작
        "customers": [
            {
                "customer_id": "C001",
# T 루프시작
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

def order_by_customers(orders):
    result = {}

    for P in orders:
        country = P['country']
        
        for S in P['customers']:
            cust_id = S['customer_id']
            
            products = []
            total_amount = 0
            
            for T in S['orders']:
                products.append(T['product'])
                total_amount += T['unit_price']*T['quantity']
            
            # products = [ order['product'] for order in S['orders'] ]
            # total_amount = sum([order['unit_price']*order['quantity'] for order in S['orders']])
            
            result[cust_id] = {
                "country": country,
                "products": products,
                "total_amount": total_amount
            }

    return result

result = order_by_customers(orders)

print(result)

# # import pprint
# pprint.pprint(result)

# import json
# print( json.dumps(result, indent=4) )