from docker import DockerClient
from docker.errors import NotFound


class DockerContainer(object):

    def __init__(self, id_or_name):
        self.id_or_name = id_or_name
        self.client = DockerClient()
        self.load_container()

    def load_container(self):
        try:
            self.container = self.client.containers.get(self.id_or_name)
        except NotFound:
            raise ContainerNotFound(self)

    @property
    def status(self):
        return self.container.status

    @property
    def is_running(self):
        return self.container.status.lower() == "running"

    @property
    def top(self):
        return self.container.top()

    @property
    def logs(self):
        return self.container.logs()

    def __str__(self):
        return self.id_or_name


class DockerContainerError(Exception):
    pass


class ContainerNotFound(DockerContainerError):
    def __init__(self, id_or_name):
        error = "Container {} not found".format(id_or_name)
        super(ContainerNotFound, self).__init__(error)
