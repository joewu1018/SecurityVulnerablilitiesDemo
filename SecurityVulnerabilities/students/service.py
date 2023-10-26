from .models import MissionRecord, Mission
from django.db.models import Max

class StudentService:
    # 建立任務紀錄
    def create_mission_record(user_id, mission_id, is_completed):
        max_attempts = StudentService.get_max_attempts(user_id, mission_id)
        attempts = max_attempts + 1 if max_attempts != None else 1
        MissionRecord.objects.create(student_id=user_id, mission_id=mission_id, attempts=attempts, is_completed=is_completed)

    # 取得該使用者該任務最大嘗試次數
    def get_max_attempts(user_id, mission_id):
        max_attempts = MissionRecord.objects.filter(student_id=user_id, mission_id=mission_id).aggregate(Max('attempts'))['attempts__max']
        return max_attempts if max_attempts != None else 0
    
    # 取得該類別所有任務資訊
    def get_missions_info(user_id, category_id):
        missions_info = []
        missions = Mission.objects.filter(category_id=category_id)
        missions_complete_count = 0
        for mission in missions:
            records = MissionRecord.objects.filter(student_id=user_id, mission_id=mission.id)
            is_completed = records.filter(is_completed=True).exists()
            if is_completed:
                missions_complete_count += 1
            missions_info.append({
                'mission': mission,
                'records': records,
                'is_completed': is_completed,
                'attempts': StudentService.get_max_attempts(user_id, mission.id),
                'last_attempt': records.order_by('-created_at').first().created_at if records.exists() else ''
            })
        return missions_info, missions_complete_count
    
