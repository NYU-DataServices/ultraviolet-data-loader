"""List all communities in the UltraViolet environment."""
import requests
from invoke import task

from tasks.helpers import json_headers, environment_config


@task(
    help={
        "environment": "Target UltraViolet environment",
    },
    optional=["environment"],
)
def list_all(_ctx, environment="local"):
    """
    Lists all Communities
    """
    with environment_config(environment) as config:
        response = requests.get(
            "{0}/api/communities".format(config["BASE_URL"]),
            headers=json_headers(config["ACCESS_TOKEN"]),
            verify=False,
        )

        hits = response.json()["hits"]["hits"]
        for hit in hits:
            print("\n# {0} ({1})\n".format(hit["metadata"]["title"], hit["slug"]))
            print("Subcommunities: {0}".format(hit["children"]["allow"]))
