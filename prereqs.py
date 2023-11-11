# NOTE: run prereqsstore.py periodically

def get(course: str):
    with open("prereqs.csv", "r") as f:
        for line in f:
            s = line.split(", ")
            if course == s[0]:
                return ", ".join(s[1:]).strip()