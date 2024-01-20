# 字节速率转换
def convert_speed_units(speed_bytes_per_sec):
    if speed_bytes_per_sec < 1024:
        return speed_bytes_per_sec, "B/s"
    elif speed_bytes_per_sec < 1024 * 1024:
        return speed_bytes_per_sec / 1024, "KB/s"
    else:
        return speed_bytes_per_sec / (1024 * 1024), "MB/s"
