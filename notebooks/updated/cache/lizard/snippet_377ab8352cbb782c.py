def label_for_waypoint(self, wp_num):
    wp = self.module('wp').wploader.wp(wp_num)
    command = wp.command
    if command not in self._label_suffix_for_wp_command:
        return str(wp_num)
    return str(wp_num) + '(' + self._label_suffix_for_wp_command[command] + ')'