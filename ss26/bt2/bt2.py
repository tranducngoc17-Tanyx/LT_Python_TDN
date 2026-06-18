# # (1) PHÂN TÍCH LỖI (CODE REVIEW)

# ## Câu 1. Vòng lặp `for hero in team_heroes: hero.use_ultimate()` thể hiện tính chất Đa hình (Polymorphism) như thế nào?

# Đoạn code:

# ```python
# for hero in team_heroes:
#     hero.use_ultimate()
# ```

# thể hiện tính Đa hình (Polymorphism) vì biến `hero` có thể tham chiếu đến nhiều đối tượng thuộc các lớp khác nhau như `Mage` hoặc `Assassin`.

# Hệ thống không cần kiểm tra:

# ```python
# if isinstance(hero, Mage):
#     ...
# elif isinstance(hero, Assassin):
#     ...
# ```

# Mà chỉ cần gọi:

# ```python
# hero.use_ultimate()
# ```

# Python sẽ tự động xác định phương thức phù hợp dựa trên kiểu thực tế của đối tượng tại thời điểm chạy (Runtime).

# Ví dụ:

# * Nếu `hero` là đối tượng `Mage` → gọi `Mage.use_ultimate()`
# * Nếu `hero` là đối tượng `Assassin` → gọi `Assassin.use_ultimate()`

# Đây chính là bản chất của Polymorphism: cùng một lời gọi phương thức nhưng tạo ra những hành vi khác nhau tùy theo đối tượng.

# ---

# ## Câu 2. Với đoạn code cũ (không dùng thư viện abc), đối tượng Assassin vẫn được tạo ra thành công. Game chỉ văng lỗi NotImplementedError vào thời điểm nào? Tại sao việc báo lỗi muộn như vậy lại là thảm họa đối với trải nghiệm người chơi?

# Trong thiết kế cũ:

# ```python
# class Hero:
#     def use_ultimate(self):
#         raise NotImplementedError(...)
# ```

# Python vẫn cho phép tạo đối tượng:

# ```python
# Assassin()
# ```

# vì lớp `Hero` chỉ là một lớp thông thường, không phải Abstract Base Class.

# Do đó giai đoạn loading trận đấu:

# ```python
# team_heroes = [Mage(), Assassin()]
# ```

# vẫn diễn ra thành công.

# Lỗi chỉ xuất hiện khi giao tranh bắt đầu:

# ```python
# for hero in team_heroes:
#     hero.use_ultimate()
# ```

# Khi vòng lặp đến đối tượng `Assassin`, Python không tìm thấy phương thức `use_ultimate()` trong lớp `Assassin`, nên sẽ sử dụng phương thức kế thừa từ `Hero`.

# Lúc này dòng:

# ```python
# raise NotImplementedError(...)
# ```

# được thực thi và chương trình bị crash.

# Việc báo lỗi muộn như vậy là thảm họa đối với trải nghiệm người chơi vì:

# * Trận đấu đã được tải thành công.
# * Người chơi đã vào game bình thường.
# * Lỗi chỉ xuất hiện khi đang giao tranh.
# * Toàn bộ trận đấu có thể bị gián đoạn hoặc văng game giữa chừng.

# Đây là lỗi Runtime xảy ra trong quá trình vận hành thực tế thay vì được phát hiện sớm.

# ---

# ## Câu 3. Khi sử dụng module abc và decorator @abstractmethod cho lớp Hero, nếu lớp Assassin vẫn không ghi đè hàm use_ultimate(), lỗi sẽ văng ra vào thời điểm nào?

# Khi sử dụng:

# ```python
# from abc import ABC, abstractmethod
# ```

# và khai báo:

# ```python
# class Hero(ABC):
#     @abstractmethod
#     def use_ultimate(self):
#         pass
# ```

# thì Python sẽ kiểm tra tính đầy đủ của các phương thức trừu tượng ngay khi khởi tạo đối tượng.

# Nếu lớp `Assassin` không ghi đè:

# ```python
# def use_ultimate(self):
# ```

# thì lỗi sẽ xuất hiện ngay tại thời điểm:

# ```python
# Assassin()
# ```

# hoặc:

# ```python
# team_heroes = [Mage(), Assassin()]
# ```

# Thông báo lỗi thường là:

# ```python
# TypeError:
# Can't instantiate abstract class Assassin
# with abstract method use_ultimate
# ```

# Như vậy lỗi xuất hiện ngay lúc loading trận đấu, trước khi giao tranh diễn ra.

# ---

# ## Câu 4. Nguyên lý Fail Fast được thể hiện như thế nào khi áp dụng Abstract Base Classes vào kiến trúc Game?

# Fail Fast có nghĩa là phát hiện và báo lỗi càng sớm càng tốt thay vì để lỗi tồn tại đến khi hệ thống đang hoạt động.

# Khi áp dụng Abstract Base Classes:

# ```python
# class Hero(ABC):
# ```

# và:

# ```python
# @abstractmethod
# ```

# Python sẽ kiểm tra xem các lớp con đã triển khai đầy đủ các phương thức bắt buộc hay chưa.

# Nếu một lớp con thiếu:

# ```python
# use_ultimate()
# ```

# thì đối tượng sẽ không thể được tạo ra.

# Nhờ đó:

# * Lỗi được phát hiện ngay từ giai đoạn khởi tạo.
# * Không cho phép dữ liệu sai đi vào hệ thống.
# * Tránh crash giữa trận đấu.
# * Dễ bảo trì và kiểm thử hơn.

# Đây chính là nguyên lý Fail Fast: báo lỗi sớm tại thời điểm phát sinh thay vì chờ đến Runtime.

# ---

# (2) SỬA LỖI (REFACTORING)


from abc import ABC, abstractmethod


# Lớp cha: Hero (Abstract Base Class)
class Hero(ABC):

    @abstractmethod
    def use_ultimate(self):
        pass


# Lớp con: Pháp Sư
class Mage(Hero):

    def use_ultimate(self):
        print("Pháp Sư tung chiêu: MƯA SAO BĂNG!")


# Lớp con: Sát Thủ
class Assassin(Hero):
    def use_ultimate(self):
        print("Sát Thủ tung chiêu: ÁM SÁT TỪ PHÍA SAU!")
print("--- LOADING TRẬN ĐẤU ---")
team_heroes = [Mage(), Assassin()]
print("Tải trận đấu thành công! Các tướng đã sẵn sàng...")
print("\n--- GIAO TRANH TỔNG BẮT ĐẦU ---")
for hero in team_heroes:
    hero.use_ultimate()
