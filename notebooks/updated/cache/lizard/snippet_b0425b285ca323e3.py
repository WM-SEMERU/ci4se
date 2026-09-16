def main():
    try:
        USBDevice.start_detection(on_attached=handle_attached, on_detached=
            handle_detached)
        while True:
            time.sleep(1)
    except Exception as ex:
        print('Exception:', ex)
    finally:
        for sn, device in __devices.items():
            device.close()
        USBDevice.stop_detection()