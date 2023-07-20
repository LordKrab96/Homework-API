import data as data
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": file_path.split('/')[-1]}
        headers = {"Authorization": "OAuth " + token}
        response = requests.get(url, headers=headers, params=params)
        print(response.status_code)
        if 200 <= response.status_code < 300:
            data = response.json()
            url = data["href"]
            with open(file_path, "rb") as f:
                requests.post(url, files={"file": f})
                print(response.status_code)
        # Тут ваша логика
        # Функция может ничего не возвращать


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input("Введите путь до файла:")
    token = open("Token").read()
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
