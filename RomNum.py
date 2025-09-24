def rom_num(s):
  romanvalues={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
  prev=0
  total=0
  
  #reversed is used to read roman string backwards
  for i in reversed(s):
    value=romanvalues[i]
    if value<prev:
      total-=value
    else:
      total+=value
    prev=value
  return total

#main
rn=input("Enter the Roman Numberal of your choice:")
s=rn.upper()
sol=rom_num(s)
print("The integer value is:",sol)
