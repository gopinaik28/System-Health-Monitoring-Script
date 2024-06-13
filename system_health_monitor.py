import psutil
import datetime

# thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 90
PROCESS_THRESHOLD = 500
def log_alert(metric, value):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("system_health.log", "a") as logfile:
        logfile.write(f"{current_time} - High {metric} usage detected: {value}%\n")

# CPU usage
cpu_percent = psutil.cpu_percent(interval=1)
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"{current_time} - CPU usage: {cpu_percent}%")
if cpu_percent > CPU_THRESHOLD:
    log_alert("CPU", cpu_percent)
# memory usage
memory_percent = psutil.virtual_memory().percent
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"{current_time} - Memory usage: {memory_percent}%")
if memory_percent > MEMORY_THRESHOLD:
    log_alert("memory", memory_percent)
# disk usage
disk_percent = psutil.disk_usage('/').percent
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"{current_time} - Disk usage: {disk_percent}%")
if disk_percent > DISK_THRESHOLD:
    log_alert("disk", disk_percent)
# number of running processes
process_count = len(psutil.pids())
current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"{current_time} - Number of running processes: {process_count}")
if process_count > PROCESS_THRESHOLD:
    log_alert("process", process_count)