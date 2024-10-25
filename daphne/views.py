import random
from datetime import datetime, timedelta
from django.http import JsonResponse
from .models import Daphne  # Modelinizi uygun şekilde içe aktarın

def create_monthly_shift_schedule(request):
    staff_members = list(Daphne.objects.all())  # Tüm personeli listele
    total_weeks = 2  # Aylık plan için 2 hafta
    shifts = []

    total_staff = len(staff_members)
    half_staff = total_staff // 2  # Toplam çalışan sayısının yarısı

    # 1. hafta Cumartesi ve Pazar izin kullananları belirle
    if total_staff > 0:
        saturday_staff_week1 = random.sample(staff_members, half_staff)
        sunday_staff_week1 = [staff for staff in staff_members if staff not in saturday_staff_week1]

        # 2. hafta izinli olacak çalışanları belirle
        saturday_staff_week2 = sunday_staff_week1  # 1. hafta Pazar izin kullananlar 2. hafta Cumartesi
        sunday_staff_week2 = saturday_staff_week1  # 1. hafta Cumartesi izin kullananlar 2. hafta Pazar

        weekend_shifts = {
            'Saturday_week1': saturday_staff_week1,
            'Sunday_week1': sunday_staff_week1,
            'Saturday_week2': saturday_staff_week2,
            'Sunday_week2': sunday_staff_week2
        }
    else:
        weekend_shifts = {key: [] for key in ['Saturday_week1', 'Sunday_week1', 'Saturday_week2', 'Sunday_week2']}  # Eğer hiç çalışan yoksa boş listeler

    # Hafta içi izinlerini belirle
    haftaici_of = {}
    haftaici_days = [0, 1, 2, 3, 4]  # Pazartesi - Cuma
    assigned_days = []  # Atanan hafta içi izin günleri

    for staff_member in staff_members:
        # Haftada 1 gün hafta içi izni (farklı günlerde)
        available_days = list(set(haftaici_days) - set(assigned_days))  # Önceden atanmamış günler
        if available_days:
            haftaici_day = random.choice(available_days)
            assigned_days.append(haftaici_day)  # Atanan günü kaydet
            haftaici_of[staff_member] = [
                day + week * 7 for week in range(total_weeks) for day in [haftaici_day]
            ]

    # Vardiya saatleri
    shift_start_times = [datetime.combine(datetime.now().date(), datetime.min.time()).replace(hour=h) for h in range(9, 17)]  # 4 saat aralıklarla

    for week in range(total_weeks):
        current_week_start = (datetime.now().date().replace(day=1) + timedelta(weeks=week))

        for day in range(7):  # Haftanın her günü
            current_date = current_week_start + timedelta(days=day)
            week_day = current_date.weekday()  # 0: Pazartesi, 1: Salı, ..., 5: Cumartesi, 6: Pazar

            # İzinli olmayan çalışanları listele
            available_staff = []
            if week == 0:  # 1. hafta
                if week_day == 5:  # Cumartesi
                    available_staff = [
                        staff_member for staff_member in staff_members 
                        if staff_member not in weekend_shifts['Saturday_week1'] and current_date.day not in haftaici_of.get(staff_member, [])
                    ]
                elif week_day == 6:  # Pazar
                    available_staff = [
                        staff_member for staff_member in staff_members 
                        if staff_member not in weekend_shifts['Sunday_week1'] and current_date.day not in haftaici_of.get(staff_member, [])
                    ]
                else:  # Hafta içi
                    available_staff = [
                        staff_member for staff_member in staff_members 
                        if current_date.day not in haftaici_of.get(staff_member, [])
                    ]
            else:  # 2. hafta
                if week_day == 5:  # Cumartesi
                    available_staff = [
                        staff_member for staff_member in staff_members 
                        if staff_member not in weekend_shifts['Saturday_week2'] and current_date.day not in haftaici_of.get(staff_member, [])
                    ]
                elif week_day == 6:  # Pazar
                    available_staff = [
                        staff_member for staff_member in staff_members 
                        if staff_member not in weekend_shifts['Sunday_week2'] and current_date.day not in haftaici_of.get(staff_member, [])
                    ]
                else:  # Hafta içi
                    available_staff = [
                        staff_member for staff_member in staff_members 
                        if current_date.day not in haftaici_of.get(staff_member, [])
                    ]

            # Eğer mevcut personel yoksa, atla
            if not available_staff:
                shifts.append(f"{current_date} : Dükkan kapalı, yeterli personel yok.")
                continue

            # Vardiya sürelerini belirle ve sırayla dağıt
            for i in range(min(len(available_staff), len(shift_start_times))):
                staff_member = available_staff[i]
                shift_start_time = shift_start_times[i % len(shift_start_times)]
                end_time = shift_start_time + timedelta(hours=4)  # Her vardiya 4 saat

                if end_time.hour > 20:  # Eğer vardiya kapanış saati 20:00'i geçerse, atla
                    continue

                # Vardiya bilgisini listeye ekle
                shifts.append(f"{staff_member.user.username} - {current_date} : {shift_start_time.time()} - {end_time.time()}")

            # İzinli olan çalışanlar için bilgiyi ekle
            izinli_staff = set()  # İzinli çalışanları set olarak tut
            for staff_member in staff_members:
                if current_date.day in haftaici_of.get(staff_member, []) or \
                   (week_day == 5 and staff_member in weekend_shifts['Saturday_week1']) or \
                   (week_day == 6 and staff_member in weekend_shifts['Sunday_week1']) or \
                   (week_day == 5 and staff_member in weekend_shifts['Saturday_week2']) or \
                   (week_day == 6 and staff_member in weekend_shifts['Sunday_week2']):
                    izinli_staff.add(staff_member.user.username)  # İzinli olanları set'e ekle

            # İzinli çalışanların bilgilerini ekle, ancak vardiya alanları hariç
            for staff_member in izinli_staff:
                if staff_member not in [s.user.username for s in available_staff]:
                    shifts.append(f"{staff_member} - {current_date} : İzinli")

    return JsonResponse({"shifts": shifts})
