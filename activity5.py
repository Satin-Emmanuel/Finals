print('\n\t\t\t\t\t\t=================================')
print('\t\t\t\t\t\t|FAHRENHEIT TO CELSIUS CONVERTER|')
print('\t\t\t\t\t\t=================================')
temp=eval(input('\nEnter Temperature in Fahrenheit: '))
celsius=(temp - 32) * 5/9
print(f'\n\nThe conversion of {temp} degrees Fahrenheit is {celsius} degrees Celsius\n\nor')
print(f'\nThe conversion of {temp} degrees Fahrenheit is {round(celsius, 2)} degrees Celsius')