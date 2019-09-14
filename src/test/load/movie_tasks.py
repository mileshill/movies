from locust import HttpLocust, TaskSet, task
from random import choice


class GetMovies(TaskSet):
    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task(1)
    def all_movies(self):
        self.client.get("/movies")

    @task(2)
    def movies_by_year(self):
        year = choice(range(1900, 2018))
        self.client.get(f"/movies/{year}", name="/movies/year")


class MovieLocust(HttpLocust):
    task_set = GetMovies
    min_wait=2000
    max_wait=10000
