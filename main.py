print("welcome tip calculator\n ")
total_pil= float(input("what was the totall pill? \n "))
bil_presentage= float(input("what presentage tip would give? 10,12,and 15 \n "))
split= float(input("How many peapole to split the bill\n "))
tip = total_pil /split * 1.12
tip_round = round(tip,2)
print(f"every person have to pay: {tip_round}")