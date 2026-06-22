from openai import OpenAI

class Employee:

    def __init__(self, role, system_prompt):
        self.role = role
        self.system_prompt = system_prompt

        self.client = OpenAI(
            api_key="YOUR_API_KEY"
        )

    def work(self, task):

        response = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": self.system_prompt
                },
                {
                    "role": "user",
                    "content": task
                }
            ]
        )

        return response.choices[0].message.content
