print("Area/Perimeter of Rectangle/Triangle")
ask1 = input("Rectangle or Triangle: ")
ask2 = input("Area or Perimeter: ")

if ask1.lower() == "rectangle":
    if ask2.lower() == "area":
        l = int(input("Enter Length: "))
        w = int(input("Enter Width: "))
        areaR = l * w 
        print("Area of Rectangle: "+ str(areaR))

    if ask2.lower() == "perimeter":
        l = int(input("Enter Length: "))
        w = int(input("Enter Width: "))
        perimeterR = 2 * (l + w)
        print("Perimeter of Rectangle: "+ str(perimeterR))  

if ask1.lower() == "triangle":
    if ask2.lower() =="area":
        b = int(input("Enter Base: "))
        h = int(input("Enter Height: "))     
        areaT = (b * h)/2
        print("Are of Triangle: "+ str(areaT))

    if ask2.lower() =="perimeter":
        s1 = int(input("Enter side 1: "))
        s2 = int(input("Enter side 2: "))
        s3 = int(input("Enter side 3: "))
        perimeterT = s1 + s2 + s3 
        print("Perimeter of Triangle: "+ str(perimeterT))


#to make it not case sensitive:
#use "variable.lower()" if value is in lowercase
#use "variable.upper()" if value is in uppercase
