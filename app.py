import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import streamlit as st

# 1. إعداد عنوان وتصميم الصفحة
st.set_page_config(
    page_title="تطبيق توقع أسعار الهواتف الذكية", page_icon="📱", layout="centered"
)

st.title("📱 نموذج الذكاء الاصطناعي لتوقع فئة أسعار الهواتف")
st.write(
    "هذا التطبيق يستخدم خوارزميات التعلم الآلي لتوقع فئة سعر الهاتف بناءً على"
    " المواصفات التقنية."
)

# 2. إنشاء بيانات تدريب وهمية وبسيطة للنموذج (لغرض التسهيل في الشرح)
# الأعمدة: [RAM (GB), Storage (GB), Battery (mAh)]
# الفئة: [0 = رخيص, 1 = متوسط, 2 = غالي/رائد]
data = {
    "RAM": [2, 4, 6, 8, 12, 4, 8, 6, 16],
    "Storage": [32, 64, 128, 128, 256, 64, 256, 128, 512],
    "Battery": [3000, 4000, 4500, 5000, 5000, 3500, 4500, 4000, 5500],
    "Price_Category": [0, 0, 1, 1, 2, 0, 2, 1, 2],
}

df = pd.DataFrame(data)

# تدريب نموذج Machine Learning (Random Forest)
X = df[["RAM", "Storage", "Battery"]]
y = df["Price_Category"]

model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# 3. تصميم واجهة الإدخال للمستخدم (Sidebar أو Main Screen)
st.sidebar.header("🎛️ أدخل مواصفات الهاتف:")

user_ram = st.sidebar.slider(
    "حجم الذاكرة العشوائية (RAM بالجيجابايت):", 2, 16, 4
)
user_storage = st.sidebar.selectbox(
    "مساحة التخزين الداخلية (Storage بالجيجابايت):", [32, 64, 128, 256, 512]
)
user_battery = st.sidebar.slider(
    "سعة البطارية (Battery بالمللي أمبير):", 2500, 6000, 4000
)

# عرض خيارات المستخدم على الشاشة الرئيسية
st.subheader("📊 المواصفات المختارة:")
st.write(
    f"- **الـ RAM:** {user_ram} جيجابايت"
    f" \n- **التخزين:** {user_storage} جيجابايت \n- **البطارية:**"
    f" {user_battery} ملي أمبير"
)

# 4. زر التوقع والنتيجة
if st.button("🚀 توقع فئة السعر الآن"):
  # تجهيز الإدخال للنموذج
  input_data = pd.DataFrame(
     [[user_ram, user_storage, user_battery]],
     columns=["RAM", "Storage", "Battery"],
  )

  # تنبؤ النتيجة
  prediction = model.predict(input_data)[0]

  # تصنيف النتيجة لعرضها بشكل جميل
  categories_names = {
      0: "💵 هاتف اقتصادي (رخيص)",
      1: "📦 هاتف متوسط الفئة",
      2: "💎 هاتف رائد (غالي وذو أداء عالي)",
  }

  result_text = categories_names.get(prediction, "غير معروف")

  # إظهار النتيجة للمستخدم بتصميم مميز
  st.success(f"النتيجة المتوقعة من الذكاء الاصطناعي: **{result_text}**")