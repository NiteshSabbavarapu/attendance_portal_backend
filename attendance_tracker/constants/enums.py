from enum import Enum


class BaseEnum(Enum):

    @classmethod
    def get_list_of_tuples(cls):
        gender_list = []
        for i in cls:
            gender_list.append((i.name, i.value))
        return gender_list

    @classmethod
    def get_list_of_values(cls):
        values_list = []
        for i in cls:
            values_list.append(i.value)
        return values_list


class Attendance_Status(BaseEnum):
    present = "present"
    absent = "absent"
