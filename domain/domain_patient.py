from dataclasses import dataclass
from enum import Enum

@dataclass
class alarm_log:
    log_message: str
    time: str
    date: str

class Gender(Enum):
    MALE = 'male'
    FEMALE = 'female'

@dataclass
class PatientDetail:
    patient_Id: int
    name: str
    weight: int
    gender: Gender
    time: str
    date: str
    alarm_logs: list[alarm_log]

   


