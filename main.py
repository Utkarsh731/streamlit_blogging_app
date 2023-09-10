import streamlit as st

# set the page config
st.set_page_config(page_title="Ink and Pixels: Crafting My Digital Sanctuary", page_icon="🤓", layout="wide",
                   initial_sidebar_state="expanded",
                   menu_items={'Get Help': 'https://www.linkedin.com/in/utkarsh-shukla-1520a8255/',
                               'Report a bug': "https://www.utkarshshukla.com/",
                               'About': "Tech wizard and innovation enthusiast 💻 Product Owner at NerdyBio and Full Stack Developer at StatusNeo. With 120+ thought-provoking blogs published on cutting-edge technologies, my expertise in System and Database Designing is second to none. I bring proficiency in Python with a strong grip on frameworks such as Flask and Django, and databases including MongoDB, RDS, and Redshift. And, let's not forget my work with Java and SpringBoot, which led to the development of a low code no code platform for IIoT applications. Award-winning professional 🏆 Recognized with the Student of the Semester Award, Best Blogger Award, and Immense Contribution Award from various organizations and universities, I am constantly pushing the limits and delivering exceptional results. Join me in my journey to revolutionize the tech world! 🚀"})

# set the header
with st.container():
    st.title("Ink and Pixels: Crafting My Digital Sanctuary")
    st.write(
        "I am [Utkarsh Shukla](https://www.utkarshshukla.com/), an explorer of life, a curious learner, and an evangelist of my passions. My multiple hats include a [poet](https://www.utkarshshukla.com/poetry), [photographer](https://www.pexels.com/@utkarsh-shukla-204757820/), magician, consultant, numismatist, and of course, a software engineer. I am a student of life who firmly believes in continuous learning and the phrase, 'Never Rest, Never Rust.'")
    st.write("---")

blogs = [{"title": "Mastering Error Handling and Debugging in Python: A Comprehensive Guide with Examples",
    "image_url": "https://images.pexels.com/photos/17574687/pexels-photo-17574687.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
    "description": "Error handling and debugging are essential skills for any Python programmer. In this comprehensive guide, we will explore the world of error handling and debugging in Python, equipping you with the knowledge and tools to effectively identify, diagnose, and resolve issues in your code. Whether you’re a beginner or an experienced developer, mastering these techniques will help you write more robust and reliable Python applications.",
    "blog_url": "https://medium.com/@utkarshshukla.author/mastering-error-handling-and-debugging-in-python-a-comprehensive-guide-with-examples-b6e8258a5c4c", },
    {"title": "Best Python Coding Practices: Writing Clean and Efficient Code",
        "image_url": "https://images.pexels.com/photos/16822804/pexels-photo-16822804/free-photo-of-laptop-side-laptop-view.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        "description": "Python is a powerful and popular programming language known for its simplicity and readability. To make the most out of Python’s capabilities, it’s crucial to follow best coding practices. Writing clean, efficient, and maintainable code not only enhances the readability but also reduces bugs and makes collaboration with other developers easier. In this blog, we will explore some of the best Python coding practices with examples to demonstrate their importance.",
        "blog_url": "https://medium.com/@utkarshshukla.author/best-python-coding-practices-writing-clean-and-efficient-code-4784946a17d0", },
    {"title": "Python’s Powerful Trio: Map, Filter, and Reduce for Simplifying Data Processing",
        "image_url": "https://images.pexels.com/photos/16397035/pexels-photo-16397035.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        "description": "Map, filter, and reduce are three powerful functions in Python that allow you to manipulate and transform data in efficient and concise ways. These functions are part of the functional programming paradigm, which emphasizes immutability and the use of higher-order functions to create more modular and reusable code. In this blog, we will explore these functions and provide real-life examples of how they can be used.",
        "blog_url": "https://medium.com/@utkarshshukla.author/pythons-powerful-trio-map-filter-and-reduce-for-simplifying-data-processing-f4ab79fd076f", },
    {"title": "Understanding Memory Management in Python: A Comprehensive Guide with Real-Life Examples",
        "image_url": "https://images.pexels.com/photos/15909996/pexels-photo-15909996.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        "description": "Memory management is a crucial aspect of any programming language, and Python is no exception. Python’s memory management is designed to be efficient and user-friendly, but it’s essential to understand how it works to write efficient and bug-free code. In this blog, we’ll explore Python’s memory management in detail, complete with real-life examples to illustrate key concepts.",
        "blog_url": "https://fourofour.org/understanding-memory-management-in-python-a-comprehensive-guide-with-real-life-examples/", },
    {"title": "Generative AI: How It’s Disrupting Industries and Changing the World",
        "image_url": "https://images.pexels.com/photos/15244394/pexels-photo-15244394.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2",
        "description": "In recent years, the field of artificial intelligence (AI) has witnessed significant advancements, with generative AI emerging as a groundbreaking technology. Generative AI refers to a subset of AI that focuses on creating new content, such as images, music, text, and even videos, mimicking human-like creativity and innovation. By leveraging deep learning techniques and massive datasets, generative AI has the potential to revolutionize various industries, from entertainment and art to healthcare and manufacturing. This article delves into the what, why, and how of generative AI, exploring its applications and implications.",
        "blog_url": "https://statusneo.com/generative-ai-how-its-disrupting-industries-and-changing-the-world/?swcfpc=1", }

]

# Page title
st.title("Trending Blogs")

# Loop through the list of blogs and display them
for blog in blogs:
    st.header(blog['title'])
    st.write("##")
    blog_url = blog['blog_url']
    image_url = blog['image_url']
    description = blog['description']
    image_column, text_column = st.columns((1, 2))
    with image_column:
        # st.markdown(f"<a href='{blog['blog_url']}' target='_blank'><img src='{blog['image_url']} alt='Blog Image' width='200'></a>",unsafe_allow_html=True)
        # Display the image as a hyperlink with a background cover effect
        # Display the image as a hyperlink with a background cover effect
        st.markdown(
            f"<a href='{blog_url}' target='_blank' style='display: block; width: 400px; height: 200px; background-image: url({image_url}); background-size: cover;'></a>",
            unsafe_allow_html=True)
    with text_column:
        # Set the line height for the text
        line_height = "3"  # Adjust this value as needed

        # Display the text with a clickable link and custom line height
        st.markdown(f"<a href='{blog_url}' target='_blank' style='line-height: {line_height};'>{description}</a>",
            unsafe_allow_html=True)
    st.write("---")

# Define your information
name = "Utkarsh Shukla"
bio = "An explorer of life, a curious learner, and an evangelist of my passions. My multiple hats include a poet, photographer, magician, consultant, numismatist, and of course, a software engineer. I am a student of life who firmly believes in continuous learning and the phrase, 'Never Rest, Never Rust.'"

# Create a footer section
st.markdown(f"""
    {bio}

    [LinkedIn](https://www.linkedin.com/in/your-profile)
    [GitHub](https://github.com/your-profile)

    &copy; {name} - {2023}
    """, unsafe_allow_html=True)
