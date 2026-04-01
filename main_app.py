import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Online Education Portal",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ------------------------------------------------------------
# Custom CSS
# ------------------------------------------------------------
CUSTOM_CSS = """
<style>
    .main {
        background: linear-gradient(180deg, #f8fbff 0%, #eef4ff 100%);
    }
    .hero {
        padding: 1.6rem 1.8rem;
        border-radius: 20px;
        background: linear-gradient(135deg, #153e75 0%, #1e5aa8 55%, #3a7bd5 100%);
        color: white;
        box-shadow: 0 8px 24px rgba(21, 62, 117, 0.18);
        margin-bottom: 1rem;
    }
    .hero h1 {
        font-size: 2rem;
        margin-bottom: 0.4rem;
    }
    .hero p {
        font-size: 1rem;
        opacity: 0.95;
        margin-bottom: 0;
    }
    .section-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #153e75;
        margin-top: 0.6rem;
        margin-bottom: 0.6rem;
    }
    .card {
        background: white;
        padding: 1rem 1rem;
        border-radius: 18px;
        border: 1px solid #e4ecf7;
        box-shadow: 0 6px 18px rgba(15, 23, 42, 0.05);
        min-height: 140px;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 18px;
        border: 1px solid #e4ecf7;
        box-shadow: 0 6px 18px rgba(15, 23, 42, 0.05);
        text-align: center;
    }
    .tag {
        display: inline-block;
        padding: 0.25rem 0.6rem;
        background: #e7f0ff;
        color: #174ea6;
        border-radius: 999px;
        font-size: 0.82rem;
        margin-right: 0.35rem;
        margin-bottom: 0.35rem;
    }
    .subtle {
        color: #5b6472;
        font-size: 0.94rem;
    }
    .result-box {
        background: #f8fbff;
        border-left: 5px solid #3a7bd5;
        border-radius: 12px;
        padding: 1rem;
        margin-top: 0.7rem;
        border-top: 1px solid #e4ecf7;
        border-right: 1px solid #e4ecf7;
        border-bottom: 1px solid #e4ecf7;
    }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ------------------------------------------------------------
# Mock data
# ------------------------------------------------------------
COURSES = [
    "Introduction to Data Science",
    "AI in Education",
    "Digital Pedagogy",
    "Learning Analytics",
    "Computer Networks",
]

ENROLLED_COURSES = [
    {
        "title": "AI in Education",
        "approach": "Hybrid",
        "next_session": "Wednesday 10:00 AM",
        "progress": 72,
    },
    {
        "title": "Digital Pedagogy",
        "approach": "Asynchronous",
        "next_session": "New content released Friday",
        "progress": 45,
    },
    {
        "title": "Computer Networks",
        "approach": "Synchronous",
        "next_session": "Thursday 2:00 PM",
        "progress": 81,
    },
]

# ------------------------------------------------------------
# Helpers
# ------------------------------------------------------------
def hero_section():
    st.markdown(
        """
        <div class="hero">
            <h1>Online Education Portal</h1>
            <p>
                AI-assisted platform for structured online teaching, assessment design,
                learner access, and academic analytics.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_tags(tags):
    html = "".join([f'<span class="tag">{tag}</span>' for tag in tags])
    st.markdown(html, unsafe_allow_html=True)


def fake_ai_lesson_plan(session_type, course, topic, modality):
    return f"""
**AI-Generated Lesson Plan**

- **Course:** {course}
- **Session Type:** {session_type}
- **Modality:** {modality}
- **Topic:** {topic}
- **Estimated Duration:** 75 minutes

**Structure**
1. Learning objectives aligned with uploaded material
2. Introductory hook and activation of prior knowledge
3. Core concepts sequencing
4. Interaction checkpoints or self-paced activities
5. Guided practice / project / follow-up activity
6. Reflection and outcome validation

**AI Suggestions**
- Add formative checkpoints every 10–15 minutes
- Include one applied example from the uploaded content
- End with a recap and a short reflection task
"""


def fake_ai_assessment(assessment_type, course, difficulty):
    return f"""
**AI-Generated Assessment Blueprint**

- **Course:** {course}
- **Assessment Type:** {assessment_type}
- **Difficulty Level:** {difficulty}

**Recommended Structure**
- 5 multiple-choice questions
- 3 short-answer questions
- 1 scenario-based application task
- 1 rubric-guided reflective question

**Quality Controls**
- Coverage across key learning outcomes
- Balanced cognitive levels
- Clear instructions and scoring criteria
- Suggested time estimate included
"""


