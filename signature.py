# TP1: Advanced Digital Signature Scheme (Python)
import hashlib

class AdvancedSignature:
    def __init__(self):
        print("Initializing Signature Scheme...")

    def key_gen(self):
        """1. توليد المفاتيح (KeyGen)"""
        # ضع هنا كود توليد المفاتيح الخاص بالخوارزمية المختارة
        private_key = "dummy_private_key"
        public_key = "dummy_public_key"
        return private_key, public_key

    def sign(self, private_key, message):
        """2. إنشاء التوقيع (Sign)"""
        # ضع هنا منطق التوقيع الرقمي المتقدم
        signature = hashlib.sha256((private_key + message).encode()).hexdigest()
        return signature

    def verify(self, public_key, message, signature):
        """3. التحقق من التوقيع (Verify)"""
        # ضع هنا منطق التحقق من صحة التوقيع
        expected_sig = hashlib.sha256(("dummy_private_key" + message).encode()).hexdigest()
        return signature == expected_sig

# اختبار سريع للتأكد من صحة العمل
if __name__ == "__main__":
    sig_scheme = AdvancedSignature()
    priv, pub = sig_scheme.key_gen()
    msg = "Hello IoT Sensor Data"

    signature = sig_scheme.sign(priv, msg)
    is_valid = sig_scheme.verify(pub, msg, signature)

    print(f"Message Signature: {signature}")
    print(f"Is Signature Valid? {is_valid}")
