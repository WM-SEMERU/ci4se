def build_workspace_path(user_id, workflow_id=None):
    workspace_path = os.path.join('users', str(user_id), 'workflows')
    if workflow_id:
        workspace_path = os.path.join(workspace_path, str(workflow_id))
    return workspace_path