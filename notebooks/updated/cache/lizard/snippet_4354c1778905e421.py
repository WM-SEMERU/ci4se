def get_active_services():
    with win32.OpenSCManager(dwDesiredAccess=win32.SC_MANAGER_ENUMERATE_SERVICE
        ) as hSCManager:
        return [entry for entry in win32.EnumServicesStatusEx(hSCManager,
            dwServiceType=win32.SERVICE_WIN32, dwServiceState=win32.
            SERVICE_ACTIVE) if entry.ProcessId]