height = int(input("What is your height: "))
weight = int(input("What is your weight: "))
name = input("What is your name: ")
height2 = height * height
BMI = weight / height2
metricBMI = BMI * 703

print(name)
print("BMI= ", BMI)
print("BMI Metric= ", + metricBMI)

if metricBMI > 30 :
  print("you are obese")
elif metricBMI < 18.5 :
  print("you are underweight")
elif 18.5 <= metricBMI <= 30 :
  print("you are healthy")
