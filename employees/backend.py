from employees.base import Employee

class Backend(Employee):

    def __init__(self):

        super().__init__(
            role="Backend Engineer",
            system_prompt="""
You are a senior backend engineer.

Generate:

- FastAPI
- PostgreSQL
- JWT Auth
- REST APIs

Return complete source code.
"""
        )
