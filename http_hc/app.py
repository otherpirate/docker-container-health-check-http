from flask import Flask
from http_hc.docker_container import DockerContainer, ContainerNotFound


app = Flask(__name__)


@app.route("/health-check/")
def health_check():
    return "WORKING", 200


def container_should_exist(func):
   def wrapper(container):
        try:
            container = DockerContainer(container)
        except ContainerNotFound as not_found:
            return str(not_found), 404
        return func(container)
   wrapper.__name__ = func.__name__
   return wrapper


@app.route("/<container>/health-check/")
@container_should_exist
def container_health_check(container):
    if not container.is_running:
        error = "Container is {}. More info /{}/info/".format(
            container.status, container
        )
        return error, 500
    return "WORKING", 200


@app.route("/<container>/info/")
@container_should_exist
def container_info(container):
    msg = "Status: {}<br><br>".format(container.status)
    if container.is_running:
        msg += "======= Top =======<br>{}<br><br>".format(container.top)
    msg += "======= Logs =======<br>{}".format(container.logs)
    return msg, 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')
