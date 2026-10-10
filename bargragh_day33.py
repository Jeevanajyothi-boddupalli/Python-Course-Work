import matplotlib.pyplot as mplt
subjects = ["Python", "DSA", "Aptitude", "Softskills"]
marks = [89,85,70,60]
mplt.bar(subjects,marks)
mplt.title("Students Marks Reports")
mplt.xlabel("subjects")
mplt.ylabel("marks")
mplt.show()