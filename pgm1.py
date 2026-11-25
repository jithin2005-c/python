 current_year=int(input("Enter current year"))
 final_year=int(input("Enter final year"))
 print("leap years are")
 for year in range(current_year,final_year+1):
 if year%4==0:
 print(year)
