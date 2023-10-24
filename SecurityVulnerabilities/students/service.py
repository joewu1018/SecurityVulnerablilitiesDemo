from .models import MissionRecord
from django.db.models import Max

class StudentService:
    def create_mission_record(user_id, mission_id, is_completed):
        max_attempts = MissionRecord.objects.filter(student_id=user_id, mission_id=mission_id).aggregate(Max('attempts'))['attempts__max']
        attempts = max_attempts + 1 if max_attempts != None else 1
        MissionRecord.objects.create(student_id=user_id, mission_id=mission_id, attempts=attempts, is_completed=is_completed)