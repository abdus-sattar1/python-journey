dictionary_one = {'key': 'value', 'key_2': 'value_2'}

print(dictionary_one['key'])

# useful for things that have fixed rates that can be pulled whenever required e.g. tax rates

shoes = int(20)
gas = int(250)
book = int(8)

shopping_list = [shoes, gas, book]

tax_rates = {'Standard Rate': 0.2, 'Reduced Rate': 0.05, 'Exempt': 0}
print('Tax rates in 2025:' + ' ' + str(tax_rates))

# calculate the tax amount on shoes
shoes_tax = shoes * tax_rates['Standard Rate']
print(shoes_tax)

#if in 2030 the standard tax rate increases to 25%
tax_rates['Standard Rate'] = 0.25
print('Tax rates in 2030:' + ' ' + str(tax_rates))

#adding a new tax rate
tax_rates['Special'] = 0.15
print(tax_rates)

#removing the tax rate
del tax_rates['Special']
print(tax_rates)

