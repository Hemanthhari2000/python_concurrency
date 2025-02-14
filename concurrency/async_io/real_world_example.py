"""
Get Top Hacker News stories using asyncio and httpx concurrently.
"""

import asyncio
import json
import time

import httpx
import pendulum
from pydantic import BaseModel, field_validator

HACKER_NEWS_TOP_STORIES_URL = (
    "https://hacker-news.firebaseio.com/v0/topstories.json"
)
HACKER_NEWS_ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"


class Story(BaseModel):
    id: int
    title: str
    by: str
    time: str
    url: str = ""

    @field_validator("time", mode="before")
    def format_timestamp(cls, time_):
        if isinstance(time_, int):
            return pendulum.from_timestamp(time_).to_datetime_string()
        return time_


async def fetch_top_story_ids(client):
    response = await client.get(HACKER_NEWS_TOP_STORIES_URL)
    response.raise_for_status()
    return response.json()[:10]


async def fetch_story_details(client, story_id):
    response = await client.get(HACKER_NEWS_ITEM_URL.format(story_id))
    response.raise_for_status()
    response = response.json()
    return Story(**response).model_dump()


async def fetch_and_save_stories():
    async with httpx.AsyncClient() as client:
        print("Fetching top story IDs...")
        story_ids = await fetch_top_story_ids(client)

        print("Fetching story details concurrently...")
        tasks = [
            fetch_story_details(client, story_id) for story_id in story_ids
        ]
        stories = await asyncio.gather(*tasks)

    if stories:
        print("Saving stories to file...")
        with open("outputs/asyncio/hacker_news_stories.json", "w") as f:
            json.dump(stories, f, indent=4)

    print("Done! Stories saved to hacker_news_stories.json")


async def real_world_example_main():
    print("Starting execution...")
    start = time.perf_counter()

    await fetch_and_save_stories()

    print(f"Finished execution in {time.perf_counter() - start} second(s)")


if __name__ == "__main__":
    asyncio.run(real_world_example_main())
