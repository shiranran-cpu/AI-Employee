from employees.base import Employee

class Designer(Employee):

    def __init__(self):

        super().__init__(
            role="UI Designer",
            system_prompt="""
You are a professional UI designer.

Generate:

- Wireframe
- UI Layout
- Color Scheme
- User Flow

Output in Markdown.
"""
        )
