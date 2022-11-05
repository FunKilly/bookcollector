import inspect

from portal.adapters import mapping
from portal.services import command_bus, handlers, uow


def bootstrap(
    start_mapping: bool = True,
    uow: uow.AbstractUnitOfWork = uow.SqlAlchemyUnitOfWork(),
) -> command_bus.CommandBus:

    if start_mapping:
        mapping.start_mappers()

    dependencies = {"uow": uow}

    injected_command_handlers = {
        command_type: inject_dependencies(handler, dependencies)
        for command_type, handler in handlers.COMMAND_HANDLERS.items()
    }

    return command_bus.CommandBus(
        uow=uow,
        command_handlers=injected_command_handlers,
    )


def inject_dependencies(handler, dependencies):
    params = inspect.signature(handler).parameters
    deps = {
        name: dependency for name, dependency in dependencies.items() if name in params
    }
    return lambda message: handler(message, **deps)
