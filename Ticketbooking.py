class Ticketbooking():
    def Bookticket(self):

        username = input("ENTER EMAIL ID:")
        print("MOVIES PLAYING NOW : ")
        a = " THE KASHMIR FILES "
        b = "RADHE SHYAM "
        c = " GANGUBAI "
        d = " JHUND"
        e = "THE BATMAN"
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)

        movie_name = input("ENTER THE MOVIE NAME YOU WANT TICKETS FOR : ")
        if movie_name == a or b or c or d or e :
            print("THANK YOU !, YOU HAVE SELECTED THE MOVIE : ", movie_name)
            no_tick = int(input("ENTER THE NUMBER OF TICKETS :"))

            x = int(no_tick * 300)
            avail_tick = 70
            print("NUMBER OF TICKETS AVAILABLE ARE : ", avail_tick)
            if no_tick < avail_tick:
                print("THE PRICE OF TICKETS ARE : ", x)

                print("COMBOS AVAILABLE:")
                print("1.POPCORN AVAILABLE ")
                print("2.FRIES COMBO")
                print("3.BURGER COMBO")

                u = int(input("ENTER COMBO NUMBER :"))
                z = int(input("HOW MANY COMBOS DO YOU WANT:"))
                y = int(z * 500)

                print("YOUR COST FOR FOOD IS  : ",y)
                print("TOTAL AMOUNT TO BE PAID IS : ", x + y)
            else:
                print("INSUFFICIENT NUMBER OF TICKETS : ")
        else:
            print(" INCORRECT MOVIE NAME ! ")
    def Removeticket(self):
        q_user = input(" ENTER EMAIL ID : ")
        w = input(" ARE YOU SURE YOU WANT TO CANCEL YOUR TICKETS : " )
        if w == "YES":
            otp = int(input("ENTER OTP : "))

            p = 7795
            if otp == p:
                print("OTP CONFIRMED !")
                print("TICKETS CANCELLED SUCESSFULLY ")
            else:
                print("INCORRECT OTP ! TRY AGAIN")
        if w == "NO":
            print("TICKETS ARE NOT CANCELLED ")
#o1 = Ticketbooking()
#o1.Bookticket()

o2 = Ticketbooking()
o2.Removeticket()