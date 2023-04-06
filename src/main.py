
import flet as ft
import os, openai
openai.api_key = os.getenv("OPENAI_API_KEY")


conversation = []

class ChatGPT:  
    

    def __init__(self):
        self.messages = conversation
        self.model = os.getenv("OPENAI_MODEL", default = "gpt-3.5-turbo")



    def get_response(self, user_input):
        conversation.append({"role": "user", "content": user_input})
        

        response = openai.ChatCompletion.create(
	            model=self.model,
                messages = self.messages

                )

        conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
        
        print("AI回答內容：")        
        print(response['choices'][0]['message']['content'].strip())


        
        return response['choices'][0]['message']['content'].strip()


chatgpt = ChatGPT()




def main(page: ft.Page):
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Please enter your prompt"
            page.update()
        else:
            name = txt_name.value
            ai_reply_response = chatgpt.get_response(name)
            page.clean()
            page.add(ft.Text(f"ChatGPT AI: {ai_reply_response}"))

    txt_name = ft.TextField(label="Your prompt")

    page.add(txt_name, ft.ElevatedButton("Generate!", on_click=btn_click))

ft.app(target=main, view=None, port=8502)
'''

import flet
from flet import IconButton, Page, Row, TextField, icons

def main(page: Page):
    page.title = "Flet counter example"
    page.vertical_alignment = "center"

    txt_number = TextField(value="0", text_align="right", width=100)

    def minus_click(e):
        txt_number.value = int(txt_number.value) - 1
        page.update()

    def plus_click(e):
        txt_number.value = int(txt_number.value) + 1
        page.update()

    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=minus_click),
                txt_number,
                IconButton(icons.ADD, on_click=plus_click),
            ],
            alignment="center",
        )
    )

#flet.app(target=main)
#flet.app(target=main, view=flet.WEB_BROWSER) 
flet.app(target=main, view=None, port=8502)
'''

