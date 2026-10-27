
import time
import json
from signature import AdvancedSignature

def simulate_iot_network():
    print("--- بدء محاكاة شبكة IoT عبر MQTT ---")
    sig_scheme = AdvancedSignature()
    priv_key, pub_key = sig_scheme.key_gen()
    
    # محاكاة 10 حساسات تنشر قراءاتها إلى البوابة (Gateway)
    sensors = [f"Sensor_Node_{i+1}" for i in range(10)]
    
    for sensor in sensors:
        payload = f"{sensor} - Temperature: 24.5C"
        signature = sig_scheme.sign(priv_key, payload)
        
        # حزمة البيانات المرسلة عبر Mosquitto MQTT Broker
        mqtt_message = {
            "sensor_id": sensor,
            "data": payload,
            "signature": signature
        }
        
        # البوابة تتحقق من الرسالة المستقبلة
        is_verified = sig_scheme.verify(pub_key, mqtt_message["data"], mqtt_message["signature"])
        
        status = "✅ مقبولة (Verified)" if is_verified else "❌ مرفوضة (Failed)"
        print(f"[Gateway Received] From: {mqtt_message['sensor_id']} | Data: {mqtt_message['data']} | Status: {status}")
        time.sleep(0.2)

if __name__ == "__main__":
    simulate_iot_network()
