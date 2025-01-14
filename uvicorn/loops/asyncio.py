import asyncio
import logging
import sys

logger = logging.getLogger("uvicorn.error")


def asyncio_setup(use_subprocess: bool = False) -> None:  # pragma: no cover
    if sys.platform == "win32" and use_subprocess:
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
