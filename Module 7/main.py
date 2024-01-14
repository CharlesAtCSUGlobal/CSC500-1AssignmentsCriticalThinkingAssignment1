# Define Course
class Course:

    def __init__(self, course_number, course_room, course_instructor, course_time):
        self.number = course_number
        self.room = course_room
        self.instructor = course_instructor
        self.time = course_time

    def print_course_info(self):
        print(
            '''\n{number} 
    Room:       {room} 
    Instructor: {instructor} 
    Time:       {time}
'''.format(number=self.number, room=self.room, instructor=self.instructor, time=self.time, ))


# Define course dictionaries

courses_available = ["CSC101", "CSC102", "CSC103", "NET110", "COM241"]

course_rooms = [{"courseNumber": "CSC101", "roomNumber": "3004"},
                {"courseNumber": "CSC102", "roomNumber": "4501"},
                {"courseNumber": "CSC103", "roomNumber": "6755"},
                {"courseNumber": "NET110", "roomNumber": "1244"},
                {"courseNumber": "COM241", "roomNumber": "1411"}
                ]

course_instructors = [{"courseNumber": "CSC101", "instructor": "Haynes"},
                      {"courseNumber": "CSC102", "instructor": "Alvarado"},
                      {"courseNumber": "CSC103", "instructor": "Rich"},
                      {"courseNumber": "NET110", "instructor": "Burke"},
                      {"courseNumber": "COM241", "instructor": "Lee"}
                      ]

course_times = [{"courseNumber": "CSC101", "time": "8:00 a.m."},
                {"courseNumber": "CSC102", "time": "9:00 a.m."},
                {"courseNumber": "CSC103", "time": "10:00 a.m."},
                {"courseNumber": "NET110", "time": "11:00 a.m."},
                {"courseNumber": "COM241", "time": "1:00 p.m."}
                ]


# Define functions

def find_in_dictionary(dictionary, number, lookup):
    item = ""
    for i in dictionary:
        if i["courseNumber"] == number:
            item = i[lookup]
            break
    if item == "":
        raise Exception("Course Not Found, data may be incomplete")
    return item


def lookup_course_info(number):
    room = find_in_dictionary(course_rooms, number, "roomNumber")
    instructor = find_in_dictionary(course_instructors, number, "instructor")
    time = find_in_dictionary(course_times, number, "time")

    return Course(number, room, instructor, time)



def print_menu():
    print("Welcome to Course Catalog\n")
    print('''MENU
    d - Display Available Courses
    i - Show Course Info
    q - Quit''')


# Main function

menu_choice = ""
while menu_choice.lower() != "q":
    print_menu()
    menu_choice = input("Choose an option:")
    if menu_choice.lower() == "d":
        for c in courses_available:
            print("   {number}".format(number=c))
        print("\n")
    elif menu_choice.lower() == "i":
        input_number = input("Please enter course selection:")

        try:
            course_info = lookup_course_info(input_number)
            course_info.print_course_info()

        except Exception as e:
            print("Course Not Found! Please try again")

    elif menu_choice.lower() != "q":
        print("\nUnknown Option, Please try again.\n")

# 'quit' selected
print("Exiting program...")

