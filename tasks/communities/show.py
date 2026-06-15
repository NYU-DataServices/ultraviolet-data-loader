"""Display details of a single community."""
import json

import requests
from invoke import task

from tasks.helpers import json_headers, environment_config


@task(
    help={
        "slug": "Slug of the environment you want to view",
        "environment": "Target UltraViolet environment",
    },
    optional=["environment"],
)
def show(_ctx, slug, environment="local"):
    """
    Displays the output of a single community
    """
    with environment_config(environment) as config:
        response = requests.get(
            "{0}/api/communities/{1}".format(config["BASE_URL"], slug),
            verify=False,
        )

        print(json.dumps(response.json(), indent=2))
