from openai import OpenAI
from apps.config import get_settings

class Assistants():

    def __init__(self):
        
        self.client = OpenAI(api_key=get_settings().openai_key)


    def create_assistant(self, instructions, name, tools, model):

        my_assistant = self.client.beta.assistants.create(
            instructions=instructions,
            name=name,
            tools=tools,
            model=model,
        )

        return my_assistant
    

    def list_assistants(self, order, limit):
        
        my_assistants = self.client.beta.assistants.list(
            order=order,
            limit=limit,
        )

        return my_assistants
    

    def retrieve_assistant(self, assistant_id):

        my_assistant = self.client.beta.assistants.retrieve(assistant_id)

        return my_assistant
    

    def modify_assistant(self, assistant_id, instructions, name, tools, model):

        my_updated_assistant = self.client.beta.assistants.update(
            assistant_id,
            instructions=instructions,
            name=name,
            tools=tools,
            model=model
        )

        return my_updated_assistant
    

    def delete_assistant(self, assistant_id):

        response = self.client.beta.assistants.delete("asst_abc123")
    
        return response


    


                
    #    my_assistant = self.client.beta.assistants.create(
    #     instructions="You are a personal math tutor. When asked a question, write and run Python code to answer the question.",
    #     name="Math Tutor",
    #     tools=[{"type": "code_interpreter"}],
    #     model="gpt-4-turbo",
