"""Performance test file."""

from locust import HttpUser, task


class HelloWorldUser(HttpUser):
    """Contains methods to be tested."""

    # @task
    # def single(self) -> None:
    #     """Send single notification request."""
    #     self.client.post(
    #         "/notifications/v1/",
    #         json={"to": "somebody"}
    #     )

    @task
    def single_multiple(self) -> None:
        """Send 100 notification requests."""
        self.client.post(
            "/notifications/v1/multiple",
            json=[
                {"to": "somebody", "personalization": {"hey": "now"}},
                {"to": "once", "personalization": {"youre": "an"}},
                {"to": "told", "personalization": {"all": "star"}},
                {"to": "me", "personalization": {"get": "your"}},
                {"to": "the", "personalization": {"game": "on"}},
                {"to": "world", "personalization": {"go": "play"}},
                {"to": "is", "personalization": {"hey": "now"}},
                {"to": "gonna", "personalization": {"youre": "a"}},
                {"to": "roll", "personalization": {"rock": "star"}},
                {"to": "me"},
                {"to": "somebody", "personalization": {"hey": "now"}},
                {"to": "once", "personalization": {"youre": "an"}},
                {"to": "told", "personalization": {"all": "star"}},
                {"to": "me", "personalization": {"get": "your"}},
                {"to": "the", "personalization": {"game": "on"}},
                {"to": "world", "personalization": {"go": "play"}},
                {"to": "is", "personalization": {"hey": "now"}},
                {"to": "gonna", "personalization": {"youre": "a"}},
                {"to": "roll", "personalization": {"rock": "star"}},
                {"to": "me"},
                {"to": "somebody", "personalization": {"hey": "now"}},
                {"to": "once", "personalization": {"youre": "an"}},
                {"to": "told", "personalization": {"all": "star"}},
                {"to": "me", "personalization": {"get": "your"}},
                {"to": "the", "personalization": {"game": "on"}},
                {"to": "world", "personalization": {"go": "play"}},
                {"to": "is", "personalization": {"hey": "now"}},
                {"to": "gonna", "personalization": {"youre": "a"}},
                {"to": "roll", "personalization": {"rock": "star"}},
                {"to": "me"},
                {"to": "somebody", "personalization": {"hey": "now"}},
                {"to": "once", "personalization": {"youre": "an"}},
                {"to": "told", "personalization": {"all": "star"}},
                {"to": "me", "personalization": {"get": "your"}},
                {"to": "the", "personalization": {"game": "on"}},
                {"to": "world", "personalization": {"go": "play"}},
                {"to": "is", "personalization": {"hey": "now"}},
                {"to": "gonna", "personalization": {"youre": "a"}},
                {"to": "roll", "personalization": {"rock": "star"}},
                {"to": "me"},
                {"to": "somebody", "personalization": {"hey": "now"}},
                {"to": "once", "personalization": {"youre": "an"}},
                {"to": "told", "personalization": {"all": "star"}},
                {"to": "me", "personalization": {"get": "your"}},
                {"to": "the", "personalization": {"game": "on"}},
                {"to": "world", "personalization": {"go": "play"}},
                {"to": "is", "personalization": {"hey": "now"}},
                {"to": "gonna", "personalization": {"youre": "a"}},
                {"to": "roll", "personalization": {"rock": "star"}},
                {"to": "me"},
                {"to": "somebody", "personalization": {"hey": "now"}},
                {"to": "once", "personalization": {"youre": "an"}},
                {"to": "told", "personalization": {"all": "star"}},
                {"to": "me", "personalization": {"get": "your"}},
                {"to": "the", "personalization": {"game": "on"}},
                {"to": "world", "personalization": {"go": "play"}},
                {"to": "is", "personalization": {"hey": "now"}},
                {"to": "gonna", "personalization": {"youre": "a"}},
                {"to": "roll", "personalization": {"rock": "star"}},
                {"to": "me"},
                {"to": "somebody", "personalization": {"hey": "now"}},
                {"to": "once", "personalization": {"youre": "an"}},
                {"to": "told", "personalization": {"all": "star"}},
                {"to": "me", "personalization": {"get": "your"}},
                {"to": "the", "personalization": {"game": "on"}},
                {"to": "world", "personalization": {"go": "play"}},
                {"to": "is", "personalization": {"hey": "now"}},
                {"to": "gonna", "personalization": {"youre": "a"}},
                {"to": "roll", "personalization": {"rock": "star"}},
                {"to": "me"},
                {"to": "somebody", "personalization": {"hey": "now"}},
                {"to": "once", "personalization": {"youre": "an"}},
                {"to": "told", "personalization": {"all": "star"}},
                {"to": "me", "personalization": {"get": "your"}},
                {"to": "the", "personalization": {"game": "on"}},
                {"to": "world", "personalization": {"go": "play"}},
                {"to": "is", "personalization": {"hey": "now"}},
                {"to": "gonna", "personalization": {"youre": "a"}},
                {"to": "roll", "personalization": {"rock": "star"}},
                {"to": "me"},
                {"to": "somebody", "personalization": {"hey": "now"}},
                {"to": "once", "personalization": {"youre": "an"}},
                {"to": "told", "personalization": {"all": "star"}},
                {"to": "me", "personalization": {"get": "your"}},
                {"to": "the", "personalization": {"game": "on"}},
                {"to": "world", "personalization": {"go": "play"}},
                {"to": "is", "personalization": {"hey": "now"}},
                {"to": "gonna", "personalization": {"youre": "a"}},
                {"to": "roll", "personalization": {"rock": "star"}},
                {"to": "me"},
                {"to": "somebody", "personalization": {"hey": "now"}},
                {"to": "once", "personalization": {"youre": "an"}},
                {"to": "told", "personalization": {"all": "star"}},
                {"to": "me", "personalization": {"get": "your"}},
                {"to": "the", "personalization": {"game": "on"}},
                {"to": "world", "personalization": {"go": "play"}},
                {"to": "is", "personalization": {"hey": "now"}},
                {"to": "gonna", "personalization": {"youre": "a"}},
                {"to": "roll", "personalization": {"rock": "star"}},
                {"to": "me"},
            ]
        )


    # @task(1)
    # def heartbeat(self) -> None:
    #     """Heartbeat request."""
    #     self.client.get("/status/heartbeat")


    # @task(1)
    # def single_with_lookup(self) -> None:
    #     """Send single notification request."""
    #     resp = self.client.post(
    #         "/notifications/v1/",
    #         json={"to": "somebody"}
    #     )
    #     self.client.get(f'/v1/notifications/{resp.json()["id"]}')

    # @task
    # def get_single(self) -> None:
    #     """Send single notification request."""
    #     self.client.get(
    #         "/notifications/v1/19e9f957-b1f6-49b6-b40e-b5d627055b00",  # Invalid
    #     )

    # @task
    # def invalid(self) -> None:
    #     """Send single notification request."""
    #     self.client.post(
    #         "/notifications/v1/",
    #         json={"oopsie": ""}
    #     )
