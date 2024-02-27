from employee import Employee
from file_op import File

if __name__ == "__main__":
    command = input("press any key to continue (q to exit): ")
    while command.lower() != "q":
        try:
            first_name = input("First name: ")
            last_name = input("Last name: ")
            father_name = input("Father's name: ")
            national_code = input("National Code: ")
            phone = input("Phone number: ")
        except:
            print("Invalid Data")
            continue
        else:
            employee = Employee(
                first_name=first_name,
                last_name=last_name,
                father_name=father_name,
                national_code=national_code,
                phone=phone,
            )
            file = File()
            file.write(employee.export())
        finally:
            command = input("press any key to continue (q to exit)")
