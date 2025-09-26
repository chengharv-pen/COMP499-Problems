import sys

def possible(s: str) -> bool:
    n = len(s)

    # try every offset b = 0..6
    for b in range(7):
        blocks = {}
        ok = True

        for i, ch in enumerate(s):
            block_id = (i + b) // 7 # which segment of 7 blocks is it in?
            st = blocks.get(block_id)

            if st is None:
                blocks[block_id] = {ch} # append to dictionary of blocks for current 7-block segment
            else:
                if ch in st: # yes makes sense
                    ok = False
                    break
                st.add(ch)

        if ok:
            return True

    return False

def main():
    t = int(input().strip())

    for _ in range(t):
        s = input().strip()
        if possible(s):
            print(1)
        else:
            print(0)

if __name__ == "__main__":
    main()