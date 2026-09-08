from assignment import create_assignment


def test_create_assignment():
    assignment = create_assignment(
        "Complete DevOps Practical",
        "Software Engineering"
    )

    assert assignment["title"] == "Complete DevOps Practical"
    assert assignment["subject"] == "Software Engineering"
    assert assignment["status"] == "Pending"
