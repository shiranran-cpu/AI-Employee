from employees.base import Employee

class QA(Employee):

    def __init__(self):

        super().__init__(
            role="QA Engineer",
            system_prompt="""
You are a senior QA engineer.

Generate:

- Test Plan
- Test Cases
- Pytest Code
- Bug Reports
"""
        )
