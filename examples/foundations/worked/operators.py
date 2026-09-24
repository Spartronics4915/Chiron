distance_m = 3.0
elapsed_s = 2.0
speed_m_per_s = distance_m / elapsed_s
enabled = True
under_limit = speed_m_per_s <= 2.0
print("Speed:", speed_m_per_s)
print("Allowed:", enabled and under_limit)
