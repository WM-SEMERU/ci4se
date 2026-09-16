def resume_service(name):
    with win32.OpenSCManager(dwDesiredAccess=win32.SC_MANAGER_CONNECT
        ) as hSCManager:
        with win32.OpenService(hSCManager, name, dwDesiredAccess=win32.
            SERVICE_PAUSE_CONTINUE) as hService:
            win32.ControlService(hService, win32.SERVICE_CONTROL_CONTINUE)