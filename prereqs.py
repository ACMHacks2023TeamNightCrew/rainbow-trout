# NOTE: run prereqsstore.py periodically

def get(course: str):
    with open("prereqs.csv", "r") as f:
        for line in f:
            s = line.strip().split(", ")
            if course == s[0]:
                for i in range(len(s)):
                    s[i].strip("\n")
                return s[1:]
    return []