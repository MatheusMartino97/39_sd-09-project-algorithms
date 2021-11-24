def study_schedule(permanence_period, target_time):
    if type(target_time) is not int:
        return None

    student_online_by_target_time_count = 0

    for (login_time, logout_time) in permanence_period:
        if type(login_time) is not int or type(logout_time) is not int:
            return None

        if login_time <= target_time <= logout_time:
            student_online_by_target_time_count += 1

    return student_online_by_target_time_count
