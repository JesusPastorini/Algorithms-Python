def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    count = 0
    for entry, exit in permanence_period:
        if not (isinstance(entry, int) and isinstance(exit, int)):
            return None
        if entry <= target_time <= exit:
            count += 1

    return count
