
from dbhelper import DBHelper

# helper=DBHelper()
#
# #helper.insert_patient(1,"ritesh","8367567865")
# # helper.insert_patient(2,"umesh","8367567865")
# # helper.insert_patient(3,"hitesh","8367567865")
# # helper.insert_patient(4,"swapnil","8367567865")
# # helper.delete_patient(3)
# # helper.fetch_all()
#
# helper.update_patient(2,"umesh jadhav","9300000000")


def main():
    db=DBHelper()
    while True:
        print("Press 1 to insert new patient")
        print("Press 2 to display all patient")
        print("Press 3 to delete patient")
        print("Press 4 to update patient")
        print("Press 5 to exit program")
        print()

        try:
            choice=int(input())
            if(choice==1):
                #insert
                pid=int(input("Enter patient id"))
                pname=input("Enter patient name")
                pphone=input("Enter patient phone")
                db.insert_patient(pid,pname,pphone)

            elif choice==2:
                #display
                db.fetch_all()
                pass
            elif choice==3:
                #delete
                paid=int(input("enter patient id to delete"))
                db.delete_patient(paid)

            elif choice == 4:
                #update
                patid=int(input("Enter patient Id to update details"))
                patname=input("Enter new name")
                patphone=input("Enter new Number")
                db.update_patient(patid,patname,patphone)
                pass
            elif choice==5:
                break
            else:
                print("Invalid input")
        except Exception:
            print(Exception)
            print("Invalid details....")


if __name__ == "__main__":
    main()