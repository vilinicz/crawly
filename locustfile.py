from locust import task, HttpUser


class UserBehavior(HttpUser):
    @task
    def search(self):
        self.client.get("search", params={"q": "python", "engines": ["bing"]})
