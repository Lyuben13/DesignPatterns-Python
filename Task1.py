# Builder Pattern Example: Building a Computer
class Computer:
    def __init__(self, cpu=None, ram=None, storage=None, gpu=None):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.gpu = gpu

    def __str__(self):
        return f"Computer with CPU: {self.cpu}, RAM: {self.ram}GB, Storage: {self.storage}GB, GPU: {self.gpu}"

# Builder Class
class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def build(self):
        return self.computer

# Director Class
class Director:
    def __init__(self, builder):
        self.builder = builder

    def build_gaming_computer(self):
        return self.builder.set_cpu("Intel i9").set_ram(32).set_storage(1000).set_gpu("NVIDIA RTX 3080").build()

    def build_office_computer(self):
        return self.builder.set_cpu("Intel i5").set_ram(16).set_storage(500).set_gpu("Integrated").build()

# Testing the Builder Pattern
builder = ComputerBuilder()
director = Director(builder)

gaming_computer = director.build_gaming_computer()
print(gaming_computer)

office_computer = director.build_office_computer()
print(office_computer)
