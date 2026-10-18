from apscheduler.schedulers.blocking import BlockingScheduler
from agent import run_agent


def morning_report():

    task = """
    افحص بيانات النظام.
    حلل الوضع الحالي.
    حدد المشاكل المهمة.
    أنشئ ملخصاً واضحاً للإدارة.
    """

    result = run_agent(task)

    print("\n===== MORNING AI REPORT =====")
    print(result)


scheduler = BlockingScheduler()

scheduler.add_job(
    morning_report,
    "cron",
    hour=8,
    minute=0
)


print("AI Scheduler started...")

scheduler.start()