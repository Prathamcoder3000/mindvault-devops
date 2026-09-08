from assignment import Assignment


def test_assignment_creation():
    assignment = Assignment(
        "DevOps Practical",
        "Software Engineering",
        "10 September 2026"
    )

    assert assignment.title == "DevOps Practical"
    assert assignment.subject == "Software Engineering"
    assert assignment.deadline == "10 September 2026"
    assert assignment.status == "Pending"


def test_complete_assignment():
    assignment = Assignment(
        "DevOps Practical",
        "Software Engineering",
        "10 September 2026"
    )

    assignment.complete_assignment()

    assert assignment.status == "Completed"
