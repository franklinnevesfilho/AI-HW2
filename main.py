from solutions import island_count, sliding_puzzle

def print_usage():
    print("=====================================================")
    print("Usage: python main.py <problem_name> <attribute>")
    print("=====================================================\n")
    print("Problems:")
    print("  - island_count:")
    print("        attributes: dfs, bfs\n")
    print("  - sliding_puzzle:")
    print("        attribute: default, or grid format: [1-2-3][4-5-6][7-8-0]")
    print("\nExample for sliding_puzzle:")
    print("  python main.py sliding_puzzle '[1-2-3][4-5-6][7-8-0]'")
    print("=====================================================")

def convert_grid(grid):
    # Removing square brackets from the ends
    grid = grid.strip("[]")
    # Splitting by ][ to separate the rows
    return [[int(x) for x in row.split("-")] for row in grid.split("][")]

def main():
    import sys
    if len(sys.argv) < 3:
        print_usage()
        return

    problem_name = sys.argv[1]
    attribute = sys.argv[2]

    if problem_name == "island_count":
        if attribute not in ["dfs", "bfs"]:
            print_usage()
            return

        if attribute == "dfs":
            print(island_count(method="dfs"))
        else:
            print(island_count(method="bfs"))

    elif problem_name == "sliding_puzzle":
        if attribute == "default":
            # Provide a default grid if no custom grid is given
            print(sliding_puzzle([[0, 2, 4], [6, 1, 3], [7, 8, 5]]))
        else:
            try:
                # Convert the passed string to a grid
                grid = convert_grid(attribute)
                print(sliding_puzzle(grid))
            except ValueError:
                print("Invalid grid format. Please use the format: [1-2-3][4-5-6][7-8-0]")
                print_usage()
    else:
        print_usage()

if __name__ == '__main__':
    main()
