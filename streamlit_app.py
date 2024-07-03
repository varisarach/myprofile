import streamlit as st

# Set the title of the Streamlit app
st.title("History of Borcelle")

# CSS for styling the timeline
st.markdown("""
    <style>
        .timeline {
            position: relative;
            max-width: 800px;
            margin: 0 auto;
        }
        .timeline::after {
            content: '';
            position: absolute;
            width: 6px;
            background-color: #ddd;
            top: 0;
            bottom: 0;
            left: 50%;
            margin-left: -3px;
        }
        .container {
            padding: 10px 40px;
            position: relative;
            background-color: inherit;
            width: 50%;
        }
        .container.left {
            left: 0;
        }
        .container.right {
            left: 50%;
        }
        .container::after {
            content: '';
            position: absolute;
            width: 10px;
            height: 10px;
            background-color: solid black;
            border: 10px solid;
            top: 15px;
            border-radius: 50%;
        }
        .left::after {
            border-color: solid black;
            left: 100%;
            transform: translateX(-50%);
        }
        .right::after {
            border-color: solid black;
            right: 100%;
            transform: translateX(50%);
        }
        .content {
            padding: 20px 30px;
            background-color: white;
            position: relative;
            border-radius: 6px;
            border-left: 3px solid;
        }
        .left .content {
            margin-left: 20px;
        }
        .right .content {
            margin-right: 20px;
        }
        .year {
            font-size: 18px;
            font-weight: bold;
        }
        .event {
            font-size: 16px;
            font-weight: bold;
            color: #333;
        }
        .description {
            font-size: 14px;
            color: #777;
        }
        .vertical {
            position: absolute;
            border-left: 5px solid black;
            height: 200px;
            left: 50%;
            transform: translateX(-50%);
        }
    </style>
""", unsafe_allow_html=True)

# Timeline data
timeline_data = [
    {"year": "1998", "event": "Born", "description": "A little girl named Mind was born.", "color": "orange"},
    {"year": "2004", "event": "Panaya Phatthanakan Bilingual School", "description": "Kindergarten.", "color": "pink"},
    {"year": "2007", "event": "Panaya Phatthanakan Bilingual School", "description": "Primary school ไระ้ English Program (EP).", "color": "purple"},
    {"year": "2013", "event": "Nawaminthrachinuthit Triamudomsuksanomklao School", "description": "High School Diploma, Science-Math.", "color": "green"},
    {"year": "2018", "event": "King Mongkut's Institute of Technology Ladkrabang", "description": "Development and launch of a new innovative product for business management.", "color": "yellow"}
]

# Display timeline in a similar format to the image
st.markdown('<div class="timeline">', unsafe_allow_html=True)
for i, entry in enumerate(timeline_data):
    side = "left" if i % 2 == 0 else "right"
    st.markdown(f"""
        <div class= "vertical"></div>
        <div class="container {side}"
            <div class="content" style="border-color:{entry['color']};">
                <div class="year" style="color:{entry['color']};">{entry['year']}</div>
                <div class="event">{entry['event']}</div>
                <div class="description">{entry['description']}</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
