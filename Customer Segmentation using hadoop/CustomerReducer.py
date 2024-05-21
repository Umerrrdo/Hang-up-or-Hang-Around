import sys

current_combination = None
current_customers = []

def emit_combination(combination, customers):
    print(f'{combination}\t{",".join(customers)}')

for line in sys.stdin:
    line = line.strip()
    
    try:
        service_combination, customer_id = line.split('\t', 1)
    except ValueError:
        
        continue
    
    if current_combination == service_combination:
        current_customers.append(customer_id)
    else:
        if current_combination is not None:
            emit_combination(current_combination, current_customers)
        current_combination = service_combination
        current_customers = [customer_id]


if current_combination is not None:
    emit_combination(current_combination, current_customers)
