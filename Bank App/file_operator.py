import pandas as pd

data = {
    "username": ["Dubi"],
    "password": ["Daba"],
    "balance": [0.0]
}


class FileOperator:

    def __init__(self):
        pass

    def check_credentials(self, username: str, password: str) -> bool:
        try:
            existing_csv = pd.read_csv("data.csv")
        except FileNotFoundError:
            print("There is no file to update")
            return False
        else:
            if (existing_csv["username"].isin([f"{username}"])).any():
                user_index = existing_csv.index.get_loc(existing_csv[existing_csv["username"] == f"{username}"].index[0])
                if existing_csv.loc[user_index, "password"] == password:
                    return True
            else:
                print("Invalid credentials")
        finally:
            pass

    def add_balance(self, username: str, amount: float) -> None:
        try:
            existing_csv = pd.read_csv("data.csv")
        except FileNotFoundError:
            print("There is no file to update")
        else:
            existing_csv.loc[existing_csv["username"] == f"{username}", "balance"] = existing_csv["balance"] + amount
            existing_csv.to_csv("data.csv", index=False)
        finally:
            pass

    def minus_balance(self, username: str, amount: float) -> None:
        try:
            existing_csv = pd.read_csv("data.csv")
        except FileNotFoundError:
            print("There is no file to update")
        else:
            existing_csv.loc[existing_csv["username"] == f"{username}", "balance"] = existing_csv["balance"] - amount
            existing_csv.to_csv("data.csv", index=False)
        finally:
            pass

    def update_password(self, username: str, new_password: str) -> None:
        try:
            existing_csv = pd.read_csv("data.csv")

        except FileNotFoundError:
            print("There is no file to update")
        else:
            existing_csv.loc[existing_csv["username"] == f"{username}", "password"]\
                = f"{new_password}"
            existing_csv.to_csv("data.csv", index=False)
        finally:
            pass

    def register_or_create_user(self, new_user_data: dict) -> None:
        try:
            existing_csv = pd.read_csv("data.csv")
        except FileNotFoundError:
            new_csv = pd.DataFrame(new_user_data)
            new_csv.to_csv("data.csv")
        else:
            new_data = pd.DataFrame(new_user_data)
            existing_csv = pd.concat([existing_csv, new_data], ignore_index=True)
            existing_csv.to_csv("data.csv", index=False)
        finally:
            pass

 file_op = FileOperator()
# file_op.register_or_create_user(data)
# file_op.add_balance("Dubi", 190.9)
# file_op.minus_balance("Dubi", 190.9)
# file_op.update_password("Dubi", "XDDD")
# if file_op.check_credentials("Dubi", "XDDD"):
#     print("dobrze się stało")
# else:
#     print("też dobrze bo nie przeszło")