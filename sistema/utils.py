import platform
import psutil

def datos_sistema():
    # CPU
    try:
        cpu = psutil.cpu_percent(interval=1)
    except Exception:
        cpu = None

    # RAM
    try:
        mem = psutil.virtual_memory()
        ram_total = mem.total / (1024**3)  
        ram_usada = mem.used  / (1024**3)
        ram_pct   = mem.percent
    except Exception:
        ram_total = ram_usada = ram_pct = None

    # Disco
    try:
        disco = psutil.disk_usage('/')
        disco_total = disco.total / (1024**3)
        disco_usado = disco.used  / (1024**3)
        disco_libre = disco.free  / (1024**3)
        disco_pct   = disco.percent
    except Exception:
        disco_total = disco_usado = disco_libre = disco_pct = None

    return {
        'cpu': cpu,
        'ram_total': ram_total, 'ram_usada': ram_usada, 'ram_pct': ram_pct,
        'disco_total': disco_total, 'disco_usado': disco_usado,
        'disco_libre': disco_libre, 'disco_pct': disco_pct,
        'so': platform.system(),
        'so_release': platform.release(),
        'nucleos_logicos':  psutil.cpu_count(logical=True),
        'nucleos_fisicos':  psutil.cpu_count(logical=False),
    }
