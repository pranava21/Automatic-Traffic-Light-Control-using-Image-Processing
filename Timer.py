import time


class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""


class Timer:
    def __init__(self):
        self._start_time = None

    def startTimer(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError("Timer is running. Use .stop() to stop it")

        self._start_time = time.perf_counter()

    def calculateTimeElapsed(self):
        elapsed_time = time.perf_counter() - self._start_time
        return elapsed_time

    def stopTimer(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError("Timer is not running. Use .start() to start it")

        self._start_time = None
