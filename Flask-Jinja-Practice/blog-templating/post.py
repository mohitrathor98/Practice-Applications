import requests
class Post:
    def __init__(self):
        self.url = "https://api.npoint.io/80b7a3998e15140acf88"
        self.data = None
        
    def getData(self):
        res = requests.get(self.url)
        print("Response: ", res.status_code)
        self.data = res.json()
        return self.data
    
    def getPostById(self, id):
        if self.data is None:
            self.getData()
        
        for post in self.data:
            if int(post["id"]) == int(id):
                return post
