from employees.base import Employee

class PM(Employee):

    def __init__(self):

        super().__init__(
            role="Product Manager",
            system_prompt="""
You are a senior product manager.

Write:
1. Product Overview
2. Target Users
3. Core Features
4. User Stories
5. Roadmap
"""
        )
