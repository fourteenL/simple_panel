import psutil
import time
from ....packages import convert_speed_units


# 获取所有网络接口的详细信息
async def get_network_info():
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


# 获取接口的网络速率
async def get_network_speed(interface, interval=1):
    last_counters = psutil.net_io_counters(pernic=True)[interface]

    while True:
        time.sleep(interval)
        current_counters = psutil.net_io_counters(pernic=True)[interface]

        bytes_sent = current_counters.bytes_sent - last_counters.bytes_sent
        bytes_recv = current_counters.bytes_recv - last_counters.bytes_recv

        upload = bytes_sent / interval
        download = bytes_recv / interval

        last_counters = current_counters

        return {
            "Interface": interface,
            "upload": upload,
            "download": download
        }
