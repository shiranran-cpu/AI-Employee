from pathlib import Path

class BaseWorkflow:

    def __init__(self):

        self.output_dir = Path("outputs")
        self.output_dir.mkdir(exist_ok=True)

    def save(self, name, content):

        path = self.output_dir / name

        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    def log(self, msg):
        print(msg)
