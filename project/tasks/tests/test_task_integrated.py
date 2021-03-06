import json
from django.urls import reverse


def test_task_status(client):

    response = client.post(reverse("run_task"), {"type": 0})
    content = json.loads(response.content)
    task_id = content["task_id"]
    assert response.status_code == 202
    assert task_id

    response = client.get(reverse("get_status", kwargs={"task_id": task_id}))
    content = json.loads(response.content)
    assert response.status_code == 200
    assert content == {
        "task_id": task_id,
        "task_status": "PENDING",
        "task_result": None,
    }


    while content["task_status"] == "PENDING":
        response = client.get(reverse("get_status", kwargs={"task_id": task_id}))
        content = json.loads(response.content)

    assert content == {
        "task_id": task_id,
        "task_status": "SUCCESS",
        "task_result": True,
    }
