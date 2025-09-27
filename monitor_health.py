import psutil
import time

def get_system_health():
    """Fetches key system health metrics."""
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    health_data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "cpu_usage_percent": cpu_percent,
        "memory_total_gb": round(memory_info.total / (1024**3), 2),
        "memory_used_percent": memory_info.percent,
        "disk_usage_percent": disk_info.percent,
    }
    return health_data

def log_health_data(data):
    """Prints or logs the health data."""
    print("--- System Health Report ---")
    for key, value in data.items():
        print(f"{key}: {value}")
    print("-" * 30)

if __name__ == "__main__":
    print("Starting Project Health Monitor...")
    try:
        # Check health every 10 seconds (for demonstration)
        while True:
            health_metrics = get_system_health()
            log_health_data(health_metrics)
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nHealth monitoring stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")
