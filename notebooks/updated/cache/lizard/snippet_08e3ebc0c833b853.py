def _windows_wwns():
    ps_cmd = (
        'Get-WmiObject -ErrorAction Stop -class MSFC_FibrePortHBAAttributes -namespace "root\\WMI" | Select -Expandproperty Attributes | %{($_.PortWWN | % {"{0:x2}" -f $_}) -join ""}'
        )
    ret = []
    cmd_ret = salt.modules.cmdmod.powershell(ps_cmd)
    for line in cmd_ret:
        ret.append(line.rstrip())
    return ret