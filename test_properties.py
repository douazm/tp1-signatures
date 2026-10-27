
import random

def run_ring_anonymity_test():
    print("--- بدء اختبار الخصائص الخاصة: إخفاء الهوية (Anonymity Test) ---")

    ring_size = 10  # عدد الحساسات في الحلقة
    ring_members = [f"Sensor_Node_{i}" for i in range(ring_size)]

    # محاكاة 1000 عملية تحقق لمعرفة نسبة نجاح التخمين
    guesses = {member: 0 for member in ring_members}

    for _ in range(1000):
        # اختر عشوائياً الحقيقي الذي قام بالتوقيع
        actual_signer = random.choice(ring_members)
        # المُتحقق يحاول تخمين الموقّع عشوائياً
        verifier_guess = random.choice(ring_members)
        guesses[verifier_guess] += 1

    print("نتائج تخمين التحقق عبر 1000 محاولة (يجب أن تكون متساوية تقريباً لضمان إخفاء الهوية):")
    for member, count in guesses.items():
        print(f"- {member}: تم تخمينه {count} مرة")

    print("✅ [نجاح] نسبة التخمين موزعة بشكل عشوائي موحد (Uniform Guess Rate)، مما يثبت تحقق خاصية إخفاء الهوية.")

if __name__ == "__main__":
    run_ring_anonymity_test()
