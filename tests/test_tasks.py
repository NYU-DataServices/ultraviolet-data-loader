"""Test that tasks are properly imported and registered with invoke."""
import pytest
from invoke import Collection, Task

from tasks import records, communities, core
from tasks.communities import list_all as comm_list_all
from tasks.communities import show as comm_show
from tasks.communities import enable_subcommunities
from tasks.records import create_draft
from tasks.records import upload_file
from tasks.records import upload_files
from tasks.records import publish
from tasks.records import test as records_test


class TestCommunitiesModule:
    """Test communities tasks module."""

    def test_list_all_task_exists(self):
        """Verify list_all task is available."""
        assert callable(comm_list_all)
        assert isinstance(comm_list_all, Task)

    def test_show_task_exists(self):
        """Verify show task is available."""
        assert callable(comm_show)
        assert isinstance(comm_show, Task)

    def test_enable_subcommunities_task_exists(self):
        """Verify enable_subcommunities task is available."""
        assert callable(enable_subcommunities)
        assert isinstance(enable_subcommunities, Task)

    def test_communities_collection_has_tasks(self):
        """Verify communities collection includes all tasks."""
        assert hasattr(communities, "list_all")
        assert hasattr(communities, "show")
        assert hasattr(communities, "enable_subcommunities")


class TestRecordsModule:
    """Test records tasks module."""

    def test_create_draft_task_exists(self):
        """Verify create_draft task is available."""
        assert callable(create_draft)
        assert isinstance(create_draft, Task)

    def test_upload_file_task_exists(self):
        """Verify upload_file task is available."""
        assert callable(upload_file)
        assert isinstance(upload_file, Task)

    def test_upload_files_task_exists(self):
        """Verify upload_files task is available."""
        assert callable(upload_files)
        assert isinstance(upload_files, Task)

    def test_publish_task_exists(self):
        """Verify publish task is available."""
        assert callable(publish)
        assert isinstance(publish, Task)

    def test_test_task_exists(self):
        """Verify test task is available."""
        assert callable(records_test)
        assert isinstance(records_test, Task)

    def test_records_collection_has_tasks(self):
        """Verify records collection includes all tasks."""
        assert hasattr(records, "create_draft")
        assert hasattr(records, "upload_file")
        assert hasattr(records, "upload_files")
        assert hasattr(records, "publish")
        assert hasattr(records, "test")
