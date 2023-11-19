import sys

def calculate_partition_bounds(num_partitions):
    max_hash = 2**64 - 1
    partition_size = max_hash // num_partitions

    partition_bounds = []
    lower_bound = 0

    for i in range(num_partitions):
        upper_bound = lower_bound + partition_size - 1
        partition_bounds.append((lower_bound, upper_bound))
        lower_bound = upper_bound + 1

    return partition_bounds

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <num_partitions>")
        sys.exit(1)

    num_partitions = int(sys.argv[1])

    bounds = calculate_partition_bounds(num_partitions)
    for i, (lower, upper) in enumerate(bounds):
        print(f"Partition {i + 1}: Lower Bound = {hex(lower)}, Upper Bound = {hex(upper)}")
