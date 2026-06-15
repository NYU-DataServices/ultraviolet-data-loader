"""Helper functions for records tasks."""
import requests

from tasks.helpers import json_headers, octet_stream_headers


def initialize_and_commit_file(config, draft_id, file_path):
    """Upload a file to a draft record, initializing and committing it.

    Args:
        config: Configuration dictionary with BASE_URL and ACCESS_TOKEN
        draft_id: The ID of the draft record
        file_path: Path to the file to upload
    """
    print("Uploading file {0}...".format(file_path))

    file_name = file_path.split("/")[-1]
    file_data = [{"key": file_name}]

    file_initialize_url = "{0}/api/records/{1}/draft/files".format(
        config["BASE_URL"], draft_id
    )
    file_content_url = "{0}/api/records/{1}/draft/files/{2}/content".format(
        config["BASE_URL"], draft_id, file_name
    )
    file_commit_url = "{0}/api/records/{1}/draft/files/{2}/commit".format(
        config["BASE_URL"], draft_id, file_name
    )

    print("Initializing file...")
    initialize_file_response = requests.post(
        file_initialize_url,
        headers=json_headers(config["ACCESS_TOKEN"]),
        json=file_data,
        verify=False,
    )

    print(
        "Initialize File Response Code: {0}".format(
            initialize_file_response.status_code
        )
    )
    print("File Content URL: {0}".format(file_content_url))

    print("Uploading file...")
    with open(file_path, "rb") as file:
        file_upload_response = requests.put(
            file_content_url,
            headers=octet_stream_headers(config["ACCESS_TOKEN"]),
            data=file,
            stream=True,
            verify=False,
        )

    print("File Upload Response Code: {0}".format(file_upload_response.status_code))

    print("Committing file...")
    commit_response = requests.post(
        file_commit_url,
        headers=json_headers(config["ACCESS_TOKEN"]),
        verify=False,
    )
    print("Commit File Response Code: {0}".format(commit_response.status_code))
    print("")
