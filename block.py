class Block:
    def __init__(self, name):
        self.name = name
        self.on_top_of = None

    def __repr__(self):
        return self.name


def print_state(blocks):
    for block in blocks:
        if block.on_top_of is None:
            print(f"{block} is on the table")
        else:
            print(f"{block} is on top of {block.on_top_of}")


def find_block(name, blocks):
    for block in blocks:
        if block.name == name:
            return block
    return None


def clear_block(block, blocks):
    for b in blocks:
        if b.on_top_of == block:
            clear_block(b, blocks)
            b.on_top_of = None


def is_legal_move(block, new_base, blocks):
    if block.on_top_of is None:
        return True
    if new_base.on_top_of is None:
        return True
    if block.on_top_of == new_base:
        return False
    return is_legal_move(block.on_top_of, new_base, blocks)


def move_block(block, new_base, blocks):
    if not is_legal_move(block, new_base, blocks):
        print(f"Error: cannot move block {block} onto {new_base}")
        return
    clear_block(block, blocks)
    block.on_top_of = new_base
    print_state(blocks)


def main():
    num_blocks = int(input("Enter the number of blocks: "))
    blocks = [Block(str(i)) for i in range(num_blocks)]
    print("Initial state:")
    print_state(blocks)

    while True:
        move = input("Enter move (block new_base or q to quit): ")
        if move == "q":
            break
        block_name, new_base_name = move.split()
        block = find_block(block_name, blocks)
        new_base = find_block(new_base_name, blocks)
        if block is None or new_base is None:
            print("Error: block not found")
            continue
        move_block(block, new_base, blocks)


if __name__ == "__main__":
    main()
