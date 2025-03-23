#Create a currency.py program that asks the user for the amount they have in pesos, soles, and reais and calculates the total in USD

def convert_pesos_to_usd(pesos):
    return pesos * 0.00024 # 1 peso is 0.00024 USD

def convert_soles_to_usd(soles):
    return soles * 0.27  # 1 sol is 0.27 USD

def convert_reais_to_usd(reais):
    return reais * 0.17 # 1 real is 0.17 USD

pesos = float(input("Enter the amount in pesos: "))
soles = float(input("Enter the amount in soles: "))
reais = float(input("Enter the amount in reais: "))

total_usd = convert_pesos_to_usd(pesos) + convert_soles_to_usd(soles) + convert_reais_to_usd(reais)
print(f"The total amount in USD is: {total_usd}")
