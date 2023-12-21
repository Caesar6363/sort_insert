### Сортировка вставками/Sorting by inserts
def git init(arr):
    for i in range(1, len(arr)): #создаем_переменную_i_и_входим_в_длинну_arr_со_значением_1
                                 #create_variable_i_and_enter_in_length_arr_with_value_1
        key = arr[i]    #создаем_переменную_key_присваиваем_значение_arr[i]
                        # create_variable_key_assign_value_arr[i]
        j = i-1     #создаем_переменную_j_отнимаем_значение_i-1
                    #create_variable_j_subtract_value_i-1
        while j >= 0 and arr[j] > key:      #пока_j_больше_или_равна_0_и_arr[j]_больше_key
                                            # while_j_is_more_or_equal_0_and_arr[j]_more_key
            arr[j+1] = arr[j]   #делаем_обмен_значениями
                                #making_the_value_exchange
            j -= 1

        arr[j+1] = key

arr = [2, 5, 7, 4, 9, 1, 8, 14]
sort_insert(arr)
print(f'"Сортировка вставками": {arr}')













