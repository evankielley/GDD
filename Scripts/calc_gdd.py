def calc_gdd(min_temp_vect, max_temp_vect, tbase, tupper):
    if(len(min_temp_vect) == len(max_temp_vect)):
        if (tupper<tbase):
            print("Error in GDD calculation: tupper<tbase.")
            return None
        else:
            res = [None]*len(min_temp_vect)
            res_day = [None]*len(min_temp_vect)
            for i in range(len(min_temp_vect)):
                try:
                    min_temp_val = min(tupper, max(tbase, min_temp_vect[i]))
                except TypeError:
                    print("Error in GDD calculation: wrong input data at "+str(i)+"th entry. Minimum temperature should be a number.")
                    return None
                except:
                    print("Error in GDD calculation: unexpected error at "+str(i)+"th entry.")
                    return None
                try:
                    max_temp_val = min(tupper, max(tbase, max_temp_vect[i]))
                except TypeError:
                    print("Error in GDD calculation: wrong input data at "+str(i)+"th entry. Maximum temperature should be a number.")
                    return None
                except:
                    print("Error in GDD calculation: unexpected error at "+str(i)+"th entry.")
                    return None
                if(min_temp_val>max_temp_val):
                    print("Error in GDD calculation: wrong input data at "+str(i)+"th entry. Maximum temperature can't be lower then minimum.")
                    return None
                else:
                    res_day[i] = (min_temp_val+max_temp_val)/2 - tbase
                    # calculating cumulative GDD
                    if(i>0):
                        res[i] = res[i-1] +res_day[i]
                    else:
                        res[i] = res_day[i]
            return (res_day, res)
    else:
        print("Error in GDD calculation: data should have the same size.")
        return None
