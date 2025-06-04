import requests
from dotenv import load_dotenv
load_dotenv()
flic_token=os.getenv("Flic_Token")
def get_socialverse_posts():
    url = "https://api.socialverseapp.com/posts/summary/get?page=1&page_size=1000"
    headers = {
        "Flic-Token": flic_token
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()  
    else:
        return {"error": response.status_code, "message": response.text}

