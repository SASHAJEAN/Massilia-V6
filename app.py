import streamlit as st
import random

st.set_page_config(
    page_title="Massilia",
    page_icon="🌞",
    layout="wide",
)

# -------------------------
# STYLE
# -------------------------

st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Arial', sans-serif;
}

.main {
    background: linear-gradient(180deg, #FFF7E8 0%, #FFE0B2 100%);
}

.hero {
    padding: 2rem;
    border-radius: 30px;
    background: linear-gradient(135deg, #FFB703 0%, #FB8500 50%, #219EBC 100%);
    color: white;
    text-align: center;
    margin-bottom: 2rem;
}

.card {
    background: white;
    padding: 1.3rem;
    border-radius: 22px;
    box-shadow: 0 4px 18px rgba(0,0,0,0.08);
    margin-bottom: 1rem;
}

.small-card {
    background: #fffaf2;
    padding: 1rem;
    border-radius: 18px;
    border: 1px solid #f4d7a1;
    margin-bottom: 1rem;
}

.tag {
    display: inline-block;
    background: #FFE4A3;
    padding: 0.3rem 0.8rem;
    border-radius: 999px;
    margin-right: 0.3rem;
    margin-bottom: 0.3rem;
    color: #5f4300;
    font-size: 0.85rem;
}

.phone {
    background: #111;
    border-radius: 35px;
    padding: 18px;
    max-width: 330px;
    margin: auto;
}

.phone-screen {
    background: white;
    border-radius: 25px;
    padding: 1rem;
    min-height: 580px;
}

.big-title {
    font-size: 3rem;
    font-weight: bold;
}

.gradient-text {
    background: linear-gradient(90deg, #FB8500, #219EBC);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: bold;
}

.metric {
    background: white;
    border-radius: 20px;
    padding: 1rem;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# -------------------------
# DATA
# -------------------------

spots = [
    {
        "name": "Chez Jeannot",
        "type": "Beach Restaurant",
        "mood": ["chill", "romantic"],
        "music": ["acoustic", "lounge"],
        "budget": 3,
        "vibe": "Sunset pizza & apéro facing the sea",
        "price": "€€",
    },
    {
        "name": "La Caravelle",
        "type": "Pastis Bar",
        "mood": ["local", "authentic"],
        "music": ["jazz", "live"],
        "budget": 2,
        "vibe": "Historic Marseille apéro atmosphere",
        "price": "€€",
    },
    {
        "name": "Le Rooftop",
        "type": "Sunset Bar",
        "mood": ["party", "trendy"],
        "music": ["electro", "house"],
        "budget": 4,
        "vibe": "Golden hour with DJ sets",
        "price": "€€€",
    },
    {
        "name": "Chez Magali",
        "type": "Panisse Spot",
        "mood": ["cheap", "student"],
        "music": ["none"],
        "budget": 1,
        "vibe": "Authentic panisse for locals",
        "price": "€",
    },
    {
        "name": "Tuba Club",
        "type": "Hidden Gem",
        "mood": ["luxury", "date"],
        "music": ["deep house"],
        "budget": 5,
        "vibe": "Mediterranean chic experience",
        "price": "€€€€",
    },
]

personas = [
    {
        "name": "Camille",
        "age": 24,
        "description": "Student who loves cheap apéros and sunset spots."
    },
    {
        "name": "Lucas",
        "age": 31,
        "description": "Parisian tourist looking for authentic Marseille experiences."
    },
    {
        "name": "Sofia",
        "age": 27,
        "description": "Content creator searching trendy hidden gems."
    },
]

competitors = [
    ["Beli", "Food recommendations", "No Marseille niche positioning"],
    ["Tripadvisor", "Tourist reviews", "Too generic and not lifestyle-focused"],
    ["Instagram", "Visual discovery", "No AI recommendations"],
    ["Google Maps", "Location search", "No mood-based discovery"],
]

# -------------------------
# SESSION STATE
# -------------------------

if "saved_places" not in st.session_state:
    st.session_state.saved_places = []

if "posts" not in st.session_state:
    st.session_state.posts = []

# -------------------------
# HERO
# -------------------------

st.markdown("""
<div class="hero">
    <div class="big-title">🌞 MASSILIA</div>
    <h3>Pas fâché avec le plaisir</h3>
    <p>
    AI-powered lifestyle & food discovery app inspired by Marseille culture.
    </p>
</div>
""", unsafe_allow_html=True)

# -------------------------
# NAVIGATION
# -------------------------

page = st.sidebar.radio(
    "Navigation",
    [
        "Startup Concept",
        "AI Recommender",
        "Community Feed",
        "Pitch Deck",
        "UX/UI Prototype",
        "Business Model",
        "Market Analysis",
        "App Architecture",
    ]
)

# -------------------------
# STARTUP CONCEPT
# -------------------------

if page == "Startup Concept":

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="metric">
        <h2>🎯 Target</h2>
        <p>20–35 years old</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric">
        <h2>📍 Location</h2>
        <p>Marseille & South of France</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric">
        <h2>🤖 AI Value</h2>
        <p>Mood-based recommendations</p>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("🌊 Brand Positioning")

    tags = [
        "Mediterranean",
        "Sunny",
        "Authentic",
        "Gen Z",
        "Social",
        "Lifestyle",
        "Community",
        "Food Discovery",
        "Apéro Culture",
    ]

    tag_html = "".join([f"<span class='tag'>{tag}</span>" for tag in tags])

    st.markdown(f"""
    <div class="card">
        {tag_html}
    </div>
    """, unsafe_allow_html=True)

    st.subheader("👥 User Personas")

    for p in personas:
        st.markdown(f"""
        <div class="small-card">
            <h4>{p['name']} • {p['age']} years old</h4>
            <p>{p['description']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("💡 Core Concept")

    st.markdown("""
    <div class="card">
    <h4>Massilia is an AI-powered Marseille lifestyle platform.</h4>

    <p>
    The app recommends the perfect food, sunset, apéro or nightlife experience
    depending on the user's mood, budget, music taste and social vibe.
    </p>

    <ul>
    <li>AI recommendations</li>
    <li>Community reviews & photos</li>
    <li>Gamification & badges</li>
    <li>Local hidden gems</li>
    <li>Personalized itineraries</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# AI RECOMMENDER
# -------------------------

elif page == "AI Recommender":

    st.subheader("🤖 AI Marseille Concierge")

    col1, col2 = st.columns(2)

    with col1:
        mood = st.selectbox(
            "Mood",
            ["chill", "party", "romantic", "local", "student", "luxury"]
        )

        music = st.selectbox(
            "Music vibe",
            ["electro", "house", "jazz", "live", "acoustic", "lounge"]
        )

    with col2:
        budget = st.slider("Budget level", 1, 5, 2)

        group = st.selectbox(
            "Group type",
            ["friends", "date", "solo", "family"]
        )

    if st.button("✨ Generate Marseille Experience"):

        recommendations = []

        for spot in spots:
            score = 0

            if mood in spot["mood"]:
                score += 2

            if music in spot["music"]:
                score += 2

            if abs(spot["budget"] - budget) <= 1:
                score += 1

            recommendations.append((score, spot))

        recommendations.sort(reverse=True, key=lambda x: x[0])

        st.success("Perfect Marseille spots found 🍋")

        for score, spot in recommendations[:3]:
            st.markdown(f"""
            <div class="card">
                <h3>{spot['name']}</h3>
                <p><b>{spot['type']}</b></p>
                <p>{spot['vibe']}</p>
                <p>Price: {spot['price']}</p>
            </div>
            """, unsafe_allow_html=True)

            if st.button(f"Save {spot['name']}"):
                st.session_state.saved_places.append(spot["name"])

    if st.session_state.saved_places:
        st.subheader("❤️ Saved Places")
        st.write(st.session_state.saved_places)

# -------------------------
# COMMUNITY
# -------------------------

elif page == "Community Feed":

    st.subheader("📸 Community Feed")

    with st.form("post_form"):
        username = st.text_input("Your name")
        experience = st.text_area("Share your Marseille experience")
        rating = st.slider("Ambiance rating", 1, 5, 4)

        submitted = st.form_submit_button("Post Experience")

        if submitted:
            st.session_state.posts.append({
                "username": username,
                "experience": experience,
                "rating": rating,
            })

    if not st.session_state.posts:
        st.info("No posts yet. Be the first to share an apéro 🌞")

    for post in reversed(st.session_state.posts):

        stars = "⭐" * post["rating"]

        st.markdown(f"""
        <div class="card">
            <h4>{post['username']}</h4>
            <p>{post['experience']}</p>
            <p>{stars}</p>
        </div>
        """, unsafe_allow_html=True)

# -------------------------
# PITCH DECK
# -------------------------

elif page == "Pitch Deck":

    st.subheader("📈 Investor Pitch Deck")

    slides = [
        "Problem",
        "Solution",
        "Market Opportunity",
        "Product Demo",
        "AI Value Proposition",
        "Business Model",
        "Go-To-Market Strategy",
        "Competitive Advantage",
        "Financial Projections",
        "Vision",
    ]

    for i, slide in enumerate(slides, start=1):
        st.markdown(f"""
        <div class="small-card">
            <h4>{i}. {slide}</h4>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("🚀 Vision")

    st.markdown("""
    <div class="card">
    Become the leading AI-powered Mediterranean lifestyle platform,
    starting with Marseille and expanding to Nice, Barcelona, Naples and Mykonos.
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# UX/UI
# -------------------------

elif page == "UX/UI Prototype":

    st.subheader("📱 Mobile App Prototype")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="phone">
            <div class="phone-screen">
                <h2>🌞 Massilia</h2>
                <p>Good evening Sasha 👋</p>

                <div class="small-card">
                    <h4>🍹 Sunset Apéro</h4>
                    <p>Electro vibes near the beach</p>
                </div>

                <div class="small-card">
                    <h4>🫓 Best Panisse</h4>
                    <p>Authentic local experience</p>
                </div>

                <div class="small-card">
                    <h4>🎶 Rooftop Tonight</h4>
                    <p>DJ set • Marseille center</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="phone">
            <div class="phone-screen">
                <h3>✨ Onboarding</h3>

                <p>Select your vibe:</p>

                <span class='tag'>Beach</span>
                <span class='tag'>Electro</span>
                <span class='tag'>Cheap Eats</span>
                <span class='tag'>Sunset</span>
                <span class='tag'>Pastis</span>

                <hr>

                <p>Budget Preference</p>

                <div class='small-card'>
                    € • €€ • €€€
                </div>

                <p>Music Preferences</p>

                <div class='small-card'>
                    House • Jazz • Live Music
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# -------------------------
# BUSINESS MODEL
# -------------------------

elif page == "Business Model":

    st.subheader("💰 Business Model")

    revenue_streams = [
        "Premium subscriptions",
        "Sponsored restaurants & bars",
        "Affiliate reservations",
        "Local tourism partnerships",
        "Event collaborations",
        "Brand partnerships",
    ]

    for r in revenue_streams:
        st.markdown(f"""
        <div class="small-card">
            💸 {r}
        </div>
        """, unsafe_allow_html=True)

    st.subheader("🧠 AI Value Proposition")

    st.markdown("""
    <div class="card">
    Unlike Tripadvisor or Google Maps, Massilia creates emotional,
    personalized and mood-based recommendations using AI.
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# MARKET ANALYSIS
# -------------------------

elif page == "Market Analysis":

    st.subheader("📊 Market Opportunity")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Tourists in Marseille", "5M+")

    with col2:
        st.metric("Target Age", "20–35")

    with col3:
        st.metric("Food Discovery Trend", "High Growth")

    st.subheader("⚔️ Competitor Analysis")

    st.table({
        "Competitor": [c[0] for c in competitors],
        "Strength": [c[1] for c in competitors],
        "Weakness": [c[2] for c in competitors],
    })

    st.subheader("🎯 Market Gap")

    st.markdown("""
    <div class="card">
    There is currently no Marseille-focused AI lifestyle platform combining:
    food discovery, local culture, social recommendations and mood-based AI.
    </div>
    """, unsafe_allow_html=True)

# -------------------------
# ARCHITECTURE
# -------------------------

elif page == "App Architecture":

    st.subheader("🛠️ Suggested Tech Architecture")

    st.code("""
Frontend:
- React Native / Next.js
- Mobile-first UI
- Dark/Light mode

Backend:
- Firebase or Supabase
- User authentication
- Realtime community feed

AI Layer:
- Mood recommendation engine
- Personalized itineraries
- Smart tagging system

Database:
- Users
- Restaurants
- Reviews
- Saved places
- Events
- Photos
""")

    st.subheader("🗄️ Suggested Database Structure")

    database = {
        "Table": [
            "users",
            "places",
            "reviews",
            "posts",
            "saved_places",
            "events"
        ],
        "Purpose": [
            "User profiles",
            "Restaurant/bar data",
            "Ratings & comments",
            "Community content",
            "Favorites",
            "Local events"
        ]
    }

    st.table(database)

    st.subheader("📱 MVP Features")

    features = [
        "AI recommendations",
        "Community feed",
        "Saved places",
        "Mood filters",
        "Interactive map",
        "Onboarding personalization",
        "Photo sharing",
    ]

    for f in features:
        st.markdown(f"""
        <div class="small-card">
        ✅ {f}
        </div>
        """, unsafe_allow_html=True)
