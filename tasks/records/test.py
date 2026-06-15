"""Test access to an environment."""
import requests
from invoke import task

from tasks.helpers import json_headers, environment_config


@task(
    help={
        "environment": "Target UltraViolet environment",
    },
    optional=["environment"],
)
def test(_ctx, environment="local"):
    """
    Tests access to an environment by listing the number of records.
    """
    with environment_config(environment) as config:
        response = requests.get(
            "{0}/api/records".format(config["BASE_URL"]),
            headers=json_headers(config["ACCESS_TOKEN"]),
            verify=False,
        )

        print("{0} records found.".format(response.json()["hits"]["total"]))
