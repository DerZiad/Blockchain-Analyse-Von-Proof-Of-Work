import GPUtil,psutil


class CPUStat:
    def __init__(self,physical_core,total_core,frequency,use,total_use):
        self.physical_core = physical_core
        self.total_core = total_core
        self.max_frequency = frequency.max
        self.min_frequency = frequency.min
        self.current_frequency = frequency.current
        self.use = use
        self.total_use = total_use

    def __str__(self):
        chain = ""
        chain += "Physical cores:" + str(self.physical_core) + "\n"
        chain += "Total cores:" + str(self.total_core) + "\n"
        chain += f"Max Frequency: {self.max_frequency:.2f}Mhz" + "\n"
        chain += f"Min Frequency: {self.min_frequency:.2f}Mhz" + "\n"
        chain += f"Current Frequency: {self.current_frequency:.2f}Mhz" + "\n"
        chain += "CPU Usage Per Core:" + "\n"
        for i in range(len(self.use)):
            chain += f"Core {i}: {self.use[i]}%" + "\n"
        chain += f"Total CPU Usage: {self.total_use}%\n"
        return chain

class GPUStat:
    def __init__(self,id,name,load,memoryFree,memoryUsed,memoryTotal,temperature,uuid):
        self.gpu_id = id
        self.gpu_name = name
        self.gpu_load = f"{load * 100}%"
        self.gpu_free_memory = f"{memoryFree}MB"
        self.gpu_used_memory = f"{memoryUsed}MB"
        self.gpu_total_memory = f"{memoryTotal}MB"
        self.gpu_temperature = f"{temperature} °C"
        self.gpu_uuid = uuid
    def __str__(self):
        chain = ""
        chain += "Gpu id:" + str(self.gpu_id) + "\n"
        chain += "Total cores:" + str(self.gpu_name) + "\n"
        chain += f"Max Frequency: {self.gpu_load:.2f}Mhz" + "\n"
        chain += f"Min Frequency: {self.gpu_free_memory:.2f}Mhz" + "\n"
        chain += f"Current Frequency: {self.gpu_used_memory:.2f}Mhz" + "\n"
        chain += f"Current Frequency: {self.gpu_used_memory:.2f}Mhz" + "\n"
        chain += f"Current Frequency: {self.gpu_used_memory:.2f}Mhz" + "\n"
        chain += f"Current Frequency: {self.gpu_used_memory:.2f}Mhz" + "\n"

        chain += "CPU Usage Per Core:" + "\n"
        for i in range(len(self.use)):
            chain += f"Core {i}: {self.use[i]}%" + "\n"
        chain += f"Total CPU Usage: {self.total_use}%\n"
        return chain

def scanGPU():
    gpus = GPUtil.getGPUs()
    list_gpus: GPUStat = []
    for gpu in gpus:
        gpu_id = gpu.id
        gpu_name = gpu.name
        gpu_load = f"{gpu.load * 100}%"
        gpu_free_memory = f"{gpu.memoryFree}MB"
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        gpu_temperature = f"{gpu.temperature} °C"
        gpu_uuid = gpu.uuid
        list_gpus.append(
            GPUStat(gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory, gpu_total_memory, gpu_temperature,
                    gpu_uuid))
        return gpu_uuid

def scanCPU():
    physical_core = psutil.cpu_count(logical=False)
    total_core = psutil.cpu_count(logical=True)
    temporal = psutil.cpu_freq()
    uses = []
    for percentage in psutil.cpu_percent(percpu=True, interval=1):
        uses.append(percentage)
    total_use = psutil.cpu_percent()
    cpuStat = CPUStat(physical_core, total_core, temporal, uses, total_use)
    return cpuStat