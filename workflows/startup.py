from workflows.base import BaseWorkflow

from employees.pm import PM
from employees.designer import Designer
from employees.frontend import Frontend
from employees.backend import Backend
from employees.qa import QA


class StartupWorkflow(BaseWorkflow):

    def run(self, idea):

        self.log("CEO: Starting Startup Workflow")

        pm = PM()
        prd = pm.work(idea)
        self.save("prd.md", prd)

        designer = Designer()
        design = designer.work(prd)
        self.save("design.md", design)

        frontend = Frontend()
        frontend_code = frontend.work(prd)
        self.save("frontend.md", frontend_code)

        backend = Backend()
        backend_code = backend.work(prd)
        self.save("backend.md", backend_code)

        qa = QA()
        tests = qa.work(prd)
        self.save("tests.md", tests)

        return {
            "prd": prd,
            "design": design,
            "frontend": frontend_code,
            "backend": backend_code,
            "tests": tests
        }
