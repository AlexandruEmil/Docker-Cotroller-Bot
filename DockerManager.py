import docker

class DockerManager:
    def __init__(self, host="npipe:////./pipe/docker_engine"):
        self.client = docker.DockerClient(base_url=host)

    def list_containers(self):
        containers = self.client.containers.list(all=True)
        return [f"{c.name} - {c.status}" for c in containers]

    def start_container(self, name):
        try:
            container = self.client.containers.get(name)
            container.start()
            return f"Containerul '{name}' a fost pornit."
        except Exception as e:
            return f"Eroare: {str(e)}"

    def stop_container(self, name):
        try:
            container = self.client.containers.get(name)
            container.stop()
            return f"Containerul '{name}' a fost oprit."
        except Exception as e:
            return f"Eroare: {str(e)}"

    def restart_container(self, name):
        try:
            container = self.client.containers.get(name)
            container.restart()
            return f"Containerul '{name}' a fost restartat."
        except Exception as e:
            return f"Eroare: {str(e)}"
