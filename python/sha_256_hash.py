from sha_256_constants import *

def sha_256_secure_hash(M):

    schedule_arrays = []
    for chunk in M:
        schedule_array  =[0x00000000] * 64
        schedule_arrays.append(schedule_array)

    return schedule_arrays