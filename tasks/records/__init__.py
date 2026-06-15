"""Records management tasks."""
from .create_draft import create_draft
from .upload_file import upload_file
from .upload_files import upload_files
from .create_draft_and_upload_files import create_draft_and_upload_files
from .publish import publish
from .test import test

__all__ = [
	"create_draft",
	"create_draft_and_upload_files",
	"upload_file",
	"upload_files",
	"publish",
	"test",
]
