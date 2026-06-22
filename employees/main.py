from employees.pm import PM
from employees.designer import Designer
from employees.frontend import Frontend
from employees.backend import Backend
from employees.qa import QA

idea = """
Build a Resume Optimization SaaS
"""

pm = PM()
designer = Designer()
frontend = Frontend()
backend = Backend()
qa = QA()

print("PM Working...")
prd = pm.work(idea)

print("Designer Working...")
design = designer.work(prd)

print("Frontend Working...")
frontend_code = frontend.work(prd)

print("Backend Working...")
backend_code = backend.work(prd)

print("QA Working...")
test_cases = qa.work(prd)

print("Done.")
