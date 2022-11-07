import logging
from typing import Callable, Dict, Type

from portal.domain import commands

from . import uow

logger = logging.getLogger(__name__)


class CommandBus:
    def __init__(
        self,
        uow: uow.AbstractUnitOfWork,
        command_handlers: Dict[Type[commands.Command], Callable],
    ):
        self.uow = uow
        self.command_handlers = command_handlers

    def handle(self, command):
        if isinstance(command, commands.Command):
            return self.handle_command(command)
        else:
            raise Exception("Passed object has invalid type, command expected")

    def handle_command(self, command: commands.Command):
        logger.debug("handling command %s", command)
        handler = self.command_handlers[type(command)]
        return handler(command)
