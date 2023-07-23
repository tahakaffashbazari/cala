import math
while True:
    m=int(input("adad avval ra vard konid"))
    y=int(input("adad dovvom ra vard konid"))
    print("+,-,/,*,sin,cos")

    p=input("entekhab konid")
    if p=="+":
        print("sum:",m + y)
    elif p=="-":
        print("tafrigh",m-y)
    elif p=="/":
        print("taghsim",m/y)
    elif p=="*":
        print("zarb",m*y)
    elif p=="sin":
        print("gavab sinos:",math.sin(m))
    elif p=="cos":
        print("gavab cosinos:",math.cos(m))
else:exit