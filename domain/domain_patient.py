from dataclasses import dataclass

@dataclass
class alarm_log:
    log_message: str
    time: str
    date: str

@dataclass
class PatientDetail:
    patient_Id: int
    name: str
    weight: int
    time: str
    date: str
    alarm_logs: list[alarm_log]


