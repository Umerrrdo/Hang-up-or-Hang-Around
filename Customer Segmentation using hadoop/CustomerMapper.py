import sys

for line in sys.stdin:
    line = line.strip()
    parts = line.split(',')
    
   
    if len(parts) < 33:  
        continue
    
    try:
        services = parts[13:22]  
        service_combination = ','.join(services)
        print(f'{service_combination}\t{parts[0]}')
    except IndexError:
       
        continue
