from memory import get_memory_text
from config import SYSTEM_PROMPT, MODEL, MAX_TOOL_CALLS
from tools import (
    get_current_time,
    calculate,
    list_documents,
    read_document,
    create_document,
)
from data_tools import analyze_csv
from report_tools import create_pdf_report
from database import get_vehicle_count
from ollama import chat

# قائمة الأدوات المتاحة
TOOLS = [
    get_current_time,
    calculate,
    list_documents,
    read_document,
    create_document,
    analyze_csv,
    create_pdf_report,
    get_vehicle_count,
]

# قاموس يربط اسم الأداة بالدالة الخاصة بها
AVAILABLE_FUNCTIONS = {
    "get_current_time": get_current_time,
    "calculate": calculate,
    "list_documents": list_documents,
    "read_document": read_document,
    "create_document": create_document,
    "analyze_csv": analyze_csv,
    "create_pdf_report": create_pdf_report,
    "get_vehicle_count": get_vehicle_count,
}

def run_agent(user_message: str):
    # 1. جلب الذاكرة السابقة
    memory = get_memory_text()

    # 2. بناء قائمة الرسائل
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    # 3. إضافة الذاكرة إذا كانت موجودة
    if memory:
        messages.append(
            {
                "role": "system",
                "content": f"""
هذه بعض المحادثات السابقة:

{memory}
"""
            }
        )

    # 4. إضافة رسالة المستخدم
    messages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    # 5. حلقة تنفيذ الأدوات
    for _ in range(MAX_TOOL_CALLS):
        response = chat(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
        )

        messages.append(response.message)

        # إذا ماكو أدوات مطلوبة، نرجع الرد النهائي
        if not response.message.tool_calls:
            return response.message.content

        # إذا الموديل طلب أدوات، ننفذها
        for tool_call in response.message.tool_calls:
            function_name = tool_call.function.name
            arguments = tool_call.function.arguments

            print(f"\n[Agent Tool] {function_name}")
            print(f"[Arguments] {arguments}")

            function = AVAILABLE_FUNCTIONS.get(function_name)

            if function is None:
                result = "Unknown tool."
            else:
                try:
                    result = function(**arguments)
                except Exception as e:
                    result = f"Tool error: {e}"

            print(f"[Result] {result}")

            # إضافة نتيجة الأداة للرسائل
            messages.append(
                {
                    "role": "tool",
                    "tool_name": function_name,
                    "content": str(result),
                }
            )

    # إذا وصلنا للحد الأقصى من الأدوات
    return "تم الوصول إلى الحد الأقصى لعمليات الأدوات."