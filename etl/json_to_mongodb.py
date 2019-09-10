import json
import logging

from pymongo import MongoClient


class JsonToMongoDB:

    async def migrate(self):
        dict_data = await self._json_to_dict()
        await self._dict_elements_to_mongodb(dict_data)

    @staticmethod
    async def _json_to_dict() -> dict:
        with open("trips-light.json") as json_file:
            return json.load(json_file)

    async def _dict_elements_to_mongodb(self, dict_data: dict) -> None:
        collection = await self._get_collection()
        collection.insert_many(dict_data["trips"])
        logging.info("Migration Success !")

    @staticmethod
    async def _get_collection():
        client = MongoClient()
        db = client.test
        return db.trips
