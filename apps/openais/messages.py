from openai import OpenAI
from apps.config import get_settings

class Messages():

    def __init__(self):
        
        self.client = OpenAI(api_key=get_settings().openai_key)


    def create_message(self, thread_id, role, content):

        thread_message = self.client.beta.threads.messages.create(
            thread_id,
            role=role,
            content=content,
        )

        return thread_message
    

    def list_messages(self, thread_id):

        thread_messages = self.client.beta.threads.messages.list(thread_id)
        print("TREAD MESSAGE : ",thread_messages)
        print("----------------------------------")
        return thread_messages
    

    def retrieve_message(self, thread_id, message_id):

        message = self.client.beta.threads.messages.retrieve(
            message_id=message_id,
            thread_id=thread_id,
        )

        return message
    
    