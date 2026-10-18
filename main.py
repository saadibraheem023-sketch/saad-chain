from agent import run_agent
from memory import initialize_database, save_memory


def main():

    initialize_database()

    print("=" * 50)
    print("       SAAD PERSONAL AI AGENT")
    print("=" * 50)

    print("اكتب exit للخروج.")
    print()

    while True:

        user_input = input("أنت: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ["exit", "quit"]:

            print("تم إغلاق Agent.")
            break

        try:

            answer = run_agent(user_input)

            print("\nAI:")
            print(answer)
            print()

            save_memory(
                user_input,
                answer
            )

        except Exception as e:

            print("\nERROR:")
            print(e)
            print()


if __name__ == "__main__":
    main()