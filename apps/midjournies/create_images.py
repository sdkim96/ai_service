from apps.config import get_settings
import requests

class Midjourneies():
    
    def __init__(self):
        self.midjourney_key = get_settings().midjourney_key

    
    def create_image(self, prompt: str):
        
        key = self.midjourney_key

        data = {
            "prompt": prompt,
        }

        response = requests.post(
            f"https://api.midjourney.com/v1/images",
            headers={
                "Authorization": f"Bearer {key}",
                "Content-Type": "application/json"
            },
            json=data)
        
        return response.json()
    

    def show_image(self, message_id):
            
            key = self.midjourney_key
    
            response = requests.get(
                f"https://api.midjourney.com/v1/images/{message_id}",
                headers={
                    "Authorization": f"Bearer {key}",
                })
            
            return response.json()