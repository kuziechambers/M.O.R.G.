from datetime import time as ti

# away times
morning_start_away = ti(7, 00, 00, 000000)
morning_end_away = ti(10, 59, 59, 000000)

afternoon_start_away = ti(11, 00, 00, 000000)
afternoon_end_away = ti(19, 00, 59, 000000)

evening_start_away = ti(19, 1, 00, 000000)
evening_end_away = ti(22, 00, 00, 000000)


# arriving times
morning_start_office = ti(7, 15, 00, 000000)
morning_end_office = ti(9, 45, 00, 000000)

morning_start = ti(8, 00, 00, 000000)
morning_end = ti(10, 59, 59, 000000)

afternoon_start = ti(11, 00, 00, 000000)
afternoon_end = ti(17, 14, 59, 000000)

evening_start = ti(17, 15, 00, 000000)
evening_end = ti(23, 44, 59, 000000)

latenight_start = ti(23, 55, 00, 000000)
latenight_end = ti(1, 55, 00, 000000)

