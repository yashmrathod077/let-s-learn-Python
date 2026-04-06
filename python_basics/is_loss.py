cost = float(input(" enter the cost to manufactoration"))
selling_price = float(input(" enter the selling price "))
diff = cost - selling_price
persantage = selling_price/cost*100

if cost >  selling_price:
    print(f"losss of  {persantage} % per peas")
else:
    print(f"profit of { persantage} % per peas")


