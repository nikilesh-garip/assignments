import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from tasks.task09.unassisted import TaskManager as TM_unassisted
from tasks.task09.assisted import TaskManager as TM_assisted

@pytest.mark.parametrize("TMClass", [TM_unassisted, TM_assisted])
def test_task_manager_isolation(TMClass):
    mgr = TMClass()
    t1 = mgr.add_task("Task 1")
    t2 = mgr.add_task("Task 2", tags=["urgent"])
    t3 = mgr.add_task("Task 3")
    
    # Ensure t1 and t3 don't inherit tags from mutable default
    assert t1["tags"] == []
    assert t2["tags"] == ["urgent"]
    assert t3["tags"] == []
    assert len(mgr.tasks) == 3
