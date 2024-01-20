import platform
import psutil
import time
from packages import convert_speed_units


# 获取所有网络接口的状态
def get_network_status():
    # 获取网络接口列表
    net_interfaces = psutil.net_if_stats()

    network_status = {}
    for interface, stats in net_interfaces.items():
        network_status[interface] = {
            "Is Up": stats.isup,
            "Speed": stats.speed,
            "MTU": stats.mtu,
            "flags": stats.flags
        }

    return network_status

# print(get_network_status())


# 获取接口的网络速率
def get_network_speed(interface, interval=1):
    last_counters = psutil.net_io_counters(pernic=True)[interface]

    while True:
        time.sleep(interval)
        current_counters = psutil.net_io_counters(pernic=True)[interface]

        bytes_sent = current_counters.bytes_sent - last_counters.bytes_sent
        bytes_recv = current_counters.bytes_recv - last_counters.bytes_recv

        bytes_sent_per_sec = bytes_sent / interval
        bytes_recv_per_sec = bytes_recv / interval

        last_counters = current_counters

        yield {
            "Interface": interface,
            "upload": bytes_sent_per_sec,
            "download": bytes_recv_per_sec
        }


target_interface = "eth0"
speed_generator = get_network_speed(target_interface)

try:
    while True:
        speed_info = next(speed_generator)
        upload_speed, upload_unit = convert_speed_units(speed_info["upload"])
        download_speed, download_unit = convert_speed_units(
            speed_info["download"])
        print("Interface:", speed_info["Interface"])
        print("upload:", upload_speed, upload_unit)
        print("download:", download_speed, download_unit)
        print()
except KeyboardInterrupt:
    print("Monitoring stopped by user")
