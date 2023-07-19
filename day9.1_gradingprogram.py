student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
def grade(score):
    if score > 90 : grade = "Outstanding"
    elif score > 80 : grade = "Exceeds Expectations"
    elif score > 70 : grade = "Acceptable"
    else : grade = "Fail"
    return grade

for student in student_scores:
   # print(student, grade(student_scores[student]))
    student_grades[student] = grade(student_scores[student])

# 🚨 Don't change the code below 👇
print(student_grades)

# Nesting

# list in a dictionary
travel_log = {
    "France": ["Paris", "Lille":, "Dijon"],
    "Germany": ["Berlin", "Hamburg"]
}

# Dictionary in dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille":, "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited":["Berlin", "Hamburg"], "total_visits": 2}
}

# Nesting Dictionary in a List

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille":, "Dijon"], 
        "total_visits": 12
    },
    {
        "country" : "Germany", 
        "cities_visited":["Berlin", "Hamburg"], 
        "total_visits": 2
    }
]


#This is the scoring criteria:
#Scores 91 - 100: Grade = "Outstanding"
#Scores 81 - 90: Grade = "Exceeds Expectations"
#Scores 71 - 80: Grade = "Acceptable"
#Scores 70 or lower: Grade = "Fail"
#