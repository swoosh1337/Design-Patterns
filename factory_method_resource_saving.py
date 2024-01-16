from abc import ABC, abstractmethod

# Product Interface
class Resource(ABC):
    @abstractmethod
    def use(self):
        pass

# Concrete Products
class DatabaseConnection(Resource):
    def use(self):
        print("Using database connection")

class NetworkResource(Resource):
    def use(self):
        print("Using network resource")

# Creator Class
class ResourceManager(ABC):
    _resources = {}

    @abstractmethod
    def createResource(self, type):
        pass

    def getResource(self, type):
        if type not in self._resources:
            self._resources[type] = self.createResource(type)
        return self._resources[type]

# Concrete Creator
class MyResourceManager(ResourceManager):
    def createResource(self, type):
        if type == "database":
            return DatabaseConnection()
        elif type == "network":
            return NetworkResource()
        else:
            raise ValueError("Unknown resource type")

# Client Code
manager = MyResourceManager()
db = manager.getResource("database")
db.use()  # Using database connection
network = manager.getResource("network")
network.use()  # Using network resource

