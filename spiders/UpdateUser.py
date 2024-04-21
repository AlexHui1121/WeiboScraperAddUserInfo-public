import json
import os
import scrapy
from scrapy.exceptions import CloseSpider


class UpdateUserInfoSpider(scrapy.Spider):
    name = "updateuserinfo"

    def start_requests(self):
        origin_file_path = self.jsonl_file
        new_file_path = "output/" + self.filename.replace("keyword", "updatinguserinfo")
        check_file_path = "output/" + self.filename.replace(
            "keyword", "updateduserinfo"
        )

        if not os.path.exists(check_file_path):

            def find_missing_ids(origin_file_path, new_file_path):
                global ids_n
                with open(origin_file_path, "r", encoding="utf-8") as f:
                    ids_o = {json.loads(line)["_id"] for line in f}
                with open(new_file_path, "r", encoding="utf-8") as f:
                    ids_n = {json.loads(line)["_id"] for line in f}
                missing_ids = ids_o - ids_n
                return missing_ids

            missing_ids = find_missing_ids(origin_file_path, new_file_path)
            print(missing_ids)
            with open(origin_file_path, "r", encoding="utf-8") as file:
                for line in file:
                    try:
                        item = json.loads(line)
                        if item["_id"] in missing_ids and item["_id"] not in ids_n:
                            url = (
                                "https://weibo.com/ajax/profile/info?uid="
                                + item["user"]["_id"]
                            )
                            yield scrapy.Request(
                                url, callback=self.parse, meta={"item": item}
                            )
                    except Exception as e:
                        print(f"Error parsing line: {e}")

    def parse(self, response):
        data = json.loads(response.text)
        item = response.meta["item"]
        if data["data"]["user"]["gender"]:
            item["user"]["gender"] = data["data"]["user"]["gender"]
        if data["data"]["user"]["location"]:
            item["user"]["location"] = data["data"]["user"]["location"]

        yield item
