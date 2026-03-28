import streamlit as st
import os


st.set_page_config(
    page_title="Mithrakayal M Portfolio",
    layout="wide"
)


with st.sidebar:
    st.title("Mithrakayal M")
    st.write("🚀 Python Developer | Aspiring Data Scientist | ML Engineer")
    st.markdown("""
**Contact**

📧 mithrakayal137@gmail.com  
📱 7598371986  
[LinkedIn](https://linkedin.com/in/mithrakayal-mani-b56b7a377)  
[GitHub](https://github.com/MITHRAKAYAL137)
""")


# NAVIGATION
page = st.sidebar.radio(
    "Navigation",
    ["About", "Experience", "Skills", "Projects", "Achievements", "Resume"]
)


# HEADER
st.markdown("<h1 style='text-align:center;'>🚀 Mithrakayal M Portfolio</h1>", unsafe_allow_html=True)
st.divider()


# ABOUT
if page == "About":
    st.subheader("About Me")
    st.write("""
Python Developer with 2+ years of experience building real-time data processing systems, automation tools, and computer vision applications.
Skilled in Python, OpenCV, NumPy, SQL, and API integration. Experienced in dashboard validation, data extraction, and system optimization for EV and healthcare domains.
""")
    
    st.divider()
    
    # Metrics
    col1, col2, col3 = st.columns(3)
    col1.metric("Experience", "3 Years")
    col2.metric("Projects", "5+")
    col3.metric("Technologies", "10+")


# EXPERIENCE
elif page == "Experience":
    st.subheader("💼 Professional Experience")
    st.markdown("**Python Developer – Infiniti Automation, Coimbatore**  | June 2023 – Present")

    st.markdown("**EV Dashboard Validation & Data Extraction System**")
    st.markdown("*Version 1 – ML-Based Region Detection*")
    st.write("""
- Developed a ML-based computer vision system to detect critical regions on EV dashboards  
- Built automated pipelines for data extraction and validation  
- Enabled real-time monitoring by sending processed data to backend systems
""")
    st.markdown("*Version 2 – Numerical Processing & Image Verification*")
    st.write("""
- Implemented seven-segment digit recognition using NumPy  
- Extracted accurate numerical values from dashboard images  
- Integrated system to send images and extracted data to server  
- Improved reliability via dual validation (visual + numerical)
""")
    st.markdown("**Medical Device Monitoring & UI System (Confidential)**")
    st.write("""
- Developed lightweight GUI with real-time data handling  
- Enabled dynamic monitoring and recording functionality  
- Integrated network connectivity for backend communication  
- Optimized performance and reliability through efficient backend design
""")


