# dict_1 --> student_id(int): student_name(str)
dict_1 = {"1": "Name 1",
          "2": "Name 2",
          "3": "Name 3",
          "4": "Name 4",
          "5": "Name 5",
          "6": "Name 6",
          "7": "Name 7",
          "8": "Name 8",
          "9": "Name 9",
          "10": "Name 10",
          "11": "Name 11",
          "12": "Name 12",
          "13": "Name 13",
          "14": "Name 14",
          "14": "Name 15",
          "16": "Name 16"
          }

# dict_2 --> student_id(int): exam_score(int)
dict_2 = {"1": "50",
          "2": "60",
          "3": "70",
          "4": "80",
          "6": "48",
          "7": "55",
          "8": "45",
          "9": "90",
          "10": "95",
          "11": "64",
          "12": "78",
          "13": "88",
          "14": "52",
          "15": "98",
          "16": "72"
          }

inverse = dict([(value, key) for (key, value) in dict_2.items()])
best_score = max(inverse)
best_student = inverse[best_score]

result = {}
result[best_student] = best_score

print(result)