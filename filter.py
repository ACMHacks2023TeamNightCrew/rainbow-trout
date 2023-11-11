import json
import prereqs

def _possible(course: str, taken: list):
    # if course is in list of taken then return false
    # if not all prereqs in list of taken then return false
    # if all course's prereqs are in list of taken then return true

    if course in taken:
        return False
    # getPreReq is a filler wait for code
    for prereq in prereqs.get(course):
        if prereq not in taken:
            return False
    return True

# Returns a list of courses that is available to the user
def courses(major: str, taken: list):
    file = open("static/majorLists/" + major + ".json", "r")
    jsonstring = file.read()
    courseList = json.loads(jsonstring)
    file.close()
    possible = []
    for course in courseList:
        if _possible(course, taken):
            possible.append(course)
    return possible

print(courses("Computer Science B.S.", ["CSE 12", "CSE 20"]))