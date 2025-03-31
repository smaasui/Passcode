# **Checking Strength of Password**
# Check for basic requirement ie Uppercase, Lowercase, Numeric and Special characters
# State Password Strength ie Weak, Moderate, Strong
# Estimates crack time using brute-force calculations
# Give Suggestion of unfullfilled requirements in basic requirements
# Suggests a strong password if needed
# State Security Tips


import streamlit as st
import re
import time

# Page Configuration
st.set_page_config(
    page_title="Password Sentinel", 
    page_icon="🔐", 
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get help": "https://www.google.com/search?q=help",
        "Report a bug": "https://github.com/streamlit/streamlit/issues",
        "About": """# SMAASU Corporation©️  
        https://g.co/kgs/VvQB8W9
        App Version 0.617"""}
    )

# Sidebar
st.sidebar.title("🔐 Password Sentinel")
tabs = st.sidebar.radio("", ["Strength Checker", "Recommendation Tips", "About App", "About Us", "About Me"])

if tabs == "Strength Checker":
    # function for checking each requirement
    def have_special_char(s):
        return bool(re.search(r'[^A-Za-z0-9 ]', s))

    def have_num(s):
        return bool(re.search(r'[0-9]', s))

    def have_upper(s):
        return any(char.isupper() for char in s)

    def have_lower(s):
        return any(letter.islower() for letter in s)

    def have_least(s):
        return len(s)>7

    def have_max(s):
        return len(s)<65

    def is_weak_password(password):
        # 🚨 List of Common Weak Passwords (Avoid using these!)
        weak_passwords = [
        # Common Numeric Patterns
        "12345678", "123456789", "1234567890", "987654321", "11223344", "65432100", "00000000", "22222222", "99999999", "12121212", "77777777", "11112222",
        
        # Common Words & Phrases
        "password", "password1", "password123", "letmein123", "welcome123", "trustno1", "football1", "monkey123", "sunshine12", "iloveyou1", "superman1", "batman123", "starwars12", "dragon123", "master123", "shadow123", "freedom12", "ninja1234", "hello1234", "qwerty123", "baseball12", "computer1", "whatever1", "access1234", "secret123", "login12345", "adminadmin",
        
        # Keyboard Patterns
        "qwertyui", "asdfghjk", "zxcvbnm1", "qazwsxed", "1q2w3e4r", "poiuytrew", "mnbvcxz1", "lkjhgfdsa", "qwertyuiop", "asdfghjkl1", "zxcvbnm123", "1qaz2wsx", "3edc4rfv", "5tgb6yhn", "7ujm8ik9",
        
        # Popular Names
        "jennifer1", "michael12", "charlie99", "andrew123", "stephanie1", "daniel123", "robert123", "jessica12", "jordan123", "hunter123", "thomas123", "george123", "harrypotter1",
        
        # Date-Based Passwords
        "20202020", "19901990", "20012002", "20102011", "12319999", "03121985", "07071996", "09092009", "01012020", "12251995", "06061999", "19971997", "19861986", "20032003",
        
        # Company & Tech
        "google123", "facebook1", "linkedin12", "netflix123", "adobe1234", "oracle12", "microsoft1", "samsung12", "apple1234", "amazon123", "tesla1234", "nvidia123",
        
        # Variations with Symbols & Capitalization
        "P@ssword1", "Password!", "Admin1234", "Welcome1!", "Qwerty123!", "1q2w3e4r5t!", "LetMeIn!", "TrustNo1!", "Superman12", "Hello123!", "Password@123", "Pa$$w0rd!", "Mypass@123",
        
        # Repetitive & Commonly Used
        "abcabcabc", "xyzxyzxyz", "testtest12", "passpass12", "default12", "changeme12", "guest1234", "system999", "administrator", "rootroot12", "database1", "backup1234", "secure1234",
        
        # Miscellaneous Common Weak Passwords
        "chocolate1", "pokemon123", "spiderman12", "batmanforever1", "liverpool1", "manutd123", "chelsea123", "arsenal12", "summer2024", "winter2023", "autumn2022", "spring2021", "corona2020", "pandemic2021", "covid1234", "vaccination1", "quarantine1"
    ]

        return password in weak_passwords
    
    col1, col2, col3 = st.columns([2.5,5,2.5])
    with col2:
    
        st.write("# 🔐 Password Strength Checker")
        passcode = st.text_input("Enter Password", type="password")
        
        placeholder = st.empty()    # Create an empty placeholder
        placeholder.warning("⚡ Strength Checking...")      # Show the message
        time.sleep(.5)       # Wait for half second
        placeholder.empty() # Clear the message
        # st.success("✅ Password strength checked!")     # Continue with password strength evaluation...

        # st.write("###  Strength Checking...")
        
        #Check password strength state
        if (have_special_char(passcode) + have_least(passcode) + have_max(passcode) + have_num(passcode) + have_upper(passcode) + have_lower(passcode)) > 5:
            st.info("### Un Crackable !")
        elif (have_special_char(passcode) + have_least(passcode) + have_max(passcode) + have_num(passcode) + have_upper(passcode) + have_lower(passcode)) > 4:
            st.success("### Strong !")
        elif (have_special_char(passcode) + have_least(passcode) + have_max(passcode) + have_num(passcode) + have_upper(passcode) + have_lower(passcode)) > 2:
            st.warning("### Mediocure !")
        elif len(passcode)==0:
            st.warning("### Enter Password !")
        else :
            st.error("### Hackable !")

        # Initialize progress bar
        progress_bar = st.progress(0)

        progress_bar.progress((have_special_char(passcode) + have_least(passcode) + have_num(passcode) + have_upper(passcode) + have_lower(passcode))/5)  

        # Example: Check all requirements
        if have_least(passcode):
            st.write("✔️ At least 8 characters")
        else:
            st.write("❌ Password should have at least 8 characters")

        if not(have_max(passcode)):
            st.write("❌ Password could be at most 64 characters")

        if have_special_char(passcode):
            st.write("✔️ At least one special character")
        else:
            st.write("❌ Password should have at least one special character")

        if have_num(passcode):
            st.write("✔️ At least one number")
        else:
            st.write("❌ Password should have at least one number")

        if have_upper(passcode):
            st.write("✔️ At least one Uppercase letter")
        else:
            st.write("❌ Password should have at least Uppercase letter")

        if have_lower(passcode):
            st.write("✔️ At least one Lowercase letter")
        else:
            st.write("❌ Password should have at least Lowercase letter")

        if is_weak_password(passcode):
            st.write("❌ Very Common Password !")

        if have_special_char(passcode) and have_least(passcode) and have_max(passcode) and have_num(passcode) and have_upper(passcode) and have_lower(passcode):
            st.info("### Great !")
        else:
            import string
            import random
            random_text = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) 
                                for _ in range(12))
            st.info(f"#### Suggested UnCrackable Password :  `{random_text}`")
            