# SKILLS (Category Cards)
elif page == "Skills":
    st.subheader("🛠 Skills by Category")
    skill_categories = {
        "💻 Programming": ["Python", "SQL"],
        "🤖 Machine Learning": ["Supervised / Unsupervised Learning", "Time Series Forecasting", "ARIMA"],
        "📷 Computer Vision": ["OpenCV", "Image Processing", "Region Detection"],
        "📊 Data Tools": ["Pandas", "NumPy", "Feature Engineering", "Data Cleaning"],
        "📈 Visualization": ["Matplotlib", "Seaborn", "Streamlit Dashboards"],
        "⚙️ Systems & Concepts": ["Real-Time Data Processing", "API Integration", "Backend Systems"]
    }
    colors = ["#FFCDD2", "#C8E6C9", "#BBDEFB", "#FFF9C4", "#D1C4E9", "#FFE0B2"]

    cols = st.columns(2)
    i = 0
    for category, skills in skill_categories.items():
        color = colors[i % len(colors)]
        with cols[i % 2]:
            st.markdown(
                f"""
                <div style='
                    border:2px solid {color}; 
                    border-radius:15px; 
                    padding:20px; 
                    margin-bottom:15px; 
                    background-color:{color}33;'>
                    <h3 style='color:{color}'>{category}</h3>
                    <ul>
                    {''.join([f"<li>{skill}</li>" for skill in skills])}
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )
        i += 1


# PROJECTS
elif page == "Projects":

    st.title("🚀 Featured Projects")

    projects = [
        {
            "name": "🚦 AI Smart Traffic Monitoring System",
            "desc": """
• Real-time vehicle detection using YOLOv8  
• Tracks traffic density and congestion  
• Streamlit dashboard visualization
""",
            "tech": "Python, OpenCV, YOLOv8, Streamlit",
            "github": "https://github.com/MITHRAKAYAL137/AI-Smart-Traffic-Monitoring-System",
            "live": None,
            "video": "traffic_ai.mp4"  # Video demo file
        },
        {
            "name": "🌆 Urban Traffic Intelligence System",
            "desc": """
• Smart city traffic analytics platform  
• Heatmaps & map visualization  
• ARIMA-based prediction
""",
            "tech": "Python, Streamlit, Plotly, ARIMA",
            "github": "https://github.com/MITHRAKAYAL137/Urban-Traffic-Intelligence-System",
            "live": "https://urban-traffic-intelligence-system-necezdkgerkcw4mezsp8ym.streamlit.app/",
            "video": None
        },
        {
            "name": "☀️ AI Solar Dryer Optimization System",
            "desc": """
• ML model for optimizing drying efficiency  
• Reduced energy consumption  
• Data-driven predictions
""",
            "tech": "Python, Machine Learning",
            "github": "https://github.com/MITHRAKAYAL137/AI-Solar-Dryer-Optimization-System",
            "live": "https://ai-driven-solar-dryer-optimization-system-afyybqvg24fp7savp6um.streamlit.app/",
            "video": None
        }
    ]

    for proj in projects:
        st.markdown(f"### {proj['name']}")
        st.write(proj["desc"])
        st.write(f"**Tech:** {proj['tech']}")

        col1, col2, col3 = st.columns(3)

        # GitHub link
        if proj.get("github"):
            col1.link_button("GitHub", proj["github"])

        # Live demo link
        if proj.get("live"):
            col2.link_button("Live Demo", proj["live"])

        # Video demo button (plays inline when clicked)
        video_file = proj.get("video")
        if video_file and os.path.exists(video_file):
            if col3.button("🎬 Video Demo", key=proj['name']):
                st.video(video_file)
        elif video_file:
            col3.warning(f"Video not found: {video_file}")

        st.divider()

# KEY ACHIEVEMENTS
elif page == "Achievements":
    st.subheader("🏆 Key Achievements")
    achievements = [
        "✔ Reduced system downtime by 25% by implementing predictive monitoring for EV dashboards.",
        "✔ Automated validation pipelines, minimizing manual errors by 80% in real-time data processing and device monitoring systems.",
        "✔ Developed a lightweight liquid glass UI for medical device monitoring, achieving high-performance, visually appealing dashboards comparable to heavier frameworks.",
        "✔ Built real-time data extraction and processing pipelines using Python and OpenCV for EV dashboards, improving data reliability and system efficiency."
    ]
    for ach in achievements:
        st.markdown(
            f"""
            <div style='
                border:2px solid #4CAF50; 
                border-radius:15px; 
                padding:15px; 
                margin-bottom:10px; 
                background-color:#E8F5E9'>
                <p style='font-size:16px; color:#2E7D32'>{ach}</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# RESUME
elif page == "Resume":
    st.subheader("📄 Resume")
    file_path = os.path.join(os.getcwd(), "MITHRAKAYAL_M_Resume.pdf")
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            st.download_button(
                "Download Resume",
                f,
                file_name="MITHRAKAYAL_M_Resume.pdf"
            )
    else:
        st.error("❌ Resume file not found")
        st.write("📂 Available files:", os.listdir())


# FOOTER
st.divider()
st.markdown("<p style='text-align:center;'>© 2026 Mithrakayal M</p>", unsafe_allow_html=True)

