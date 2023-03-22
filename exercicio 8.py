# conversor de medidas

a = (float(input('Uma distancia em metros :')))

print('A medida de {} m corresponde a : \n {} KM \n {} hm \n {} dam \n {:.0f}  dm \n {:.0f} cm \n {:.0f} mm'.format(a,(a/1000),(a/100),(a/10),(a*10),(a*100),(a*1000)))