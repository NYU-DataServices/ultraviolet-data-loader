"""Create a draft and upload files to it using existing tasks."""
from invoke import task

from .create_draft import create_draft
from .upload_files import upload_files


@task(
    help={
        "glob-pattern": "Glob pattern of files to upload (*.jpg, code/*.py, etc.)",
        "environment": "Target UltraViolet environment",
        "file-path": "Optional path to JSON file containing the record data. If not provided, a minimal record will be created.",
    },
    optional=["environment", "file_path"],
)
def create_draft_and_upload_files(_ctx, glob_pattern, environment="local", file_path=None):
    """
    Create a draft record and upload multiple files to it using a glob pattern.

    This task reuses `create_draft` and `upload_files` to avoid duplicating logic.
    """
    # Create the draft and get the draft ID
    draft_id = create_draft(_ctx, environment=environment, file_path=file_path)

    if not draft_id:
        raise RuntimeError("Failed to create draft")

    # Upload files to the created draft
    upload_files(_ctx, draft_id, glob_pattern, environment=environment)
