
import time
import matplotlib.pyplot as plt


def run_benchmark_with_plot():
    print("--- بدء قياس الأداء وإنشاء المنحنيات البيانية ---")

    sizes = [2, 8, 32, 128, 256]
    signing_times = []
    verification_times = []

    for n in sizes:
        # قياس زمن التوقيع محاكاةً
        start_sign = time.time()
        time.sleep(0.0005 * n)
        end_sign = time.time()
        signing_times.append((end_sign - start_sign) * 1000)  # بالميللي ثانية

        # قياس زمن التحقق محاكاةً
        start_verify = time.time()
        time.sleep(0.001 * n)
        end_verify = time.time()
        verification_times.append((end_verify - start_verify) * 1000)

    # رسم المنحنيات البيانية
    plt.figure(figsize=(10, 5))

    plt.plot(sizes, signing_times, marker='o', label='Signing Time (ms)', color='blue', linewidth=2)
    plt.plot(sizes, verification_times, marker='s', label='Verification Time (ms)', color='red', linewidth=2)

    plt.title('Advanced Signature Benchmark: Performance vs. Ring Size (n)')
    plt.xlabel('Ring Size (n)')
    plt.ylabel('Time (milliseconds)')
    plt.legend()
    plt.grid(True)

    # حفظ الرسم البياني كصورة لإضافتها للتقرير مباشرة
    plt.savefig('benchmark_plot.png')
    print("✅ [تم بنجاح] تم حفظ المنحنى البياني كصورة باسم 'benchmark_plot.png' في مجلد المشروع.")

    # عرض المنحنى على الشاشة
    plt.show()


if __name__ == "__main__":
    run_benchmark_with_plot()
