# Case Study 1: Attendance Recovery Computation
# PDF Topic No. 12

total_classes = int(input("Enter total classes conducted: "))
attended_classes = int(input("Enter classes attended: "))

if total_classes <= 0 or attended_classes < 0 or attended_classes > total_classes:
    print("Invalid input")
else:
    percentage = (attended_classes / total_classes) * 100

    print("Attendance percentage:", round(percentage, 2), "%")

    if percentage >= 75:
        print("You are eligible for the examination.")
        print("No additional classes are required.")
    else:
        additional = 0

        while ((attended_classes + additional) /
               (total_classes + additional)) * 100 < 75:
            additional = additional + 1

        print("You are not eligible yet.")
        print("Additional classes required:", additional)