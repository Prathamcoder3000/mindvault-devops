class Assignment:
    def __init__(self, title, subject, deadline):
        self.title = title
        self.subject = subject
        self.deadline = deadline
        self.status = "Pending"

    def complete_assignment(self):
        self.status = "Completed"

    def display_assignment(self):
        print("Title    :", self.title)
        print("Subject  :", self.subject)
        print("Deadline :", self.deadline)
        print("Status   :", self.status)


# MindVault AI Assignment Module
assignment = Assignment(
    "DevOps Practical",
    "Software Engineering",
    "10 September 2026"
)

print("===== MindVault AI =====")
print("Assignment Management Module")
print()

assignment.display_assignment()

print()
assignment.complete_assignment()

print("After completing assignment:")
assignment.display_assignment()

print("CI/CD Pipeline Working Successfully!")
