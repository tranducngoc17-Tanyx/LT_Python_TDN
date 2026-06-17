class BankAccount:
    # Class attributes
    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number, account_name):
        self.account_number = account_number
        self._account_name = ""
        self.account_name = account_name
        self.__balance = 0

    # @property chỉ cho phép đọc số dư
    @property
    def balance(self):
        return self.__balance

    # Getter tên tài khoản
    @property
    def account_name(self):
        return self._account_name

    # Setter tên tài khoản
    @account_name.setter
    def account_name(self, new_name):
        new_name = new_name.strip()

        if new_name == "":
            print("Tên tài khoản không được để trống")
            return

        self._account_name = new_name.upper()

    # Static method kiểm tra số tài khoản
    @staticmethod
    def validate_account_number(account_number):
        return account_number.isdigit() and len(account_number) == 10

    # Class method cập nhật phí giao dịch
    @classmethod
    def update_transaction_fee(cls, new_fee):
        cls.transaction_fee = new_fee

    # Nạp tiền
    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False

        self.__balance += amount
        return True

    # Rút tiền
    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
            return False

        total = amount + BankAccount.transaction_fee

        if self.__balance < total:
            print("Giao dịch thất bại. Số dư không đủ để thanh toán số tiền và phí giao dịch")
            return False

        self.__balance -= total
        return True

    # Hiển thị thông tin
    def display_info(self):
        print("\n--- THÔNG TIN TÀI KHOẢN ---")
        print(f"Ngân hàng: {BankAccount.bank_name}")
        print(f"Số tài khoản: {self.account_number}")
        print(f"Tên chủ tài khoản: {self.account_name}")
        print(f"Số dư hiện tại: {self.balance:,} VND")
        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")


current_account = None

while True:

    print("\n===== VIETCOMBANK DIGIBANK SIMULATOR =====")
    print("1. Mở tài khoản mới")
    print("2. Xem thông tin tài khoản")
    print("3. Giao dịch Nạp / Rút tiền")
    print("4. Cập nhật Tên chủ tài khoản")
    print("5. Đổi phí giao dịch hệ thống")
    print("6. Thoát chương trình")
    print("==========================================")

    choice = input("Chọn chức năng (1-6): ")

    match choice:

        # Mở tài khoản
        case "1":

            print("\n--- MỞ TÀI KHOẢN MỚI ---")

            while True:
                account_number = input("Nhập số tài khoản 10 chữ số: ")

                if BankAccount.validate_account_number(account_number):
                    break

                print("Số tài khoản không hợp lệ!")
                print("Số tài khoản phải gồm đúng 10 chữ số.")

            account_name = input("Nhập tên chủ tài khoản: ")

            current_account = BankAccount(account_number, account_name)

            print("\nMở tài khoản thành công!")
            print("Số tài khoản:", current_account.account_number)
            print("Tên chủ tài khoản:", current_account.account_name)

        # Xem thông tin
        case "2":

            if current_account is None:
                print("Hệ thống chưa có thông tin tài khoản")
                print("Vui lòng mở tài khoản ở Chức năng 1 trước.")
            else:
                current_account.display_info()

        # Giao dịch
        case "3":

            if current_account is None:
                print("Hệ thống chưa có thông tin tài khoản")
                continue

            print("\n--- GIAO DỊCH NẠP / RÚT TIỀN ---")
            print("1. Nạp tiền")
            print("2. Rút tiền")

            transaction = input("Chọn loại giao dịch (1-2): ")

            try:
                amount = int(input("Nhập số tiền giao dịch: "))
            except ValueError:
                print("Số tiền không hợp lệ")
                continue

            match transaction:

                case "1":
                    if current_account.deposit(amount):
                        print(f"Nạp tiền thành công: +{amount:,} VND")
                        print(f"Số dư mới: {current_account.balance:,} VND")

                case "2":
                    if current_account.withdraw(amount):
                        print(f"Rút tiền thành công: -{amount:,} VND")
                        print(f"Phí giao dịch: {BankAccount.transaction_fee:,} VND")
                        print(f"Số dư mới: {current_account.balance:,} VND")
                    else:
                        print(f"Số dư mới: {current_account.balance:,} VND")

                case _:
                    print("Lựa chọn không hợp lệ")