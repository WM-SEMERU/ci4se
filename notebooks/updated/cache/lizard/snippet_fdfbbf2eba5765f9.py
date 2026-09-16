def get_volume():
    if system.get_name() == 'windows':
        pass
    elif system.get_name() == 'mac':
        volume = system.get_cmd_out(['osascript', '-e',
            'set ovol to output volume of (get volume settings); return the quoted form of ovol'
            ])
        return int(volume) * 10
    else:
        volume = system.get_cmd_out(
            "amixer get Master |grep % |awk '{print $5}'|sed -e 's/\\[//' -e 's/\\]//' | head -n1"
            )
        return int(volume.replace('%', ''))