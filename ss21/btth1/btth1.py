import logging
import sys

class InvalidAmountError(Exception):
    """Exception raised for negative or zero amounts."""
    pass

class InsufficientBalanceError(Exception):
    """Exception raised when balance is less than transfer amount."""
    pass

class TransactionLogger:
    """Handles logging configuration and operations."""
    
    def __init__(self, log_file='momo_transactions.log'):
        self.logger = logging.getLogger('MoMoLogger')
        self.logger.setLevel(logging.DEBUG)
        
        # Prevent duplicate handlers if instantiated multiple times
        if not self.logger.handlers:
            formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(message)s'
            )
            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def log_info(self, message: str):
        """Logs an info level message."""
        self.logger.info(message)

    def log_warning(self, message: str):
        """Logs a warning level message."""
        self.logger.warning(message)

    def log_error(self, message: str):
        """Logs an error level message."""
        self.logger.error(message)


class Wallet:
    """Manages wallet balance and money transactions."""
    
    def __init__(self, logger: TransactionLogger):
        self.balance = 0
        self.logger = logger

    def deposit(self, amount: int):
        """Handles depositing money into the wallet."""
        if amount <= 0:
            self.logger.log_error(
                f"InvalidAmountError: Attempted to process {amount} VND."
            )
            raise InvalidAmountError("Số tiền giao dịch phải lớn hơn 0.")
        
        self.balance += amount
        self.logger.log_info(
            f"Deposit successful: +{amount} VND. "
            f"Current Balance: {self.balance}"
        )

    def transfer(self, phone: str, amount: int):
        """Handles transferring money to another user."""
        if amount <= 0:
            self.logger.log_error(
                f"InvalidAmountError: Attempted to process {amount} VND."
            )
            raise InvalidAmountError("Số tiền giao dịch phải lớn hơn 0.")
        
        if amount > self.balance:
            self.logger.log_error(
                f"InsufficientBalanceError: Attempted to transfer "
                f"{amount} VND with balance {self.balance} VND."
            )
            raise InsufficientBalanceError(
                "Giao dịch thất bại: Số dư của bạn không đủ."
            )

        if amount >= 10000000:
            self.logger.log_warning(
                f"High value transaction detected: {amount} VND to {phone}"
            )

        self.balance -= amount
        self.logger.log_info(
            f"Transfer successful: -{amount} VND to {phone}. "
            f"Current Balance: {self.balance}"
        )

    def get_balance(self) -> int:
        """Returns the current wallet balance."""
        self.logger.log_info(
            f"Balance checked. Current Balance: {self.balance}"
        )
        return self.balance


def display_menu():
    """Displays the main CLI menu layout."""
    print("\n========== VÍ MOMO GIẢ LẬP ==========")
    print("1. Nạp tiền vào ví")
    print("2. Chuyển tiền")
    print("3. Xem số dư hiện tại")
    print("4. Thoát chương trình")
    print("=======================================")


def handle_deposit(wallet: Wallet, logger: TransactionLogger):
    """Processes user input and logic for depositing money."""
    print("\n--- NẠP TIỀN VÀO VÍ ---")
    try:
        amount = int(input("Nhập số tiền cần nạp: "))
        wallet.deposit(amount)
        print(f"Nạp tiền thành công: +{amount:,} VND")
        print(f"Số dư hiện tại: {wallet.balance:,} VND")
    except ValueError:
        logger.log_error("ValueError: Invalid numeric input for deposit.")
        print("Lỗi: Vui lòng nhập số tiền hợp lệ.")
    except InvalidAmountError as e:
        print(f"Lỗi: {e}")


def handle_transfer(wallet: Wallet, logger: TransactionLogger):
    """Processes user input and logic for transferring money."""
    print("\n--- CHUYỂN TIỀN ---")
    phone = input("Nhập số điện thoại người nhận: ")
    
    if len(phone) != 10 or not phone.isdigit():
        print("Lỗi: Số điện thoại không hợp lệ (cần đúng 10 chữ số).")
        return

    try:
        amount = int(input("Nhập số tiền cần chuyển: "))
        wallet.transfer(phone, amount)
        print(f"Chuyển tiền thành công tới số điện thoại {phone}.")
        print(f"Số tiền đã chuyển: {amount:,} VND")
        print(f"Số dư còn lại: {wallet.balance:,} VND")
    except ValueError:
        logger.log_error("ValueError: Invalid numeric input for transfer.")
        print("Lỗi: Vui lòng nhập số tiền hợp lệ.")
    except InsufficientBalanceError as e:
        print(e)
    except InvalidAmountError as e:
        print(f"Lỗi: {e}")


def main():
    """Main execution loop for the MoMo Wallet simulator."""
    logger = TransactionLogger()
    wallet = Wallet(logger)

    while True:
        display_menu()
        choice = input("Chọn chức năng (1-4): ")

        if choice == '1':
            handle_deposit(wallet, logger)
        elif choice == '2':
            handle_transfer(wallet, logger)
        elif choice == '3':
            print("\n--- SỐ DƯ VÍ MOMO ---")
            balance = wallet.get_balance()
            print(f"Số dư hiện tại: {balance:,} VND")
        elif choice == '4':
            print("Cảm ơn bạn đã sử dụng dịch vụ.")
            logger.log_info("System shutdown")
            sys.exit(0)
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại (1-4).")

if __name__ == "__main__":
    main()

import unittest
from momo_wallet import (
    Wallet, 
    TransactionLogger, 
    InvalidAmountError, 
    InsufficientBalanceError
)

class TestWallet(unittest.TestCase):
    """Unit test cases for the Wallet class."""

    def setUp(self):
        """Sets up a clean Wallet and Logger instance before each test."""
        # Using a separate log file for testing to avoid cluttering main logs
        self.logger = TransactionLogger(log_file='test_transactions.log')
        self.wallet = Wallet(self.logger)

    def test_deposit_success(self):
        """Tests if a valid deposit increases the balance correctly."""
        self.wallet.deposit(500000)
        self.assertEqual(self.wallet.balance, 500000)

        self.wallet.deposit(250000)
        self.assertEqual(self.wallet.balance, 750000)

    def test_transfer_insufficient_balance(self):
        """Tests if InsufficientBalanceError is properly raised."""
        self.wallet.deposit(300000)
        
        with self.assertRaises(InsufficientBalanceError):
            self.wallet.transfer("0987654321", 500000)
        
        # Ensure the balance remains entirely unchanged after failure
        self.assertEqual(self.wallet.balance, 300000)

    def test_invalid_amount(self):
        """Tests if InvalidAmountError is raised on negative/zero amounts."""
        with self.assertRaises(InvalidAmountError):
            self.wallet.deposit(-100000)

        with self.assertRaises(InvalidAmountError):
            self.wallet.deposit(0)

        self.wallet.deposit(100000)
        
        with self.assertRaises(InvalidAmountError):
            self.wallet.transfer("0987654321", -50000)

if __name__ == "__main__":
    unittest.main()