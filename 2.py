from datetime import datetime
class AgeCalc:
    def getAge(bday,bmonth,byear):
        nowyear=datetime.now().year
        nowmonth=datetime.now().month
        nowday=datetime.now().day
        if nowday >= bday:
            dayAge=int(nowday) - int(bday)

        else:

            nowmonth = nowmonth -1
            if nowmonth == 2:
                if(nowyear%4==0):
                    month_check = 29
                else:
                    month_check = 28

            elif nowmonth == 1 or 3 or 5 or 7 or 8 or 10 or 12:

                month_check = 31
            else :
                month_check = 30
            print(month_check)
            nowday = nowday + month_check
            dayAge=int(nowday) - int(bday)
        if nowmonth >= bmonth:
            monthage=int(nowmonth) - int(bmonth)
        else:
            nowyear = nowyear -1
            nowmonth = nowmonth + 12
            monthage=int(nowmonth) - int(bmonth)
        if nowyear >= byear:
            yearage=int(nowyear) - int(byear)
        else:
            print("Not Born and Use Computers 'WOW' ")
        agee=[yearage,monthage,dayAge]
        return agee

# obj = AgeCalc()
# obj1 = obj.getAge(25,2,1985)
# print(obj1)
class Person(AgeCalc):
    def __init__(self,fname,lname,birthday,birthmonth,birthyear):
        self.fname=fname
        self.lname=lname
        self.birthmonth=birthday
        self.birthday=birthmonth
        self.birthyear=birthyear
        self.age=AgeCalc.getAge(birthday,birthmonth,birthyear)
    def welcome(self):
        print(f'Welcom {self.fname} {self.lname} you are {self.age[0]} year , {self.age[1]} month , {self.age[2]} days')
obj1 = Person (input("Enter First name : "),input("Enter Last name : "),int(input("Enter Birthday : ")),int(input("Enter Birthymonth : ")),int(input("Enter Birthyear : ")))
obj1.welcome()



















# import datetime
# class agecalc:
#     def days_in_month(year, month):
#         if month==12:
#             return 31
#         else:
#             date1 = datetime.date(year, month, 1)
#             date2 = datetime.date(year, month+1, 1)
#             difference = date2 - date1
#             return(difference.days)
#     def is_valid_date(year, month, day):
#         if datetime.MINYEAR<=year<=datetime.MAXYEAR and 1<=month<=12 and 1<=day<= days_in_month(year, month):
#             return True
#         else:
#             return False
#     def days_between(year1, month1, day1, year2, month2, day2):
#         date1=datetime.date(year1,month1,day1)
#         date2=datetime.date(year2,month2,day2)
#         if is_valid_date(year1,month1,day1) and is_valid_date(year2,month2,day2)and (date1<date2):
#             difference=date2-date1
#             return difference.days
#         else:
#             return 0
#     def age_in_days(year, month, day):
#         todays_date=datetime.date.today()
#         if is_valid_date(year, month,day) and (age_in_days<todays_date):
#             return days_between(age_in_days(year,month,day),todays_date(year,month,day))
#         else:
#             return 0