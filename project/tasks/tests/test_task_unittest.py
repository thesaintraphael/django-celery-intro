from unittest.mock import patch

from tasks import sample_task


@patch("tasks.sample_task.create_task.run")
def test_mock_task(mock_run):
    assert sample_task.create_task.run(1)
    sample_task.create_task.run.assert_called_once_with(1)

    assert sample_task.create_task.run(2)
    assert sample_task.create_task.run.call_count == 2

    assert sample_task.create_task.run(3)
    assert sample_task.create_task.run.call_count == 3
