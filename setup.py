from setuptools import setup, find_packages

setup(
    name="vc_dilution_calculator",
    version="1.0.0",
    description="VC Ownership Dilution Calculator built with Streamlit",
    author="Mariam Younis",
    author_email="mariam.youniis@gmail.com",
    packages=find_packages(),  # This automatically includes all folders with __init__.py
    install_requires=[
        "streamlit",
    ],
    python_requires='>=3.7',
)
