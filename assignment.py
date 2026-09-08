def create_assignment(title, subject):
    return {
        "title": title,
        "subject": subject,
        "status": "Pending"
    }


assignment = create_assignment(
    "Complete DevOps Practical",
    "Software Engineering"
)

print("MindVault AI - Assignment Module")
print(assignment)
