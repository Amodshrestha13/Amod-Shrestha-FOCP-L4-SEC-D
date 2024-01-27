import sys


def read_log(file_path):
    cat_visits = 0
    intruder_count = 0
    total_time = 0
    longest = 0
    shortest = float('inf')

    with open(file_path, 'r') as file:
        for line in file:
            if line.strip() == 'END':
                break

            cat, entry, exit = line.strip().split(',')
            entry, exit = int(entry), int(exit)
            duration = exit - entry

            if cat == 'OURS':
                cat_visits += 1
                total_time += duration

                if duration > longest:
                    longest = duration

                if duration < shortest:
                    shortest = duration
            else:
                intruder_count += 1

    return cat_visits, intruder_count, total_time, longest, shortest


def format_duration(minutes):
    hours, minutes = divmod(minutes, 60)
    return f"{hours} Hours, {minutes} Minutes"


def amd():
    if len(sys.argv) != 2:
        print("Missing command line argument!")
        return

    file_path = sys.argv[1]
    cat_visits, intruder_count, total_time, longest, shortest = read_log(file_path)

    print(f'Cat Visits:{cat_visits}')
    print(f'Other Cats:{intruder_count}')
    print('Total Time in House:',format_duration(total_time))
    print('Average Length:',format_duration(total_time // cat_visits))
    print('Longest Visit:',format_duration(longest))
    print('Shortest Visit:',format_duration(shortest))


amd()