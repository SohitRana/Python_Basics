sub1=int(input("enter the subject math"))
sub2=int(input("enter the subject science"))
sub3=int(input("enter the subject hindi"))
sub4=int(input("enter the subject english"))
sub5=int(input("enter the subject sanskrit"))

percentage=(sub1+sub2+sub3+sub4+sub5)*100/500


if percentage>100:
    print("percentage should not exceed 100")

elif percentage>=95 and percentage<=100:
    print("grade A+")
    
elif percentage>=90 and percentage<=95:
    print("grade A")

elif percentage>=85 and percentage<=90:
    print("grade B+")

elif percentage>=81 and percentage<=85:
    print("grade b")

elif percentage>=76 and percentage<=80:
    print("grade C+")

elif percentage>=71 and percentage<=75:
    print("grade C")
    
elif percentage>=61 and percentage<=70:
    print("grade D+")

elif percentage>=46 and percentage<=60:
    print("grade D")

elif percentage>=33 and percentage<=45:
    print("grade E")
    
else:
    print("fail")
