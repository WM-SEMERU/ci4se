def get_service(name):
    with win32.OpenSCManager(dwDesiredAccess=win32.SC_MANAGER_ENUMERATE_SERVICE
        ) as hSCManager:
        with win32.OpenService(hSCManager, name, dwDesiredAccess=win32.
            SERVICE_QUERY_STATUS) as hService:
            try:
                return win32.QueryServiceStatusEx(hService)
            except AttributeError:
                return win32.QueryServiceStatus(hService)