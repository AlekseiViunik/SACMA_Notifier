import json
import os
import sys

from typing import Any

import consts as c


class JsonHandler:

    def __init__(self, file_path: str) -> None:
        self.file_path: str = c.EMPTY_STRING

        self.set_file_path(file_path)

    def get_all_data(self) -> dict[str, Any]:
        """
        Открывает JSON файл только для чтения, получает все данные и возвращает
        их в виде словаря. Расшифровывает, если требуется.

        Returns
        -------
        - _: dict
            Возвращаемые данные.
        """

        if self.file_path:
            try:
                with open(
                    self.file_path,
                    c.FILE_READ,
                    encoding=c.STR_CODING
                ) as f:
                    data = json.load(f)

                return data

            except FileNotFoundError:
                raise FileNotFoundError(
                    c.FNF_MESSAGE
                )
        return {}

    def get_value_by_key(self, key: str) -> Any:
        """
        Открывает JSON файл только для чтения, получает данные по ключу и
        возвращает их в том виде, в котором они там хранятся.

        Parameters
        ----------
        - key: str
            Ключ, по которому надо получить данные.

        Returns
        -------
        - _: Any
            Возвращаемые данные.
        """

        data = self.get_all_data()
        if data:
            return data.get(key, c.EMPTY_STRING)
        return c.EMPTY_STRING

    def get_values_by_keys(self, keys: list[str]) -> dict[str, str]:
        """
        Открывает JSON файл только для чтения, получает данные по списку
        ключей и возвращает их в виде словаря, где ключами будут те самые
        переданные в списке ключи.

        Parameters
        ----------
        - keys : list
            список ключей, для которых нужно найти значения в файле.

        Returns
        -------
        - result : dict
            Словарь со значениями для этих ключей. Или пустой словарь.
        """

        result = {}
        data = self.get_all_data()

        if data:
            for key in keys:
                if key in data.keys():
                    result[key] = data.get(key, c.EMPTY_STRING)

        return result

    def rewrite_file(self, data: dict[str, Any]) -> None:
        """
        Открывает файл JSON для записи и полностью перезаписывает его, заменяя
        имеющиеся там данные переданными в метод. Обычно используется для
        одноуровневого словаря. Шифрует, если требуется.

        Parameters
        ----------
        - data: dict
            Данные, которыми будет перезаписан файл.
        """

        data_to_upload: dict[str, str] | list[str] = data
        with open(
            self.file_path,
            c.FILE_WRITE,
            encoding=c.STR_CODING
        ) as f:
            if isinstance(data, dict):
                data_to_upload = {key: field for key, field in data.items()}
            json.dump(
                data_to_upload, f, indent=c.INDENT, ensure_ascii=False
            )

    def set_file_path(self, path: str) -> None:
        """
        Устанавливает абсолютный путь к файлу, если приложение работает как ехе
        файл.

        Parameters
        ----------
         - path: str
            относительный путь к файлу.
        """

        if getattr(sys, c.EXE_FROZEN, False):
            BASE_DIR = os.path.dirname(sys.executable)
            self.file_path = os.path.join(BASE_DIR, path)
        else:
            self.file_path = path
