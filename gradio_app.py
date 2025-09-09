import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load tokenizer and model globally
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-1.5", trust_remote_code=True)
llm_model = AutoModelForCausalLM.from_pretrained("microsoft/phi-1.5", trust_remote_code=True)


def generate_answer(question):
    prompt = "Answer the following question: " + question
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    # Generate response
    output = llm_model.generate(
        input_ids,
        max_length=512,
        do_sample=True,
        top_k=50,
        top_p=0.9
    )[0]

    answer = tokenizer.decode(output, skip_special_tokens=True)
    end_of_text_index = answer.find("(end of text)")
    if end_of_text_index > -1:
        answer = answer[:end_of_text_index]
    return answer.strip()


def chatbot(question):
    return generate_answer(question)


if __name__ == "__main__":
    with gr.Blocks(css="""
        body {background-color: #f0f8ff; font-family: 'Arial', sans-serif;}
        .gradio-container {max-width: 700px; margin: auto; border-radius: 15px; padding: 20px; background-color: #ffffff; box-shadow: 0px 8px 20px rgba(0,0,0,0.1);}
        h1 {color: #007acc;}
        .description {color: #555555;}
        .input-box, .output-box {border-radius: 10px; border: 1px solid #ccc; padding: 10px;}
        .gr-button {background-color: #00bfff; color: white; border-radius: 10px; border: none;}
        .gr-button:hover {background-color: #009acd;}
    """) as demo:
        gr.Markdown("<h1>I am your AI Health Assistance 🏥</h1>")
        gr.Markdown("<p class='description'>Ask general health related questions to the AI Bot.</p>")

        with gr.Row():
            question_input = gr.Textbox(placeholder="Type your health question here...", lines=2, label="Your Question")
            answer_output = gr.Textbox(label="AI Answer", interactive=False)

        ask_button = gr.Button("Ask AI")
        ask_button.click(fn=chatbot, inputs=question_input, outputs=answer_output)

    demo.launch()
