import os
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO)


project_name = "ML_PROJECT"
list_of_files = [
    ".Github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitoring.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipelines.py",
    f"src/{project_name}/pipelines/prediction_pipelines.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile",
    "Requirements.txt",
    "setup.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)  
    filedir, filename = os.path.split(filepath)  

    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    
    if (not filepath.exists()) or (filepath.stat().st_size == 0):
        with open(filepath, 'w') as f:
            pass  
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} already exists")

