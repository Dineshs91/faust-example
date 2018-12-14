import faust

from faustapp import app


class Vote(faust.Record):
    vote: bool


@app.agent()
async def poll_voted(votes):
    async for vote in votes:
        print("Vote received", vote)


@app.timer(interval=1.0)
async def example_sender(app):
    await poll_voted.send(
        value=Vote(vote=True),
    )
