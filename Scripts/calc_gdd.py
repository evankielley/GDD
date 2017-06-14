def calc_gdd(min_temp_vect, max_temp_vect, tbase, tupper):
    """
        Computes gdd (per day and cumulative) from minimum and maximum temperatures, Tbase and Tupper

        Specification:
            (<list<float>>, <list<float>>) calc_gdd(<list<float>>, <list<float>>, <float>, <float>)
        Checks if data is consistent, if not - prints message and returns None.
    """
    if(len(min_temp_vect) == len(max_temp_vect)):
        try:
            float(tbase)
        except:
            print("Error in GDD calculation: tbase is not a number.")
            return None
        try:
            float(tupper)
        except:
            print("Error in GDD calculation: tupper is not a number.")
            return None
        if (tupper<tbase):
            print("Error in GDD calculation: tupper<tbase.")
            return None
        else:
            res = [None]*len(min_temp_vect)
            res_day = [None]*len(min_temp_vect)
            for i in range(len(min_temp_vect)):
                # Put min_temp to the range (tbase, tupper)
                try:
                    min_temp_val = min(tupper, max(tbase, min_temp_vect[i]))
                except TypeError:
                    print("Error in GDD calculation: wrong input data at "+str(i)+"th entry. Minimum temperature should be a number.")
                    return None
                except:
                    print("Error in GDD calculation: unexpected error at "+str(i)+"th entry.")
                    return None
                # Put min_temp to the range (tbase, tupper)
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
