"""Create a draft record in the UltraViolet environment."""
import json
import sys
from json import JSONDecodeError

import requests
from invoke import task

from tasks.helpers import json_headers, minimal_record, environment_config


@task(
    help={
        "environment": "Target UltraViolet environment",
        "file-path": "Path to JSON file containing the record data. If not provided, a minimal record will be created.",
    },
    optional=["environment", "file_path"],
)
def create_draft(_ctx, environment="local", file_path=None):
    """
    Create a draft record
    """
    with environment_config(environment) as config:
        data = ""

        if file_path is None:
            data = json.dumps(minimal_record())
        else:
            with open(file_path, "r") as file:
                data = file.read()

                try:
                    json.loads(data)
                except JSONDecodeError as err:
                    print("Error parsing {0} - {1}".format(file_path, err))
                    sys.exit(1)

        draft_response = requests.post(
            "{0}/api/records".format(config["BASE_URL"]),
            headers=json_headers(config["ACCESS_TOKEN"]),
            data=data,
            verify=False,
        )

        draft_response.raise_for_status()

        print("Draft Response Code: {0}".format(draft_response.status_code))

        draft_id = draft_response.json()["id"]
        print("Draft Record ID: {0}".format(draft_id))
        return draft_id
