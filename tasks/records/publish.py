"""Publish a draft record."""
import requests
from invoke import task

from tasks.helpers import json_headers, environment_config


@task(
    help={
        "draft-id": "The ID of the draft record to publish",
        "environment": "Target UltraViolet environment",
    },
    optional=["environment"],
)
def publish(_ctx, draft_id, environment="local"):
    """
    Publish a draft record
    """
    with environment_config(environment) as config:
        publish_response = requests.post(
            "{0}/api/records/{1}/draft/actions/publish".format(
                config["BASE_URL"], draft_id
            ),
            headers=json_headers(config["ACCESS_TOKEN"]),
            verify=False,
        )

        publish_response.raise_for_status()

        print("Publish Response Code: {0}".format(publish_response.status_code))

        record_id = publish_response.json()["id"]
        print("Record ID: {0}".format(record_id))
