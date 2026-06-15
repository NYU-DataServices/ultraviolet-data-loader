"""Upload a single file to a draft record."""
from invoke import task

from tasks.helpers import environment_config
from ._helpers import initialize_and_commit_file


@task(
    help={
        "draft-id": "The ID of the draft record to upload the file to",
        "file-path": "Path to the file to upload",
        "environment": "Target UltraViolet environment",
    },
    optional=["environment"],
)
def upload_file(_ctx, draft_id, file_path, environment="local"):
    """
    Upload a single file to a record
    """
    with environment_config(environment) as config:
        initialize_and_commit_file(config, draft_id, file_path)
