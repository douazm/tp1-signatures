
from signature import AdvancedSignature

def run_correctness_tests():
    sig_scheme = AdvancedSignature()
    priv_key, pub_key = sig_scheme.key_gen()

    message = "Sensor_ID_01: Temperature = 25.5C"
    signature = sig_scheme.sign(priv_key, message)

    print("--- بدء اختبارات الصحة (Correctness Tests) ---")

    # 1. اختبار الحالة الصحيحة (Valid Signature)
    assert sig_scheme.verify(pub_key, message, signature) == True, "فشل الاختبار: التوقيع الصحيح لم ينجح!"
    print("✅ [نجاح] التحقق من التوقيع السليم تم بنجاح.")

    # 2. اختبار تعديل الرسالة (Modified Message)
    tampered_message = "Sensor_ID_01: Temperature = 80.0C"
    assert sig_scheme.verify(pub_key, tampered_message, signature) == False, "فشل الاختبار: قبل رسالة معدلة!"
    print("✅ [نجاح] تم كشف تعديل الرسالة ورفض التوقيع.")

    # 3. اختبار مفتاح خاطئ (Wrong Key)
    wrong_pub_key = "fake_public_key"
    assert sig_scheme.verify(wrong_pub_key, message, signature) == False, "فشل الاختبار: قبل مفتاح خاطئ!"
    print("✅ [نجاح] تم رفض التوقيع عند استخدام مفتاح خاطئ.")

    print("--- جميع اختبارات الصحة اجتازت بنجاح! ---")

if __name__ == "__main__":
    run_correctness_tests()
