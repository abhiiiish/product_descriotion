import openai
import gradio as gr

#set key
from dotenv.main import load_dotenv
import os
load_dotenv()
openai.api_key = os.environ['openai_key']

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant. and you have to generate description"},
]

def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply

inputs = gr.inputs.Textbox(lines=7, label="Put your details here")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Generate description",
             description="Ask anything you want",
             theme="compact").launch(share=True)