def app_home():
    hero_section()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div class="card">
                <div class="section-title">Teacher Workspace</div>
                <div class="subtle">Create AI-supported lesson plans, sessions, and assessments.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class="card">
                <div class="section-title">Student Workspace</div>
                <div class="subtle">View enrolled courses, attend sessions, and access learning materials.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            """
            <div class="card">
                <div class="section-title">Admin Workspace</div>
                <div class="subtle">Track engagement, logins, duration, and delivery analytics.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("<div class='section-title'>Core Functional Design</div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)

    with c1:
        st.markdown("""
        <div class="card">
            <b>Teacher flows</b><br><br>
            • Create Content<br>
            • Synchronous sessions<br>
            • Asynchronous sessions<br>
            • Hybrid sessions<br>
            • Create Assessment<br>
            • AI-generated instructional outputs
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="card">
            <b>Platform outcomes</b><br><br>
            • Better online delivery structure<br>
            • Standardized learning experiences<br>
            • Faster course preparation<br>
            • More engaging student pathways<br>
            • Institutional analytics dashboard
        </div>
        """, unsafe_allow_html=True)


def teacher_dashboard():
    st.markdown("<div class='section-title'>Teacher Dashboard</div>", unsafe_allow_html=True)

    tabs = st.tabs(["Create Content", "Create Assessment", "My Content Library"])

    # --------------------------------------------------------
    # Create Content
    # --------------------------------------------------------
    with tabs[0]:
        left, right = st.columns([1.1, 1.2])

        with left:
            course = st.selectbox("Select course", COURSES)
            category = st.selectbox(
                "Content category",
                ["Synchronous Session", "Asynchronous Session", "Hybrid Session"],
            )

            if category == "Synchronous Session":
                subtype = st.radio(
                    "Choose session type",
                    ["Lecture-based (large cohorts)", "Interactive session (small cohorts)"],
                )
            elif category == "Asynchronous Session":
                subtype = st.radio(
                    "Choose asynchronous option",
                    [
                        "New asynchronous session",
                        "Follow-up session linked to a synchronous session",
                        "Guided project",
                        "Assessment preparation session",
                    ],
                )
            else:
                subtype = st.radio(
                    "Choose hybrid design",
                    [
                        "Lecture + follow-up activities",
                        "Interactive live session + guided project",
                        "Assessment prep + live debrief",
                    ],
                )

            topic = st.text_input("Session topic", placeholder="e.g., Introduction to supervised learning")
            uploaded = st.file_uploader(
                "Upload course material",
                type=["pdf", "docx", "pptx", "txt"],
                help="This MVP uses uploaded material as a placeholder input for the AI pipeline.",
            )

            generate_plan = st.button("Generate AI lesson plan", type="primary")

        with right:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("**Selected design characteristics**")
            render_tags([
                category,
                subtype,
                "AI-assisted planning",
                "Structured online delivery",
            ])
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(
                "This module helps instructors transform uploaded material into a structured lesson plan adapted to the chosen teaching approach.")
            st.markdown("</div>", unsafe_allow_html=True)

            if generate_plan:
                if not topic:
                    st.warning("Please add a topic before generating the lesson plan.")
                else:
                    result = fake_ai_lesson_plan(category, course, topic, subtype)
                    st.markdown(f"<div class='result-box'>{result}</div>", unsafe_allow_html=True)
                    if uploaded:
                        st.success(f"Source material received: {uploaded.name}")
                    else:
                        st.info("No file uploaded yet. The current result is based on the selected options only.")

    # --------------------------------------------------------
    # Create Assessment
    # --------------------------------------------------------
    with tabs[1]:
        a1, a2 = st.columns([1.1, 1.2])

        with a1:
            course_a = st.selectbox("Course for assessment", COURSES, key="assessment_course")
            assessment_type = st.radio(
                "Assessment type",
                ["Low-stakes assessment", "High-stakes assessment"],
            )
            difficulty = st.select_slider(
                "Difficulty level",
                options=["Easy", "Moderate", "Challenging", "Advanced"],
                value="Moderate",
            )
            uploaded_assessment = st.file_uploader(
                "Upload source content for assessment generation",
                type=["pdf", "docx", "pptx", "txt"],
                key="assessment_upload",
            )
            generate_assessment = st.button("Generate AI assessment", type="primary")

        with a2:
            st.markdown("<div class='card'>", unsafe_allow_html=True)
            st.markdown("**Assessment engine**")
            render_tags([
                assessment_type,
                difficulty,
                "Outcome-aligned",
                "AI-generated items",
            ])
            st.markdown("<br>", unsafe_allow_html=True)
            st.markdown(
                "The assessment module creates evaluation blueprints based on uploaded teaching material and the stakes of the assessment."
            )
            st.markdown("</div>", unsafe_allow_html=True)

            if generate_assessment:
                result = fake_ai_assessment(assessment_type, course_a, difficulty)
                st.markdown(f"<div class='result-box'>{result}</div>", unsafe_allow_html=True)
                if uploaded_assessment:
                    st.success(f"Assessment source content received: {uploaded_assessment.name}")
                else:
                    st.info("No file uploaded yet. The current blueprint is generated from the selected options.")

    # --------------------------------------------------------
    # Library
    # --------------------------------------------------------
    with tabs[2]:
        st.markdown("<div class='section-title'>Saved instructional assets</div>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("""
            <div class="card">
                <b>AI in Education</b><br>
                Synchronous lesson plan<br><br>
                <span class="subtle">Generated on 2026-03-31</span>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div class="card">
                <b>Digital Pedagogy</b><br>
                Guided project structure<br><br>
                <span class="subtle">Generated on 2026-03-30</span>
            </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div class="card">
                <b>Learning Analytics</b><br>
                High-stakes assessment draft<br><br>
                <span class="subtle">Generated on 2026-03-29</span>
            </div>
            """, unsafe_allow_html=True)


def student_dashboard():
    st.markdown("<div class='section-title'>Student Dashboard</div>", unsafe_allow_html=True)

    left, right = st.columns([1.2, 0.8])

    with left:
        for item in ENROLLED_COURSES:
            st.markdown(
                f"""
                <div class="card" style="margin-bottom: 0.8rem;">
                    <div style="font-size: 1.05rem; font-weight: 700; color: #153e75;">{item['title']}</div>
                    <div class="subtle">Teaching approach: {item['approach']}</div>
                    <div class="subtle">Next activity: {item['next_session']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.progress(item["progress"] / 100.0, text=f"Progress: {item['progress']}%")
            st.write("")

    with right:
        st.markdown("""
        <div class="card">
            <b>Student actions</b><br><br>
            • Join synchronous session<br>
            • Access asynchronous content<br>
            • Open hybrid session pathway<br>
            • Download learning materials<br>
            • Complete assessments
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        selected_course = st.selectbox("Quick access to course", [x["title"] for x in ENROLLED_COURSES])
        action = st.radio(
            "Choose action",
            ["Open materials", "Attend live session", "View assessment tasks"],
        )
        if st.button("Launch"):
            st.success(f"{action} for '{selected_course}' launched successfully.")


def admin_dashboard():
    st.markdown("<div class='section-title'>Admin Analytics Dashboard</div>", unsafe_allow_html=True)

    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown("<div class='metric-card'><h3>1,248</h3><div class='subtle'>Total logins this week</div></div>", unsafe_allow_html=True)
    with m2:
        st.markdown("<div class='metric-card'><h3>86%</h3><div class='subtle'>Student engagement rate</div></div>", unsafe_allow_html=True)
    with m3:
        st.markdown("<div class='metric-card'><h3>73 min</h3><div class='subtle'>Average session duration</div></div>", unsafe_allow_html=True)
    with m4:
        st.markdown("<div class='metric-card'><h3>92%</h3><div class='subtle'>Attendance completion</div></div>", unsafe_allow_html=True)

    st.write("")
    left, right = st.columns(2)

    with left:
        st.markdown("""
        <div class="card">
            <b>Trackable analytics</b><br><br>
            • Session duration<br>
            • Student login frequency<br>
            • Live attendance rate<br>
            • Course engagement levels<br>
            • Completion per learning approach<br>
            • Assessment submission patterns
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown("""
        <div class="card">
            <b>Institutional insight value</b><br><br>
            • Identify low-engagement cohorts<br>
            • Compare synchronous vs asynchronous outcomes<br>
            • Improve instructor support needs<br>
            • Standardize delivery quality across programs
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='section-title'>Activity Monitor</div>", unsafe_allow_html=True)
    st.dataframe(
        {
            "Course": ["AI in Education", "Digital Pedagogy", "Computer Networks", "Learning Analytics"],
            "Logins": [315, 274, 401, 258],
            "Avg Session Duration (min)": [68, 74, 81, 62],
            "Engagement Level": ["High", "Moderate", "High", "Moderate"],
            "Completion Rate": [88, 71, 91, 76],
        },
        use_container_width=True,
    )


def platform_architecture():
    st.markdown("<div class='section-title'>Suggested Streamlit Architecture</div>", unsafe_allow_html=True)

#     st.code(
#         """
# project/
# │── app.py
# │── components/
# │   ├── teacher.py
# │   ├── student.py
# │   ├── admin.py
# │   └── ui_helpers.py
# │── services/
# │   ├── ai_generation.py
# │   ├── analytics.py
# │   └── auth.py
# │── assets/
# │   └── style.css
# │── data/
# │   └── demo_data.json
# │── requirements.txt
#         """.strip(),
#         language="bash",
#     )

#      st.markdown("""
#  **Recommended backend evolution**
#  - **Frontend:** Streamlit
#  - **Authentication:** Streamlit auth or external identity provider
#  - **Database:** PostgreSQL / Supabase / Firebase
#  - **File storage:** S3 or equivalent
#  - **AI engine:** OpenAI / Azure OpenAI / local LLM workflow
#  - **Analytics pipeline:** event logging + dashboard aggregation
#  """)


# ------------------------------------------------------------
# Sidebar navigation
# ------------------------------------------------------------
with st.sidebar:
    st.title("Portal Navigation")
    role = st.radio("Select profile", ["Home", "Teacher", "Student", "Admin", "Architecture"])
    st.divider()
    # st.caption("Design prototype in Streamlit")
    st.caption(f"Date: {datetime.now().strftime('%Y-%m-%d')}")

# ------------------------------------------------------------
# App routing
# ------------------------------------------------------------
if role == "Home":
    app_home()
elif role == "Teacher":
    teacher_dashboard()
elif role == "Student":
    student_dashboard()
elif role == "Admin":
    admin_dashboard()
else:
    platform_architecture()
