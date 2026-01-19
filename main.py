class Student:
    def __init__(self, name, roll, course, password):
        self.name = name
        self.roll = roll
        self.course = course
        self.__password = password

    def get_pass(self):
        return self.__password


# ডাটা ফাইলে সেভ করার ফাংশন
def save_to_file(student):
    # এখানে encoding="utf-8" যোগ করা হয়েছে
    file = open("students.txt", "a", encoding="utf-8")
    info = f"নাম: {student.name} | রোল: {student.roll} | কোর্স: {student.course}\n"
    file.write(info)
    file.close()


# ডাটা ফাইল থেকে পড়ার ফাংশন
def show_all():
    print("\n--- বর্তমানে ভর্তি হওয়া ছাত্র-ছাত্রীরা ---")
    try:
        # পড়ার সময়ও encoding="utf-8" দিতে হবে
        file = open("students.txt", "r", encoding="utf-8")
        print(file.read())
        file.close()
    except FileNotFoundError:
        print("এখনো কোনো ডাটা সেভ করা হয়নি।")


# --- মূল প্রোগ্রাম (একই থাকবে) ---
while True:
    print("\n১. নতুন ছাত্র ভর্তি (Enroll)")
    print("২. সব ছাত্রের তালিকা দেখা (Show All)")
    print("৩. বন্ধ করুন (Exit)")

    choice = input("আপনার পছন্দ (১/২/৩): ")

    if choice == '1':
        name = input("নাম লিখুন: ")
        roll = input("রোল লিখুন: ")
        course = input("কোর্সের নাম লিখুন: ")
        password = input("একটি পাসওয়ার্ড দিন: ")

        new_student = Student(name, roll, course, password)
        save_to_file(new_student)
        print("সফলভাবে সেভ হয়েছে!")

    elif choice == '2':
        show_all()

    elif choice == '3':
        print("প্রোগ্রামটি বন্ধ হচ্ছে। ধন্যবাদ!")
        break

    else:
        print("ভুল অপশন! আবার চেষ্টা করুন।")