#!/usr/bin/env python
from setuptools import find_packages, setup
# from pip.req import parse_requirements

setup(
    name='VKR_3D_Reconstruction',
    version='0.1.3',    
    description='VKR_3D_Reconstruction',
    url='https://github.com/Sashiyamo/VKR_3D_Reconstruction',
    author='Denisov Alexander',
    author_email='chatt-171@yandex.ru',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
            "opencv-python",
            "joblib",
            "scikit-learn",
            "pyrender",
            "dill",
            "rich",
            "einops",
            "scenedetect[opencv]",
            "hydra-core",
            "timm",
            "av",
            "smplx==0.1.28",
            "numpy",
            "detectron2 @ git+https://github.com/facebookresearch/detectron2.git",
            "pytube @ git+https://github.com/pytube/pytube.git",
            "pyopengl @ git+https://github.com/mmatl/pyopengl.git",
            "chumpy @ git+https://github.com/mattloper/chumpy", # smplx dependency
            "neural-renderer-pytorch @ git+https://github.com/shubham-goel/NMR.git",
        ],
    extras_require={
        'all': [
            "hmr2 @ git+https://github.com/shubham-goel/4D-Humans.git",
        ],
        'blur': [
            'facenet_pytorch'
        ]
    },
    dependency_links=[]
)
