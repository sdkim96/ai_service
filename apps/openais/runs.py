from openai import OpenAI
from apps.config import get_settings

class Runs():

    def __init__(self):

        self.client = OpenAI(api_key=get_settings().openai_key)


    def create_run(self, thread_id, assistant_id):

        run = self.client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id
        )

        return run
    

    def list_runs(self, thread_id):

        runs = self.client.beta.threads.runs.list(thread_id=thread_id)

        return runs
    

    def retrieve_run(self, thread_id, run_id):

        run = self.client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id)

        return run