elif tabs == "Recommendation Tips":
    st.markdown(
        """
        # 🔐 Password Sentinel 
        ## Your Ultimate Password Strength Analyzer""")

    # Display password tips
    st.markdown("""
    ### 🔒 **Tip for a Password**

    ⚠️ **Security Tip:** Avoid using common or easily guessable passwords (e.g., `password123`, `12345678`).  
    💡 **Best Practice:** Consider using a **passphrase** (e.g., `"Green$ky@2024"`) for added security.  
    🔒 **Your password is personal—never share it with anyone.**  
    📌 We recommend using a **password manager** to generate and store secure passwords safely.  

    """)
    # Display password requirements
    st.markdown("""
    ### 🔒 **Requirements for a Strong Password**

    For your **security**, please ensure your password meets the following criteria:

    ✅ **At least 8 characters** (longer passwords provide better security)  
    ✅ **At least one uppercase letter** (`A-Z`)  
    ✅ **At least one lowercase letter** (`a-z`)  
    ✅ **At least one number** (`0-9`)  
    ✅ **At least one special character** (`!@#$%^&*()-_+=`)  

    ⚠️ **Security Tip:** Avoid using common or easily guessable passwords (e.g., `password123`, `12345678`).  
    💡 **Best Practice:** Consider using a **passphrase** (e.g., `"Green$ky@2024"`) for added security.  
    🔒 **Your password is personal—never share it with anyone.**  
    📌 We recommend using a **password manager** to generate and store secure passwords safely.  

    """)

elif tabs == "About App":

    # About App Section
    st.markdown(
        """
        # 🔐 Password Sentinel 
        ## Your Ultimate Password Strength Analyzer

        Developed by **SMAASU Corporation**, Password Sentinel is an advanced web application designed to evaluate and enhance password security. This tool provides real-time password analysis, strength classification, and security suggestions to help you create unbreakable passwords.

        ## ✨ Key Features:
        - 🛡 **Strength Assessment** – Checks uppercase, lowercase, numbers, and special characters.
        - 📊 **Password Strength Rating** – Categorizes passwords as **Weak, Moderate, or Strong**.
        - ⏳ **Crack Time Estimation** – Predicts how long a brute-force attack would take.
        - ⚠ **Requirement Suggestions** – Highlights missing security requirements.
        - 🔑 **Strong Password Generator** – Suggests highly secure passwords if needed.
        - 🔐 **Security Tips** – Educates users on best password practices.

        🚀 **Ensure your passwords are robust and secure with Password Sentinel!**  
        """,
        unsafe_allow_html=True
    )
            
