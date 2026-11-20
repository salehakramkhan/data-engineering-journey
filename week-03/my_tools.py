
# helper function
def clean_amount(text):
    amount  = float(text.strip().replace("৳", "").replace(",", ""))
    return amount

def taka(amount):
    return f"৳{amount:.2f}"

def read_lines(path):
    with open(path, encoding='utf-8') as fh:
        lines = fh.read().strip().split('\n')
    return lines


if __name__ == "__main__":
    print(clean_amount(" ৳ 1,240.50 "))    # 1240.5
    print(taka(1240.5))                     # ৳1240.50
    
    
    