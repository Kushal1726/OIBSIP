# Enter your details here  #
Name = input("Enter your sweet name: ")
Age = int(input("Enter your Age: "))
Gender = input("Enter your gender: ")
Weight = float(input("Enter your weight in Kilogram: "))
Height = float(input("Enter your height in Centimeter: "))
Height = Height / 100
BMI = Weight / (Height * Height)

# print section of the calculator #
print(".!------------Your body mass weight report-----------!.\n")
print("Name:", Name)
print("Age:", Age)
print("Gender:", Gender)
print("Body mass index:", BMI)

def categorize_bmi(BMI):
    if BMI <= 18.5:
        return "Underweight : You gain the Weight "
    elif BMI <= 24.9:
        return "Normal weight "
    elif BMI <= 29.9:
        return "Overweight : You need a Exercise "
    elif BMI <= 40:
        return "Obese : You need a Exercise "
    else:
        return "Extremely obese : You need a Exercise "
    
    # This section save the Memory in one text # 

def save_user_data(Height, Weight, BMI, category):
    with open("memory.txt", "a") as file:
        file.write(f"{Height},{Weight},{BMI},{category}\n")
print("Your data been saved in memory ")

def main():
    if BMI > 0:
        category = categorize_bmi(BMI)
        print(Name + ", You are classified as", category)
        save_user_data(Height, Weight, BMI, category)
# calling the main function #
if __name__ == '__main__':
    main()
