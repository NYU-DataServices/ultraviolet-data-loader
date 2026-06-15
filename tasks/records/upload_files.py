"""Upload multiple files to a draft record using glob patterns."""
import glob

from invoke import task

from tasks.helpers import environment_config
from ._helpers import initialize_and_commit_file


@task(
    help={
        "draft-id": "The ID of the draft record to upload the file to",
        "glob-pattern": "Glob pattern of files to upload (*.jpg, code/*.py, etc.)",
        "environment": "Target UltraViolet environment",
    },
    optional=["environment"],
)
def upload_files(_ctx, draft_id, glob_pattern, environment="local"):
    """
    Upload multiple files to a record using glob patterns (*.jpg, code/*.py, etc.)
    """
    with environment_config(environment) as config:
        for file_path in glob.glob(glob_pattern):
            initialize_and_commit_file(config, draft_id, file_path)
