
from ctransformers import AutoModelForCausalLM
import gradio as gr


model_name = "TheBloke/Mistral-7B-OpenOrca-GGUF"
llm = AutoModelForCausalLM.from_pretrained(model_name, model_type="llama")



def chatgpt(message, history):
    history_log = []
    for human, assistant in history:
        history_log.append({"role": "user", "content": human })
        history_log.append({"role": "assistant", "content":assistant})
    history_log.append({"role": "user", "content": message})
    response = llm(message)
    yield response


gr.ChatInterface(chatgpt).queue().launch(auth=("admin", "pass"))


