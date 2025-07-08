from setuptools import setup

setup(
    name="deepseek_cli",
    version="1.0.0",
    description="Cliente CLI para DeepSeek com contexto de arquivos",
    author="Anthony",
    py_modules=["main", "config", "context_loader", "chat_engine"],
    install_requires=[
        "requests",
        "rich",
        "tqdm",
        "setuptools",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "deepseekcli = main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
