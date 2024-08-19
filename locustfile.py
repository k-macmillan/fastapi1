"""Performance test file."""

from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    """Contains methods to be tested."""

    @task
    def single(self) -> None:
        """Send single notification request."""
        self.client.post(
            "/v1/notifications/",
            json={"to": "somebody"}
        )

    # @task
    # def multiple(self) -> None:
    #     """Send 100 notification requests."""
    #     self.client.post(
    #         "/v1/notifications/multiple",
    #         json=[
    #             {"to": "somebody", "personalization": {"hey": "now"}},
    #             {"to": "once", "personalization": {"youre": "an"}},
    #             {"to": "told", "personalization": {"all": "star"}},
    #             {"to": "me", "personalization": {"get": "your"}},
    #             {"to": "the", "personalization": {"game": "on"}},
    #             {"to": "world", "personalization": {"go": "play"}},
    #             {"to": "is", "personalization": {"hey": "now"}},
    #             {"to": "gonna", "personalization": {"youre": "a"}},
    #             {"to": "roll", "personalization": {"rock": "star"}},
    #             {"to": "me"},
    #             {"to": "somebody", "personalization": {"hey": "now"}},
    #             {"to": "once", "personalization": {"youre": "an"}},
    #             {"to": "told", "personalization": {"all": "star"}},
    #             {"to": "me", "personalization": {"get": "your"}},
    #             {"to": "the", "personalization": {"game": "on"}},
    #             {"to": "world", "personalization": {"go": "play"}},
    #             {"to": "is", "personalization": {"hey": "now"}},
    #             {"to": "gonna", "personalization": {"youre": "a"}},
    #             {"to": "roll", "personalization": {"rock": "star"}},
    #             {"to": "me"},
    #             {"to": "somebody", "personalization": {"hey": "now"}},
    #             {"to": "once", "personalization": {"youre": "an"}},
    #             {"to": "told", "personalization": {"all": "star"}},
    #             {"to": "me", "personalization": {"get": "your"}},
    #             {"to": "the", "personalization": {"game": "on"}},
    #             {"to": "world", "personalization": {"go": "play"}},
    #             {"to": "is", "personalization": {"hey": "now"}},
    #             {"to": "gonna", "personalization": {"youre": "a"}},
    #             {"to": "roll", "personalization": {"rock": "star"}},
    #             {"to": "me"},
    #             {"to": "somebody", "personalization": {"hey": "now"}},
    #             {"to": "once", "personalization": {"youre": "an"}},
    #             {"to": "told", "personalization": {"all": "star"}},
    #             {"to": "me", "personalization": {"get": "your"}},
    #             {"to": "the", "personalization": {"game": "on"}},
    #             {"to": "world", "personalization": {"go": "play"}},
    #             {"to": "is", "personalization": {"hey": "now"}},
    #             {"to": "gonna", "personalization": {"youre": "a"}},
    #             {"to": "roll", "personalization": {"rock": "star"}},
    #             {"to": "me"},
    #             {"to": "somebody", "personalization": {"hey": "now"}},
    #             {"to": "once", "personalization": {"youre": "an"}},
    #             {"to": "told", "personalization": {"all": "star"}},
    #             {"to": "me", "personalization": {"get": "your"}},
    #             {"to": "the", "personalization": {"game": "on"}},
    #             {"to": "world", "personalization": {"go": "play"}},
    #             {"to": "is", "personalization": {"hey": "now"}},
    #             {"to": "gonna", "personalization": {"youre": "a"}},
    #             {"to": "roll", "personalization": {"rock": "star"}},
    #             {"to": "me"},
    #             {"to": "somebody", "personalization": {"hey": "now"}},
    #             {"to": "once", "personalization": {"youre": "an"}},
    #             {"to": "told", "personalization": {"all": "star"}},
    #             {"to": "me", "personalization": {"get": "your"}},
    #             {"to": "the", "personalization": {"game": "on"}},
    #             {"to": "world", "personalization": {"go": "play"}},
    #             {"to": "is", "personalization": {"hey": "now"}},
    #             {"to": "gonna", "personalization": {"youre": "a"}},
    #             {"to": "roll", "personalization": {"rock": "star"}},
    #             {"to": "me"},
    #             {"to": "somebody", "personalization": {"hey": "now"}},
    #             {"to": "once", "personalization": {"youre": "an"}},
    #             {"to": "told", "personalization": {"all": "star"}},
    #             {"to": "me", "personalization": {"get": "your"}},
    #             {"to": "the", "personalization": {"game": "on"}},
    #             {"to": "world", "personalization": {"go": "play"}},
    #             {"to": "is", "personalization": {"hey": "now"}},
    #             {"to": "gonna", "personalization": {"youre": "a"}},
    #             {"to": "roll", "personalization": {"rock": "star"}},
    #             {"to": "me"},
    #             {"to": "somebody", "personalization": {"hey": "now"}},
    #             {"to": "once", "personalization": {"youre": "an"}},
    #             {"to": "told", "personalization": {"all": "star"}},
    #             {"to": "me", "personalization": {"get": "your"}},
    #             {"to": "the", "personalization": {"game": "on"}},
    #             {"to": "world", "personalization": {"go": "play"}},
    #             {"to": "is", "personalization": {"hey": "now"}},
    #             {"to": "gonna", "personalization": {"youre": "a"}},
    #             {"to": "roll", "personalization": {"rock": "star"}},
    #             {"to": "me"},
    #             {"to": "somebody", "personalization": {"hey": "now"}},
    #             {"to": "once", "personalization": {"youre": "an"}},
    #             {"to": "told", "personalization": {"all": "star"}},
    #             {"to": "me", "personalization": {"get": "your"}},
    #             {"to": "the", "personalization": {"game": "on"}},
    #             {"to": "world", "personalization": {"go": "play"}},
    #             {"to": "is", "personalization": {"hey": "now"}},
    #             {"to": "gonna", "personalization": {"youre": "a"}},
    #             {"to": "roll", "personalization": {"rock": "star"}},
    #             {"to": "me"},
    #             {"to": "somebody", "personalization": {"hey": "now"}},
    #             {"to": "once", "personalization": {"youre": "an"}},
    #             {"to": "told", "personalization": {"all": "star"}},
    #             {"to": "me", "personalization": {"get": "your"}},
    #             {"to": "the", "personalization": {"game": "on"}},
    #             {"to": "world", "personalization": {"go": "play"}},
    #             {"to": "is", "personalization": {"hey": "now"}},
    #             {"to": "gonna", "personalization": {"youre": "a"}},
    #             {"to": "roll", "personalization": {"rock": "star"}},
    #             {"to": "me"},
    #         ]
    #     )


    # @task(1)
    # def heartbeat(self) -> None:
    #     """Heartbeat request."""
    #     self.client.get("/status/heartbeat")


    # @task(1)
    # def single_with_lookup(self) -> None:
    #     """Send single notification request."""
    #     resp = self.client.post(
    #         "/v1/notifications/",
    #         json={"to": "somebody"}
    #     )
    #     self.client.get(f'/v1/notifications/{resp.json()["id"]}')

    # @task
    # def get_single(self) -> None:
    #     """Send single notification request."""
    #     self.client.get(
    #         "/v1/notifications/19e9f957-b1f6-49b6-b40e-b5d627055b00",  # Invalid
    #     )

    # @task
    # def invalid(self) -> None:
    #     """Send single notification request."""
    #     self.client.post(
    #         "/v1/notifications/",
    #         json={"oopsie": ""}
    #     )
