from openai import OpenAI
from apps.config import get_settings

class Threads():

    def __init__(self):

        self.client = OpenAI(api_key=get_settings().openai_key)

    
    def create_thread(self):

        empty_thread = self.client.beta.threads.create()

        return empty_thread
    

    def retrieve_thread(self, thread_id):

        my_thread = self.client.beta.threads.retrieve(thread_id)

        return my_thread
    

    def delete_thread(self, thread_id):

        response = self.client.beta.threads.delete(thread_id)

        return response