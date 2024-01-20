import psutil


def get():
    server_info = {
        "hostname": psutil.users()[0].name,
        "os": f"{psutil.Process().username()}@{psutil.os.uname().sysname}",
        "cpu_percent": psutil.cpu_percent(),
        "memory_percent": psutil.virtual_memory().percent
    }
    return server_info
