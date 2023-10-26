def is_interesting(time_str):
    digits = set(time_str.replace(':', ''))
    return len(digits) <= 2

def solution(S, T):
    count = 0
    current_time = S

    while current_time <= T:
        if is_interesting(current_time):
            count += 1
        
        # Increment the time by one second
        h, m, s = map(int, current_time.split(':'))
        s += 1
        if s == 60:
            s = 0
            m += 1
            if m == 60:
                m = 0
                h += 1
                if h == 24:
                    h = 0

        current_time = f"{h:02d}:{m:02d}:{s:02d}"

    return count

# Test cases
print(solution("15:15:00", "15:15:12"))  # Should return 1
print(solution("22:22:21", "22:22:23"))  # Should return 3
