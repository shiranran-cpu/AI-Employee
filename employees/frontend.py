from employees.base import Employee

class Frontend(Employee):

    def __init__(self):

        super().__init__(
            role="Frontend Engineer",
            system_prompt="""
You are a senior React engineer.

Generate:

- React
- Next.js
- TypeScript
- TailwindCSS

Return complete source code.
"""
        )
