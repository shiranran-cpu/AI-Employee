import gradio as gr

from workflows.startup import StartupWorkflow

workflow = StartupWorkflow()


def generate_company(idea):

    result = workflow.run(idea)

    return (
        result["prd"],
        result["design"],
        result["frontend"][:5000],
        result["backend"][:5000]
    )


with gr.Blocks() as demo:

    gr.Markdown(
        """
        # 🏢 AI Employee

        Hire AI employees.
        Build products in minutes.
        """
    )

    idea = gr.Textbox(
        label="Startup Idea",
        lines=4
    )

    btn = gr.Button("🚀 Build Company")

    prd = gr.Textbox(label="PRD")
    design = gr.Textbox(label="Design")
    frontend = gr.Textbox(label="Frontend")
    backend = gr.Textbox(label="Backend")

    btn.click(
        generate_company,
        inputs=idea,
        outputs=[
            prd,
            design,
            frontend,
            backend
        ]
    )

demo.launch()
