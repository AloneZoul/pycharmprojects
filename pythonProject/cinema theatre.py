seat = {1: 'Normal Seat', 2: 'Balcony Seat'}
print(seat)
select = int(input("Enter A Number"))
if (select > 2) or (select <= 0):
    print("Invalid Selection")
else:
     print ("You Have Selected:" + seat[select])
movie = {1: 'Abu',  2: 'New',  3: 'Second'}
print(movie)
select=int(input("Enter A Number"))
if (select>3) or (select<=0) :
    print("There Is No Such Choice")
else :
      print("You Have Selected"+movie[select])
      print("Long Time No see")
