from dataclasses import dataclass


@dataclass
class UndoOperation:
    target_object: object
    handler: object
    arguments: tuple



class UndoManager:
    __undo_operations = []

    @staticmethod
    def register_operation(target_object, handler, *arguments):
        UndoManager.__undo_operations.append(UndoOperation(target_object, handler, arguments))

    @staticmethod
    def undo():
        undo_operation = UndoManager.__undo_operations.pop()
        undo_operation.handler(undo_operation.target_object, *undo_operation.arguments)

    @staticmethod
    def get_first_argument():
        return UndoManager.__undo_operations[len(UndoManager.__undo_operations)-1].arguments[0]

    @staticmethod
    def get_second_argument():
        return UndoManager.__undo_operations[len(UndoManager.__undo_operations)-1].arguments[1]

    @staticmethod
    def get_third_argument():
        return UndoManager.__undo_operations[len(UndoManager.__undo_operations)-1].arguments[2]

    @staticmethod
    def get_fourth_argument():
        return UndoManager.__undo_operations[len(UndoManager.__undo_operations)-1].arguments[3]

    @staticmethod
    def get_fifth_argument():
        return UndoManager.__undo_operations[len(UndoManager.__undo_operations)-1].arguments[4]

    @staticmethod
    def get_sixth_argument():
        return UndoManager.__undo_operations[len(UndoManager.__undo_operations)-1].arguments[5]

    @staticmethod
    def get_seventh_argument():
        return UndoManager.__undo_operations[len(UndoManager.__undo_operations)-1].arguments[6]

    @staticmethod
    def get_eighth_argument():
        return UndoManager.__undo_operations[len(UndoManager.__undo_operations)-1].arguments[7]

    @staticmethod
    def get_nineth_argument():
        return UndoManager.__undo_operations[len(UndoManager.__undo_operations)-1].arguments[8]

    @staticmethod
    def get_tenth_argument():
        return UndoManager.__undo_operations[len(UndoManager.__undo_operations)-1].arguments[9]


    @staticmethod
    def get_handler():
        return UndoManager.__undo_operations[len(UndoManager.__undo_operations)-1].handler
