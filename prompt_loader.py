from pathlib import Path

PROMPT_DIR = Path("prompts")

def load_prompt(name):

    path = PROMPT_DIR / f"{name}.txt"

    with open(path, "r", encoding="utf8") as f:
        return f.read()
