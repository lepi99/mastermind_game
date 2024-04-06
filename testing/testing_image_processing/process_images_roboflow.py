from roboflow import Roboflow

rf=Roboflow(api_key="8EyzahJG84fbgVEUGXk8")
project= rf.workspace("lepi").project("mastermind")
settings_d={"augmentation": {},
"preprocessing": {}}
new_version = project.generate_version(settings=settings_d)

#version = project.version("VERSION_NUMBER")
#download(model_format="yolov8", location="roboflow_export/", overwrite= True):


rf = Roboflow(api_key="8EyzahJG84fbgVEUGXk8")
project = rf.workspace("lepi").project("mastermind")
dataset = project.version(1).download("yolov8")

