"""Enable subcommunities for a given community."""
import json

import requests
from invoke import task
from requests import HTTPError

from tasks.helpers import json_headers, environment_config


@task(
    help={
        "slug": "Slug of the environment you want to update",
        "environment": "Target UltraViolet environment",
    },
    optional=["environment"],
)
def enable_subcommunities(_ctx, slug, environment="local"):
    """
    Enables subcommunities on the given top-level community
    """
    with environment_config(environment) as config:
        get_response = requests.get(
            "{0}/api/communities/{1}".format(config["BASE_URL"], slug),
            headers=json_headers(config["ACCESS_TOKEN"]),
            verify=False,
        )

        response_json = get_response.json()

        new_subcommunities_url = "You can create new communities at {0}/communities/{1}/subcommunities/new".format(
            config["BASE_URL"], slug
        )

        if response_json["children"]["allow"]:
            print("Subcommunities already enabled for {0}.".format(slug))
            print(new_subcommunities_url)

        else:
            update_data = {
                "slug": slug,
                "metadata": response_json["metadata"],
                "access": response_json["access"],
                "children": {"allow": "yes"},
            }

            try:
                update_response = requests.put(
                    "{0}/api/communities/{1}".format(config["BASE_URL"], slug),
                    headers=json_headers(config["ACCESS_TOKEN"]),
                    verify=False,
                    data=json.dumps(update_data),
                )
                update_response.raise_for_status()
                print(new_subcommunities_url)

            except HTTPError as e:
                print(e.response.text)

            print("Update Response Code: {0}".format(get_response.status_code))
