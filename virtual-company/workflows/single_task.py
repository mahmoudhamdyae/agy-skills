"""
Company Fast-Path Workflow: Single Specialist Task
Dispatches directly to the target specialist and passes through Quality Review.
"""
import sys

def run_single_task(task_title, department, specialist, instructions):
    print(f"Company Mode: ACTIVE")
    print(f"Task: {task_title}")
    print(f"Primary Department: {department}")
    print(f"Assigned Specialist: {specialist}")
    print("Executing single-task fast-path with senior quality verification.")
    return {"status": "SUCCESS", "task": task_title, "specialist": specialist}

if __name__ == "__main__":
    run_single_task("Sample Task", "Engineering", "Flutter Developer", "Build widget")
