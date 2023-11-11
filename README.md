# rainbow-trout
A counselor/scheduler for classes.

This helps generate course lists that fit with a student's current progression in the major. As of right now, it only works for Computer Science B.S., due to peculiarities in the UCSC General Catalogue where they specify things such as "Either", "At least one of the" or "4 from the list below" in the major requirements pages, or some pages which direct a student to pick a course within a range of courses, as well as prose descriptions of course requirements, which cannot be parsed by a computer very easily. As such, we decided to simply make a course list for Computer Science because it was the major most familiar to us and from there, we have the blueprints to further build upon.

Run this project by issuing the following commands on a command line in the root directory of this repository:
```
pip install -r requirements.txt
python main.py
```

The hackathon for which this project is written, and our submission, is located here: [https://devpost.com/software/team-night-crew](https://devpost.com/software/team-night-crew)
