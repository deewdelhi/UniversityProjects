from dataclasses import dataclass


@dataclass
class RedoOperation:
    target_object: object
    handler: object
    arguments: tuple


class RedoManager:
    __redo_operations = []

    @staticmethod
    def register_operation(target_object, handler, *arguments):
        RedoManager.__redo_operations.append(RedoOperation(target_object, handler, arguments))

    @staticmethod
    def redo():
        redo_operation = RedoManager.__redo_operations.pop()
        redo_operation.handler(redo_operation.target_object, *redo_operation.arguments)

    @staticmethod
    def get_first_argument():
        return RedoManager.__redo_operations[len(RedoManager.__redo_operations) - 1].arguments[0]

    @staticmethod
    def get_second_argument():
        return RedoManager.__redo_operations[len(RedoManager.__redo_operations) - 1].arguments[1]

    @staticmethod
    def get_third_argument():
        return RedoManager.__redo_operations[len(RedoManager.__redo_operations) - 1].arguments[2]

    @staticmethod
    def get_fourth_argument():
        return RedoManager.__redo_operations[len(RedoManager.__redo_operations) - 1].arguments[3]

    @staticmethod
    def get_fifth_argument():
        return RedoManager.__redo_operations[len(RedoManager.__redo_operations) - 1].arguments[4]

    @staticmethod
    def get_sixth_argument():
        return RedoManager.__redo_operations[len(RedoManager.__redo_operations) - 1].arguments[5]

    @staticmethod
    def get_seventh_argument():
        return RedoManager.__redo_operations[len(RedoManager.__redo_operations) - 1].arguments[6]

    @staticmethod
    def get_eighth_argument():
        return RedoManager.__redo_operations[len(RedoManager.__redo_operations) - 1].arguments[7]

    @staticmethod
    def get_nineth_argument():
        return RedoManager.__redo_operations[len(RedoManager.__redo_operations) - 1].arguments[8]

    @staticmethod
    def get_handler():
        return RedoManager.__redo_operations[len(RedoManager.__redo_operations) - 1].handler
