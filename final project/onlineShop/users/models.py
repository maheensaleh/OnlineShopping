from django.db import models
from home.models import BasicPerson


class InvalidInput(Exception): #if there is error in start or end time

    @staticmethod
    def syntax():
        print(' You have entered incorrect format, the correct format is: "hours AM/PM"  ')


class Employee(BasicPerson):

    dept = models.CharField(max_length=300, default='')
    st = models.CharField(max_length=10, default='')
    et = models.CharField(max_length=10, default='')
    designation = models.CharField(max_length=200, default='')
    qualification = models.CharField(max_length=200, default='')

    #  following attributes are calculated by create_sal method
    total_hours = models.CharField(max_length=10, default='')
    salary = models.CharField(max_length=50, default='')

    def create_sal(self):  # name 'create' by convention

        try:
            total_pay = 50000 #an avg amount set
            per_hr_pay = ((total_pay * 10) / 100)

            if len(self.st) > 5 or len(self.et) > 5:
                raise InvalidInput()

            l = [self.st, self.et]
            st_hr_only = ''
            et_hr_only = ''

            et_hr_only=l[1][2]
            st_hr_only=l[0][2]

            if len(st_hr_only) == 2 or len(et_hr_only) == 2:
                dur = abs(int(st_hr_only) - int(et_hr_only))
            else:
                dur = 12 - int(st_hr_only) + int(et_hr_only)

            i_dur = int(dur)

            if i_dur != 8:
                change_in_pay = per_hr_pay * abs((8 - i_dur))
                if i_dur < 8:
                    total_pay = total_pay - change_in_pay
                else:
                        total_pay = total_pay + change_in_pay

            # the attributes have now been assigned
            self.salary = (total_pay)
            self.total_hours = (dur)

        except InvalidInput as e:
            e.syntax()

    def save(self):  # save method is overridden here to call the other method implicitly
        if self.st and self.et:
            self.create_sal()
        super(Employee, self).save() #calling the normal save method

    def __str__(self):
        return self.name + '-' + self.designation
