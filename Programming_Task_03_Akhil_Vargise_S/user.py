first = input("Enter First Name: ").lower()
last = input("Enter Last Name: ").lower()
year = input("Enter Birth Year (e.g. 2004): ")

short_year = year[-2:]  

print("\nHere are your username suggestions:")
print(f"1. {first}{last}{year}")           
print(f"2. {first[0]}.{last}{short_year}") 
print(f"3. {last}_{first}")                
print(f"4. {first}{short_year}_{last}")    
print(f"5. {first[0]}{last}_{year}")       