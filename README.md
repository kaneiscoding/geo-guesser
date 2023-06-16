# geo-guesser

Project Organization
------------
Folder structure or organziation for this project:
```
├── README.md                       <- The top-level README for developers using this project.
├── .gitignore                      <- Ignores files that shouldn't go into git (e.g. ./data/).
├── Dockerfile                      <- Dockerfile for building jupyterlab container.
├── docker-compose.yml              <- Container instructions used when running docker-compose.
├── requirements.txt                <- List of dependancies to be installed in the docker containers.
│
├── app                             <- Application 
│
├── data
│   ├── csv                         <- Data contained in csv format.
│   ├── raw                         <- Raw image data.
│   ├── train                       <- Image data split into the training set used to train the models.
│   └── validation                  <- Image data split into the validation set used to validate the models.
│                       
│
├── notebooks                       <- Jupyter notebooks. Naming convention is a short `-` delimited description.
│   ├── draft                       <- Draft notebooks for creating models etc.    
│   └── final                       <- The final notebooks to demonstrate and can be run from start from finish. 
│
│
└── src                             <- Python modules to be used in the notebooks.
```
