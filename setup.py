""" Polyend Tracker .pti creator setup """
from setuptools import setup

setup(
    name="polyend_tracker_pti_creator",
    version="0.0.1",
    packages=[
        "polyend_tracker_pti_creator",
        "polyend_tracker_pti_creator.utils",
        "polyend_tracker_pti_creator.utils.audio",
        "polyend_tracker_pti_creator.utils.pti",
    ],
    python_requires=">=3",
    entry_points={
        "console_scripts": ["pet-pti-creator=polyend_tracker_pti_creator.creator:main"]
    },
    test_suite="tests",
    url="https://github.com/adriananders/polyend-tracker-pti-creator",
    license="MIT",
    author="Adrian Anders",
    author_email="realaanders@gmail.com",
    description="Polyend Tracker .pti instrument creator",
)
