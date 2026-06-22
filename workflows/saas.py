from workflows.base import BaseWorkflow

from employees.analyst import Analyst
from employees.pm import PM
from employees.designer import Designer
from employees.frontend import Frontend
from employees.backend import Backend
from employees.qa import QA
from employees.devops import DevOps


class SaaSWorkflow(BaseWorkflow):

    def run(self, idea):

        analyst = Analyst()

        market_report = analyst.work(idea)

        self.save(
            "market_analysis.md",
            market_report
        )

        pm = PM()

        prd = pm.work(
            idea + "\n\n" + market_report
        )

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

        devops = DevOps()

        deploy = devops.work(prd)

        self.save("deploy.md", deploy)

        return {
            "market": market_report,
            "prd": prd,
            "design": design,
            "frontend": frontend_code,
            "backend": backend_code,
            "tests": tests,
            "deploy": deploy
        }
