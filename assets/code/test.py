# Import thư viện random.
import random


# Chọn một cửa ngẫu nhiên số từ 1 -> 3.
def choose():
    return random.randint(1, 3)


# Chọn một cửa ngẫu nhiên trong những cửa chưa được chọn.
def get_unchoosen_door(chosen_doors):
    doors_selection = [1, 2, 3]

    # Loại bỏ những cửa đã chọn.
    for choice in chosen_doors:
        if choice in doors_selection:
            doors_selection.remove(choice)

    # Nếu có một cửa chưa được chọn thì chọn cửa đó. Nếu không chọn ngẫu nhiên 1 trong 2 cửa còn lại.
    if len(doors_selection) == 1:
        return doors_selection[0]
    else:
        return doors_selection[random.randint(0, 1)]


# List để lưu lại các kết quả
RESULTS = []

# Variable lưu lại số lượt thắng
WINS = 0

# Strategy (chiến thuật) 0: giữ nguyên lựa chọn ban đầu.
# strategy (chiến thuật) 1: đổi cửa.
STRATEGY = 1

# Số lượt thử
TEST_SAMPLE = 100000


for test in range(TEST_SAMPLE):
    # Variable lưu lại kết quả của mỗi lượt.
    result = ""

    # Chọn ngẫu nhiên một cửa đúng.
    correct_door = choose()

    # Người chơi chọn một cửa.
    first_choice = choose()

    # MC mở một ra một cửa sai.
    # Lưu ý: mc luôn mở ra cửa sai và không phải là cửa người chơi đã chọn.
    incorrect_door = get_unchoosen_door([first_choice, correct_door])

    # Lưu lại lựa chọn.
    result += f"1st choice: {first_choice} | incorrect door: {incorrect_door} | correct door: {correct_door}"

    if STRATEGY:
        # Nếu chọn chiến thuật 1 người chơi sẽ đổi cửa.
        final_choice = get_unchoosen_door([first_choice, incorrect_door])
        result += f" | final choice: {final_choice}"
    else:
        # Nếu chọn chiến thuật 0 người chơi sẽ giữ nguyên lựa chọn ban đầu.
        final_choice = first_choice
        result += " | final choice: unchanged"

    if final_choice == correct_door:
        # Nếu người chơi chọn đúng cửa, tăng số lượt thắng lên 1
        WINS += 1
        result += " | result: win"
    else:
        result += " | result: lose"

    # Thêm kết quả của lượt chơi vào list các kết quả
    RESULTS.append(result)

# In ra một số kết quả mẫu
for r in range(5):
    print(RESULTS[r])

# In ra tổng kết.
print(f"Test sample: {TEST_SAMPLE}")
print(f"Strategy: {STRATEGY} ({'change door when offered' if STRATEGY else 'do not change door when offered'})")
print(f"Wins: {WINS}")
print(f"Winning probability: {WINS / TEST_SAMPLE}")
