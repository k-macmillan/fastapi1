"""Status routes."""

from time import monotonic
from typing import Any, Callable, Coroutine

from fastapi import APIRouter, HTTPException, Request, status
from fastapi.responses import Response
from fastapi.routing import APIRoute

from fastapi1.app_logging import logger


class StatusRoute(APIRoute):
    """Exception and logging handling."""

    def get_route_handler(self) -> Callable[[Request], Coroutine[Any, Any, Response]]:
        """Override default handler.

        Returns
        -------
            Callable: the route handler

        """
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            status_code = None
            try:
                start = monotonic()
                resp = await original_route_handler(request)
                status_code = resp.status_code
                return resp
            except Exception as exc:
                status_code = 500
                logger.exception("UNKNOWN EXCEPTION: %s %s", type(exc), exc)
                raise HTTPException(status_code, str(exc))
            finally:
                # Is there any chance request would not be available?
                logger.info("%s %s %s %ss", request.method, request.url, status_code, f"{(monotonic() - start):6f}")

        return custom_route_handler


status_router = APIRouter(
    prefix="/status",
    tags=["System Status"],
    responses={404: {"description": "Not found"}},
    route_class=StatusRoute,
)


@status_router.get("/heartbeat", status_code=status.HTTP_204_NO_CONTENT)
def system_heartbeat() -> None:
    """Heartbeat."""
    pass