elif tabs == "About Me":
    st.write("# 🏅 Syed Muhammad Abdullah Abdulbadeeii")
    col1, col2, col3 = st.columns([4.5,1,4.5])
    with col1:
    # Personal Title 🏅🌟💡🌱🌍👤
        st.write("\n\n")
        st.markdown(
        "<img src='https://raw.githubusercontent.com/smaasui/SMAASU/main/16.jpeg' width='550'>",
        unsafe_allow_html=True)

        # st.image("https://raw.githubusercontent.com/smaasui/SMAASU/main/16.jpeg", use_container_width=True, width=100)
        # Expertise & Interests
        st.write("\n\n")
        st.header("🚀 Areas of Expertise")
        st.markdown(
            """
            - 🏗️ **Civil Engineering & Smart Infrastructure** – Engineering sustainable and innovative urban solutions.
            - 💻 **Software & Web Development** – Creating intelligent digital solutions to optimize efficiency.
            - 🤖 **Artificial Intelligence & Data Science** – Harnessing AI-driven technologies for smarter decision-making.
            - 📊 **Data Processing & Automation** – Streamlining complex workflows through advanced automation.
            - 🚀 **Entrepreneurship & Technological Innovation** – Spearheading startups that drive meaningful change.
            - ❤️ **Philanthropy & Social Impact** – Advocating for and supporting communities in need.
            """
        )


    with col3:
        st.write("# 🌱 About Me")
        # Introduction
        st.markdown(
            """
            I am **Syed Muhammad Abdullah Abdulbadeeii**, a **Civil Engineering Student at NED University of Engineering & Technology, Entrepreneur, Innovator, and Philanthropist**. 
            With a deep passion for **Artificial Intelligence, Architecture, and Sustainable Urbanization**, I am committed to pioneering **Transformative Solutions** that seamlessly integrate technology with real-world applications.
            
            My work is driven by a vision to **Build a Smarter, More Sustainable Future**, where cutting-edge innovations enhance efficiency, improve urban living, and empower businesses. 
            Beyond my professional pursuits, I am dedicated to **philanthropy**, striving to **uplift Muslims and support underprivileged communities**, fostering a society rooted in compassion, empowerment, and progress.
            """
        )
        
        # Vision & Journey
        st.header("🌍 My Vision & Journey")
        st.markdown(
            """
            As the founder of **SMAASU Corporation**, I have led groundbreaking initiatives such as **Data Duster**, a web-based platform revolutionizing data processing and automation. 
            My entrepreneurial journey is fueled by a relentless drive to **bridge the gap between technology and urban development**, delivering impactful solutions that **redefine the future of cities and industries**.
            
            **I believe in innovation, sustainability, and the power of technology to transform lives.** Through my work, I strive to create solutions that not only drive efficiency but also foster inclusivity and social well-being.
            
            **Let’s collaborate to build a brighter, more progressive future!**
            """
        )

elif tabs == "About Us":

    # Company Title
    st.write("# 🏢 About SMAASU Corporation")

    # Introduction
    st.markdown(
        """
        **SMAASU Corporation** is a forward-thinking company committed to innovation in **technology, architecture, and sustainable urbanization**.
        Our vision is to create cutting-edge solutions that simplify workflows, enhance productivity, and contribute to a smarter, more efficient future.
        """
    )

    # Mission Section
    st.header("🌍 Our Mission")
    st.markdown(
        """
        At **SMAASU Corporation**, we aim to:
        - 🚀 **Develop pioneering software solutions** that enhance business efficiency.
        - 🏗️ **Revolutionize architecture and urban planning** with smart, sustainable designs.
        - 🌱 **Promote sustainability** in every project we undertake.
        - 🤝 **Empower businesses and individuals** with next-gen technology.
        """
    )

    # Core Values Section
    st.header("💡 Our Core Values")
    st.markdown(
        """
        - **Innovation** – Continuously pushing boundaries with cutting-edge technology.
        - **Sustainability** – Building a future that is eco-friendly and efficient.
        - **Excellence** – Delivering top-tier solutions with precision and quality.
        - **Integrity** – Upholding transparency and trust in every endeavor.
        """
    )

    # Call to Action
    st.markdown(
        """
        🚀 **Join us on our journey to create a smarter, more sustainable world with SMAASU Corporation!**
        """,
        unsafe_allow_html=True
    )
    st.link_button("🔗 Visit SMAASU Corporation", "https://g.co/kgs/VvQB8W9")



            