import pandas as pd

data = {
    "username": ["ciebie"],
    "password": ["xdxd"],
    "balance": [0.0]
}


class FileOperator:

    def __init__(self):
        pass

    def read_or_create_file(self, user_data: dict) -> None:
        try:
            existing_csv = pd.read_csv("data.csv")
        except FileNotFoundError:
            new_csv = pd.DataFrame(user_data)
            new_csv.to_csv("data.csv")
        finally:
            pass


    def update_balance(self, username: str, amount: float) -> None:
         try:
            existing_csv = pd.read_csv("data.csv")
            existing_csv.loc[existing_csv["username"] == f"{username}", "balance"] = existing_csv["balance"] + amount
            existing_csv.to_csv("data.csv", index=False)
         except FileNotFoundError:
             print("There is no file to update")
         finally:
             pass

    def update_password(self, username:str, new_password: str):
        try:
            existing_csv = pd.read_csv("data.csv")
            existing_csv.loc[existing_csv["username"] == f"{username}", "password"]\
                = f"{new_password}"
            existing_csv.to_csv("data.csv", index=False)
        except FileNotFoundError:
            print("There is no file to update")
        finally:
            pass

    def register_user(self, new_user_data: dict):
        try:
            existing_csv = pd.read_csv("data.csv")
            new_data = pd.DataFrame(new_user_data)
            existing_csv = pd.concat([existing_csv, new_data], ignore_index=True)
            existing_csv.to_csv("data.csv", index=False)
        except FileNotFoundError:
            new_csv = pd.DataFrame(new_user_data)
            new_csv.to_csv("data.csv")
        finally:
            pass

file_op = FileOperator()
#file_op.register_user(data)
#file_op.update_balance("z", 190.9)
#file_op.update_password("Dolan", "xdxd")