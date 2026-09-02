class File:
    def __init__(self, name: str) -> None:
        self.name = name
        self.in_trash = False
        self.is_deleted = False

    def restore_from_trash(self) -> None:
        print(f'Файл {self.name} восстановлен из корзины')
        self.in_trash = False

    def remove(self) -> None:
        print(f'Файл {self.name} был удален')
        self.is_deleted = True

    def __readwrite(self, action: str, text: str) -> None:
        if self.is_deleted:
            print(f'Error{action}FileDeleted({self.name})')
        elif self.in_trash:
            print(f'Error{action}FileTrashed({self.name})')
        else:
            print(text)

    def read(self) -> None:
        self.__readwrite('Read', f'Прочитали все содержимое файла {self.name}')

    def write(self, content) -> None:
        self.__readwrite('Write', f'Записали значение {content} в файл {self.name}')


class Trash:
    content = []

    @staticmethod
    def add(file_obj: File) -> None:
        if not isinstance(file_obj, File):
            print('В корзину можно добавлять только файл')
            return

        file_obj.in_trash = True
        Trash.content.append(file_obj)

    @staticmethod
    def clear() -> None:
        print('Очищаем корзину')

        for file_obj in Trash.content:
            file_obj.remove()

        Trash.content = []
        print(f'Корзина пуста')

    @staticmethod
    def restore() -> None:
        print('Восстанавливаем файлы из корзины')

        for file_obj in Trash.content:
            file_obj.restore_from_trash()

        Trash.content = []
        print('Корзина пуста')