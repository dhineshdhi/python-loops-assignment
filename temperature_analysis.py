# Name: Dhinesh
# Roll Number: 777
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
# Write your code here

for temp1 in range(len(temperatures)):
    for temp2 in range(len(temperatures)):
        if temperatures[temp1] < temperatures[temp2]:
            temperatures[temp1],temperatures[temp2]=temperatures[temp2],temperatures[temp1]

# print(temperatures)

print(f"Highest Temperature: {temperatures[6]}°C")
print(f"Lowest Temperature: {temperatures[0]}°C")

print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
# Write your code here
count = 0
for temp in temperatures:
    if temp<=30:
        continue
    else:
        count+=1
print(f"Hot Days (>30°C):{count}")


print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]
# Write your code here
count = 0
for day,temp in enumerate(temperatures):
    if temp>30:
        if temp>=40:
         print(f"Hot Days before alert: {count}")
         print(f"Alert! Extreme temperature {temp}°C detected on Day {day+1}")
         break
        count+=1




